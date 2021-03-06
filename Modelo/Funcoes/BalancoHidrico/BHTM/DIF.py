# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: Paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA, RasterData
import subprocess
import gdal
import sys
from Modelo.beans.RasterData import RasterFile
progress = gdal.TermProgress_nocb
import numpy

class Etc(AbstractFunction):
    '''
        Essa função calcula a diferença (DIF, mm) entre a precipitação e a evapotranspiração da cultura (ETc)
        Formula: DIF = PPP - ETc
        Para efeitos de histórico, periodos de ETc anteriores ao periodo da cultura devem ser inseridos, por default quando a
    cultura não está presente, o Kc é considerado de valor 1
        
        Esta função não entende datas por isso todos os parametros devem ser passados com referencia a cena
    '''
    
    def __setParamIN__(self):
        
        self.descriptionIN["DIF"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de diferença"}
        self.descriptionIN["PPP"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de precipitacao"}
        self.descriptionIN["ETc"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de evapotranspiração da cultura"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["DIF"] = {"Type":SERIAL_FILE_DATA, "Description":"Série de imagens de evapotranspiração da cultura"}
    
    def __execOperation__(self):
        '''
            Por padrão agora assumo que, quando uma variavel tiver como sufixo um underline "_"
            é porque esta variavel contem os valores carregados (matrizes brutas) dos dados
        '''
        
        serie_ET0 = self.paramentrosIN_carregados["ET0"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_Kc = self.paramentrosIN_carregados["Kc"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_ETc = self.paramentrosIN_carregados["ETc"] # pucha lista
        
        Kc_factor = float(serie_Kc.mutiply_factor)
        ET0_factor = serie_ET0.mutiply_factor
        ETC_factor = serie_ETc.mutiply_factor
        
        
        
        for i_Kc in range(len(serie_Kc)):
            #gdal_calc.py [-A <filename>] [--A_band] [-B...-Z filename] [other_options]
            Kc = serie_Kc[i_Kc]
            data_kc = serie_Kc.getDate_time(file=Kc)
            
            ET0 = self.procurar_descende_correspondente(data_kc, serie_ET0)
            
            etc = RasterFile(file_path=serie_ETc.root_path, ext="tif", file_name=Kc.file_name)
            
            ET0_ = numpy.array(ET0.loadRasterData()).astype(dtype="float32") * ET0_factor
            Kc_ = numpy.array(Kc.loadRasterData()).astype(dtype="float32") * Kc_factor
            
            dias_decend = self.dias_decend
            
            ETc_ = Kc_ * (ET0_  / dias_decend) * ETC_factor
            
            #print ET0.file_full_path
            #print Kc.file_full_path
            
            etc.metadata = Kc.metadata
            etc.data = ETc_
            etc.saveRasterData()
            
    
    def procurar_descende_correspondente(self, data, serie_temporal):
        '''
            Esse método procura a imagem correspondente para a data informada (feito para capturar o descende correto)
        '''
        img_correspondente = None
        
        for i_img in range(len(serie_temporal)-1):
            data_img =  serie_temporal.getDate_time(i_img)
            data_img_1 = serie_temporal.getDate_time(i_img+1)
            if data_img == data : 
                img_correspondente = serie_temporal[i_img]
                self.dias_decend = (data_img_1 - data_img).days
                break
            elif data_img < data and data_img_1 > data: 
                img_correspondente = serie_temporal[i_img]
                self.dias_decend = (data_img_1 - data_img).days
        
        if img_correspondente == None : img_correspondente = serie_temporal[-1]
           
        return img_correspondente

if __name__ == '__main__':
    from Modelo.beans import SerialTemporalFiles
    
    serie_Kc = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\Kc_distribuido\\soltas")
    serie_Kc.mutiply_factor = 0.01
    serie_Kc.date_mask = "%Y-%m-%d"
    
    serie_ET0 = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\7-Cortado_tamanho_Modis\\EVPT")
    serie_ET0.sufixo = "evpt_"
    serie_ET0.date_mask = "%Y%m%d"
    
    serie_ETC = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\ETc")
    serie_ETC.sufixo = "ETc_"
    serie_ETC.date_mask = "%Y-%m-%d"
    
    paramIN = dict()
    paramIN["ET0"] = serie_ET0
    paramIN["ETc"] = serie_ETC
    paramIN["Kc"] = serie_Kc
    
    Etc().executar(paramIN)
    


