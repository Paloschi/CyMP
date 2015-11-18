# -*- coding: utf-8 -*-
'''
Created on Nov 18, 2015

@author: rennan.paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA
import threading
import numpy
from Modelo.beans.RasterData import RasterFile

class Ks(AbstractFunction):
    
    def __setParamIN__(self):
        
        self.descriptionIN["RAW"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagem RAW"}
        self.descriptionIN["TAW"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens TAW"}
        self.descriptionIN["Dr"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagem Dr"}
        self.descriptionIN["Ks"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagem Ks"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["Ks"] = {"Type":SERIAL_FILE_DATA, "Description":"Série de imagen Ks"}
    
    def __execOperation__(self):
        
        serie_raw = self.paramentrosIN_carregados=["RAW"].loadListByRoot()
        serie_taw = self.paramentrosIN_carregados=["TAW"].loadListByRoot()
        serie_dr = self.paramentrosIN_carregados=["Dr"].loadListByRoot()
        
        serie_ks = self.paramentrosIN_carregados=["Ks"]
        
        factor_raw = float(serie_raw.mutiply_factor)
        factor_taw = float(serie_taw.mutiply_factor)
        factor_dr = float(serie_dr.mutiply_factor)
        factor_ks = float(serie_ks.mutiply_factor)
        
        n_taw = len(serie_taw)
        
        taw_ = serie_taw[0].loadRasterData()
        n_linhas = len(taw_)
        n_colunas = len(taw_[0])
        
        for i in range(n_taw):
            
            if threading.currentThread().stopped()  : return 
            self.setProgresso(i, n_taw)
            
            taw = serie_taw[i]
            data_taw = serie_taw.getDate_time(file=taw)
            taw_ = numpy.array(taw.loadRasterData()).astype(dtype="float32")
            taw_ *= factor_taw
            
            raw_ = self.LoadImgByDate(serie_raw, data_taw, factor_raw)
            dr_ = self.LoadImgByDate(factor_dr, data_taw, factor_dr)
            
            ''' ----------------------------------------------- '''
            
            ks_ = numpy.zeros((n_linhas, n_colunas))
            ks_ +=1
            
            ''' ----------------------------------------------- '''
            
            temp = numpy.array(numpy.zeros((n_linhas, n_colunas))).astype(dtype="float32")
            temp = (taw_ - dr_) / (taw_ - raw_)
            
            for i in range(len(taw_)) :
                ks_[i][dr_ >= raw_] = temp[i][dr_ >= raw_]
            
            ''' ------------------------------------------------ '''
            
            ks_ = numpy.round(ks_, 2)  
            ks_ *= factor_ks
            ks_ = self.compactar(ks_)
            
            
            ks = RasterFile(file_path=serie_ks.root_path, ext="tif")
            ks = serie_ks.setDate_time(data_taw, file=ks)       
            ks.data = ks_
            ks.metadata = taw.metadata
            ks.saveRasterData()
            ks.data = None
            serie_ks.append(ks)
            
        return serie_ks
            
    def LoadImgByDate(self, serie, date, factor):          
            img = self.procura_img_por_data(serie, date)
            img_ = numpy.array(img.loadRasterData()).astype(dtype="float32")
            img_ *= factor  
            return img_