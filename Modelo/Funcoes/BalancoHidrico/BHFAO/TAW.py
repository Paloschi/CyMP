# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: Paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA, FILE_DATA
import gdal
from Modelo.beans.RasterData import RasterFile
progress = gdal.TermProgress_nocb
import numpy
import threading

class TAW(AbstractFunction):
    '''
        Essa função calcula a TAW
    '''
    def __setParamIN__(self):
        
        self.descriptionIN["CAD"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de capacidade de armazenamento de agua no solo CAD"}
        self.descriptionIN["Zr"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de Zr distribuido"}
        self.descriptionIN["TAW"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Configuração para a saída da série de imagens TAW"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["TAW"] = {"Type":SERIAL_FILE_DATA, "Description":"Série de imagens TAW"}
    
    def __execOperation__(self):

        self.console("Carregando imagens.")
        
        serie_Zr = self.paramentrosIN_carregados["Zr"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_TAW = self.paramentrosIN_carregados["TAW"]
        CAD_ = self.paramentrosIN_carregados["CAD"].loadRasterData() # pucha lista
        
        Zr_factor = float(serie_Zr.mutiply_factor)
        TAW_factor = float(serie_TAW.mutiply_factor)
        
        n_zr = len(serie_Zr)
        
        self.console(str(n_zr) + " imagens de Zr encontradas.")
        self.console(u"Gerando série de imagens TAW..")

        '''
            O laço a seguir percorre todas as imagens de Zr presentes
            O calculo da TAW é Zr = CAD * Zr
        '''

        for i in range(n_zr):
            
            if threading.currentThread().stopped()  : return 
            self.setProgresso(i, n_zr)

            zr = serie_Zr[i]
            data_zr = serie_Zr.getDate_time(file=zr)
            zr_ = numpy.array(zr.loadRasterData()).astype(dtype="float32")
            zr_ = zr_ * Zr_factor
            
            taw_ = zr_ * CAD_       
            taw_ *= TAW_factor
            
            taw = RasterFile(file_path=serie_TAW.root_path, ext="tif")
            taw = serie_TAW.setDate_time(data_zr, file=taw)       
            taw.data = taw_
            taw.metadata = zr.metadata
            taw.saveRasterData()
            
            taw.data = None
            serie_TAW.append(taw)
        
        return serie_TAW


