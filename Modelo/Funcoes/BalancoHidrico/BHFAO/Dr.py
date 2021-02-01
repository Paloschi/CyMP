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
        
        
        #Etc_factor = float(serie_Etc.mutiply_factor)
        PPP_factor = float(serie_PPP.mutiply_factor)
        #TAW_factor = float(serie_TAW.mutiply_factor)
        #Dr_factor = float(serie_Dr.mutiply_factor)
        
        n_ETc = len(serie_Etc)

        
        self.console(str(len(serie_PPP)) + u" imagens de precipitação encontradas.")
        self.console(str(len(serie_Etc)) + u" imagens de Etc encontradas.")
        self.console(str(len(serie_TAW)) + u" imagens de TAW encontradas.")
        self.console(u"Gerando balanço...")

        '''
            O laço a seguir percorre todas as imagens de Zr presentes
            O calculo da TAW é Zr = CAD * Zr
        '''
        
        Dr_anterior = None

        ppp_index = None
        taw_index = None

        for i in range(n_ETc):

            if threading.currentThread().stopped()  : return 
            self.setProgresso(i, n_ETc)

            ETc = serie_Etc[i]
            ETc_data = serie_Etc.getDate_time(file=ETc)
            etc_ = numpy.array(ETc.loadRasterData()).astype(dtype="float32")

            ppp, ppp_index = self.procura_img_por_data(serie_PPP, ETc_data, ppp_index)
            if ppp is not None:
                ppp_ = numpy.array(ppp.loadRasterData()).astype(dtype="float32")
                ppp_ = ppp_ * PPP_factor
                ppp_ = ppp_
            else:
                self.console("Rain image not found for ETc date: " + str(ETc_data))

            taw, taw_index = self.procura_img_por_data(serie_TAW, ETc_data, taw_index)

            if taw is not None:
                taw_ = numpy.array(taw.loadRasterData()).astype(dtype="float32")
                #taw_ = taw_ * PPP_factor
                taw_ = taw_
            else:
                self.console("TAW image not found for ETc date: " + str(ETc_data))
                taw_[numpy.where(taw_ <= 0)] = CAD_[numpy.where(taw_ <= 0)]

            if Dr_anterior is None:
                Dr_anterior = -CAD_

            print("Valor de ppp_:" + str(ppp_[970][483]))
            print("Valor de etc_:" + str(etc_[970][483]))
            print("Valor de Dr_anterior:" + str(Dr_anterior[970][483]))

            #Dr_ = etc_ - ppp_ + Dr_anterior

            Dr_ = Dr_anterior - ppp_ + etc_

            for i in range(len(taw_)) :
                Dr_[i][Dr_[i] > taw_[i]] = taw_[i][Dr_[i] > taw_[i]]
                #"isso aqui em baixo é pro balanço idrico nao ser menor que 0 ou seja o Dr nao pode ser maior q 0"
                Dr_[i][Dr_[i] < 0] = 0

            print("Valor de Dr_:" + str(Dr_[970][483]))


            print("Valor de taw_:" + str(taw_[970][483]))

            print("------------------------------")

            Dr_anterior = numpy.copy(Dr_)



            #Dr_ = numpy.round(Dr_, 2)   
            #Dr_ *= Dr_factor
            
            #Dr_ = self.compactar(Dr_)        
            
            dr = RasterFile(file_path=serie_Dr.root_path, ext="tif")
            dr = serie_Dr.setDate_time(ETc_data, file=dr)
            dr.data = Dr_
            dr.metadata = ppp.metadata
            dr.metadata.update(dtype = dr.data.dtype)
            dr.saveRasterData()
            dr.data = None
            serie_Dr.append(dr)
  
        return serie_Dr

