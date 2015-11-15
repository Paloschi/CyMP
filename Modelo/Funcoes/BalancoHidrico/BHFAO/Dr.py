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

class Dr(AbstractFunction):
    '''
        Essa função calcula o esgotamento
    '''
    def __setParamIN__(self):
        
        self.descriptionIN["Etc"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de Etc"}
        self.descriptionIN["PPP"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de precipitação distribuido"}
        self.descriptionIN["TAW"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens TAW"}
        self.descriptionIN["Dr"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Configuração pra Série de imagens Dr"}
        self.descriptionIN["CAD"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de capacidade de armazenamento de agua no solo CAD"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["Dr"] = {"Type":SERIAL_FILE_DATA, "Description":"Série de imagens Dr"}
    
    def __execOperation__(self):

        self.console("Carregando imagens.")
        
        serie_Etc = self.paramentrosIN_carregados["Etc"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_PPP = self.paramentrosIN_carregados["PPP"].loadListByRoot() 
        serie_TAW = self.paramentrosIN_carregados["TAW"].loadListByRoot() 
        serie_Dr = self.paramentrosIN_carregados["Dr"]
        CAD_ = self.paramentrosIN_carregados["CAD"].loadRasterData()
        
        
        Etc_factor = float(serie_Etc.mutiply_factor)
        PPP_factor = float(serie_PPP.mutiply_factor)
        TAW_factor = float(serie_TAW.mutiply_factor)
        Dr_factor = float(serie_Dr.mutiply_factor)
        
        n_ppp = len(serie_PPP)
        
        self.console(str(n_ppp) + u" imagens de precipitação encontradas.")
        self.console(str(len(serie_Etc)) + u" imagens de Etc encontradas.")
        self.console(str(len(serie_TAW)) + u" imagens de TAW encontradas.")
        self.console(u"Gerando balanço...")

        '''
            O laço a seguir percorre todas as imagens de Zr presentes
            O calculo da TAW é Zr = CAD * Zr
        '''

        for i in range(n_ppp):
            
            if threading.currentThread().stopped()  : return 
            self.setProgresso(i, n_ppp)

            ppp = serie_PPP[i]
            data_ppp = serie_PPP.getDate_time(file=ppp)
            ppp_ = numpy.array(ppp.loadRasterData()).astype(dtype="float32")
            ppp_ *= PPP_factor
            
            etc = self.procura_img_por_data(serie_Etc, data_ppp)
            if etc is not None :
                etc_ = numpy.array(etc.loadRasterData()).astype(dtype="float32")
                etc_ *= Etc_factor
                
            taw = self.procura_img_por_data(serie_TAW, data_ppp)
            if taw is not None :
                taw_ = numpy.array(taw.loadRasterData()).astype(dtype="float32")   
                taw_ *= TAW_factor 
            else :
                taw_ = CAD_
                       
            if etc is not None : 
                dif_ = ppp_ - etc_
            else :
                dif_ = ppp_   
              
            Dr_ = taw_
            
            mask = taw_ > dif_
            
            for m in mask:
                print m
            
            print mask
            
            if etc is not None : 
                Dr_[mask] = etc_ - ppp_      
            Dr_ *= Dr_factor
            
            dr = RasterFile(file_path=serie_Dr.root_path, ext="tif")
            dr = serie_Dr.setDate_time(data_ppp, file=dr)       
            dr.data = Dr_
            dr.metadata = ppp.metadata
            dr.saveRasterData()
            
            dr.data = None
            serie_Dr.append(dr)
        
        return serie_Dr

    def procura_img_por_data(self, serie, data):
        img = None
        for i in range(len(serie)):
            data_i = serie.getDate_time(file=serie[i])
            if data_i == data:
                img = serie[i]
                break  
        return img