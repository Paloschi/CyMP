# -*- coding: utf-8 -*-
'''
Created on Sep 10, 2015

@author: rennan.paloschi
'''

from Modelo.Funcoes import AbstractFunction
from Modelo.beans import TABLE_DATA, FILE_DATA, RasterFile
import datetime
import numpy as np
from numpy.core.numeric import array
from datetime import timedelta

class DistribuidorKC(AbstractFunction):
    
    ''' Essa classe pega o KC tabelado e transforma em um cubo temporal de kc pra cada cultura dependendo da data de colheita e semeadura '''
    
    def __setParamIN__(self):
        self.descriptionIN["Kc"] = {"Required":True, "Type":TABLE_DATA, "Description":"Dados Kc tabelado"}
        self.descriptionIN["semeadura"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de semeadura"}
        self.descriptionIN["colheita"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de colheita"}  
        
    def __setParamOUT__(self):
        self.descriptionOUT["images"] = "Série de imagens kc distribuidas de acordo com as imagens de semeadura e  colheita" 
            
    def __execOperation__(self):
        
        try:
            semeadura_ = self.paramentrosIN_carregados["semeadura"].loadRasterData()
            colheita_ = self.paramentrosIN_carregados["colheita"].loadRasterData()
        except: 
            print "não foi possivel carregar as imagens de semeadura e colheita"
            return None
        try:
            #data_minima = self.Ds_DC_to_date(np.min(img_semeadura))
            data_minima = self.Ds_DC_to_date("2013240")
            #data_maxima = self.Ds_DC_to_date(np.max(img_colheita))
            data_maxima = self.Ds_DC_to_date("201499")
        except:
            print "não foi possivel converter os valores das imagens de semeadura e colheita em datas"
            return None
        
        kc_vetorizado = self.vetorizar_kc()
        pf = len(kc_vetorizado)
        
        n_linhas = len(semeadura_)
        n_colunas = len(colheita_[0])
        
        for i_dia in range ((data_maxima-data_minima).days):
            dia = data_minima + timedelta(i_dia)
            imagem_kc = RasterFile()
            imagem_kc.data = array(semeadura_)
            imagem_kc.name = dia.date()
                    
            for i_linha in range(0, n_linhas):
                for i_coluna in range(0, n_colunas):
                    Ds = self.Ds_DC_to_date(semeadura_[i_linha][i_coluna])
                    Dc = self.Ds_DC_to_date(colheita_[i_linha][i_coluna])
                    delta_c = Dc - Ds
                    
                    if(dia >= Ds and dia <= Dc):
                        k = dia - Ds 
                        
                        i_FKc = int(k * delta_c / pf)
                        Kc = kc_vetorizado[i_FKc]
                        
                    else: Kc = 1
                    
                    imagem_kc.data[i_linha][i_coluna] = Kc
                    
            print imagem_kc.name
            print imagem_kc.data
            

                
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

    
    