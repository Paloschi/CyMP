# -*- coding: utf-8 -*-
'''
Created on 04/12/2015

@author: Paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA, FILE_DATA, SerialTemporalFiles
import gdal
from Modelo.beans.RasterData import RasterFile
progress = gdal.TermProgress_nocb
import numpy
import threading
from Modelo.beans import RasterFile, SERIAL_FILE_DATA

class Ya(AbstractFunction):
    '''
        Essa função calcula a TAW
    '''
    def __setParamIN__(self):
        
        self.descriptionIN["ETa"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"..."}
        self.descriptionIN["ETc"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"..."}
        self.descriptionIN["Ky"] = {"Required":True, "Type":None, "Description":"..."}
        self.descriptionIN["Yx"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"..."}
        self.descriptionIN["Ya"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"..."}
        self.descriptionIN["Kc"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"..."}
    
    def __setParamOUT__(self):
        self.descriptionOUT["Ya"] = {"Type":SERIAL_FILE_DATA, "Description":"..."}
    
    def __execOperation__(self):

        #self.console("Carregando imagens.")
        
        serie_eta = self.paramentrosIN_carregados["ETa"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_etc = self.paramentrosIN_carregados["ETc"].loadListByRoot()
        serie_yx = self.paramentrosIN_carregados["Yx"].loadListByRoot() # pucha lista
        serie_Kc = self.paramentrosIN_carregados["Kc"].loadListByRoot() # pucha lista
        serie_ya = self.paramentrosIN_carregados["Ya"]
        
        ky = self.paramentrosIN_carregados["Ky"]
        
        factor_eta = float(serie_eta.mutiply_factor)
        factor_etc = float(serie_etc.mutiply_factor)
        factor_yx = float(serie_yx.mutiply_factor)
        factor_ya = float(serie_ya.mutiply_factor)
        
        n_img = len(serie_Kc)
        
        #self.console("As imagens de Kc serão usadas como referencia")
        #self.console(str(n_img) + " imagens de Kc encontradas.")
        
        #self.console(u"Gerando série de imagens de Ya..")

        for i in range(n_img):
            
            #if threading.currentThread().stopped()  : return 
            #self.setProgresso(i, n_img)

            kc = serie_Kc[i]
            data_ref = serie_Kc.getDate_time(file=kc)
            kc_ = kc.loadRasterData()
            
            eta_ = self.LoadImgByDate(serie_eta, data_ref, factor_eta)
            etc_ = self.LoadImgByDate(serie_etc, data_ref, factor_etc)
            yx_ = self.LoadImgByDate(serie_yx, data_ref, factor_yx)
            
            
            p1= ky * (1-eta_/etc_)
            ya_ = (1-p1) * yx_
            
            for i in range(len(ya_)): 
                ya_[i][kc_[i]==0] = 0
            
            ya = RasterFile(file_path=serie_ya.root_path, ext="tif")
            ya = serie_ya.setDate_time(data_ref, file=ya)       
            ya.data = ya_
            ya.metadata = kc.metadata
            ya.metadata.update(nodata=0)
            ya.saveRasterData()
            
            ya.data = ya_
            
            serie_ya.append(ya)
        
        return serie_ya
    
    def LoadImgByDate(self, serie, date, factor):          
            img = self.procura_img_por_data(serie, date)
            img_ = numpy.array(img.loadRasterData()).astype(dtype="float32")
            img_ *= factor  
            return img_
        
    def testar(self):

        self.paramentrosIN_carregados = dict()
        self.paramentrosIN_carregados["ETa"] = SerialTemporalFiles(root_path="C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\6-Eta")
        self.paramentrosIN_carregados["ETa"].prefixo = "eta_"
        self.paramentrosIN_carregados["ETa"].date_mask = "%Y-%m-%d"
        self.paramentrosIN_carregados["ETa"].multply_factor = 0.01
        
        self.paramentrosIN_carregados["ETc"] = SerialTemporalFiles(root_path="C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\3-ETc")
        self.paramentrosIN_carregados["ETc"].prefixo = "etc_"
        self.paramentrosIN_carregados["ETc"].date_mask = "%Y-%m-%d"
        self.paramentrosIN_carregados["ETc"].multply_factor = 0.01
        
        self.paramentrosIN_carregados["Ky"] = 0.8
        
        self.paramentrosIN_carregados["Yx"] = SerialTemporalFiles(root_path="C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\5-PPR(Yx)")
        self.paramentrosIN_carregados["Yx"].prefixo = "ppr_"
        self.paramentrosIN_carregados["Yx"].date_mask = "%Y-%m-%d"
        self.paramentrosIN_carregados["Yx"].multply_factor = 1
        
        self.paramentrosIN_carregados["Ya"] = SerialTemporalFiles(root_path="C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\7-Ya2")
        self.paramentrosIN_carregados["Ya"].prefixo = "Ya_"
        self.paramentrosIN_carregados["Ya"].date_mask = "%Y-%m-%d"
        self.paramentrosIN_carregados["Ya"].multply_factor = 1
        
        self.paramentrosIN_carregados["Kc"] = SerialTemporalFiles(root_path="C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\2-Kc")
        self.paramentrosIN_carregados["Kc"].date_mask = "%Y-%m-%d"
         
        self.__execOperation__()
        
        
if __name__ == '__main__':
    ppr = Ya()
    ppr.testar()