# -*- coding: utf-8 -*-
'''
Created on Sep 10, 2015

@author: rennan.paloschi
'''

from Modelo.Funcoes import AbstractFunction
from Modelo.beans import TABLE_DATA, FILE_DATA, RasterFile
import datetime
import numpy as np

class DistribuidorKC(AbstractFunction):
    
    ''' Essa classe pega o KC tabelado e transforma em um cubo temporal de kc pra cada cultura dependendo da data de colheita e semeadura '''
    
    def __setParamIN__(self):
        self.descriptionIN["Kc"] = {"Required":True, "Type":TABLE_DATA, "Description":"Dados Kc tabelado"}
        self.descriptionIN["semeadura"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de semeadura"}
        self.descriptionIN["colheita"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de colheita"}  
        
    def __setParamOUT__(self):
        self.descriptionOUT["images"] = "Série de imagens kc distribuidas de acordo com as imagens de semeadura e  colheita" 
            
    def __execOperation__(self):
        
        kc_vetorizado = self.vetorizar_kc()
        try:
            img_semeadura = self.paramentrosIN_carregados["semeadura"].loadRasterData()
            img_colheita = self.paramentrosIN_carregados["colheita"].loadRasterData()
        except: 
            print "não foi possivel converter os valores das imagens de semeadura e colheita em datas"
        
        data_minima = self.Ds_DC_to_date(np.min(img_semeadura))
        data_maxima = self.Ds_DC_to_date(np.max(img_colheita))
        
        for i_dia in range (data_maxima-data_minima):
            dia = datetime.timedelta(data_minima+i_dia)

                
    def vetorizar_kc(self): 
        kc_vetorizado = list()
        for key in self.paramentrosIN_carregados["Kc"].keys():
            inicio = int(key.split("-")[0])
            fim = int(key.split("-")[1])
            for x in range(inicio, fim):
                kc_vetorizado.append(self.paramentrosIN_carregados["Kc"][key])
        return kc_vetorizado
    
    def Ds_DC_to_date(self, data):
        
        n = len(str(data))
        year = int(str(data)[0:4])    
        days = int(str(data)[4:n])
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
        return date
    
if __name__ == '__main__':   
    
    from Modelo.beans import TableData
    
    paramIN = dict()
    paramIN["semeadura"] = RasterFile(file_full_path="C:\\Users\\rennan.paloschi\\Desktop\\Dados_Gerais\\raster\\Pesada\\MYD13Q1.20150109.250m_16_dias_EVI_PR.tif")
    paramIN["colheita"] = RasterFile(file_full_path="C:\\Users\\rennan.paloschi\\Desktop\\Dados_Gerais\\raster\\Pesada\\MYD13Q1.20150501.250m_16_dias_EVI_PR.tif")
    paramIN["Kc"] = TableData()
    
    f = DistribuidorKC()
    f.executar(paramIN)

    
    