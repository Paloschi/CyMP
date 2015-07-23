# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: Paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA, TABLE_DATA, FILE_DATA

class Etc(AbstractFunction):
    '''
        Essa função calcula a evapotranspiração da cultura ETc, baseado nas datas de plantio, evapotranspiração de referencia
    e os coeficientes da cultura.
        Formula: ETc = Kc * ET0
        Onde o Kc varia dependendo do estado fenologico da cultura.
        Para efeitos de histórico, periodos de ETc anteriores ao periodo da cultura devem ser inseridos, por default quando a
    cultura não está presente, o Kc é considerado de valor 1
        
        Esta função não entende datas por isso todos os parametros devem ser passados com referencia a cena
    '''
    def __setParamIN__(self):
        
        self.descriptionIN["ET0"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de evapotranspiração de referencia"}
        self.descriptionIN["Kc"] = {"Required":True, "Type":TABLE_DATA, "Description":"Valores tabelados de Kc"}
        self.descriptionIN["semeadura"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de semeadura"}
        self.descriptionIN["colheira"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de colheita"}  
        self.descriptionIN["noData"] = {"Required":None, "Type":None, "Description":"Valor a ser ignorado (verificado na da data de semeadura)"}

    def __setParamOUT__(self):
        self.descriptionOUT["ETc"] = {"Type":SERIAL_FILE_DATA, "Description":"Série de imagens de evapotranspiração da cultura"}
    
    def __execOperation__(self):
        '''
            Por padrão agora assumo que, quando uma variavel tiver como sufixo um underline "_"
            é porque esta variavel contem os valores carregados (matrizes brutas) dos dados
        '''
        
        print("Carregando imagens (ET0, semeadura, colheita): ")
        
        serie_et0_ = self.paramentrosIN_carregados["ET0"].loadRasterData()
        semeadura_ = self.paramentrosIN_carregados["semeadura"].loadRasterData()
        colheita_ = self.paramentrosIN_carregados["colheita"].loadRasterData()
        
        n_imagens = len(serie_et0_)
        n_linhas = len(serie_et0_[0])
        n_colunas = len(serie_et0_[0][0])
        
        for img_ in serie_et0_:
            pass
            
        
        