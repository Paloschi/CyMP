# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: Paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA, TABLE_DATA, FILE_DATA, SerialFiles
from datetime import datetime
import datetime
import numpy as np

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
        self.descriptionIN["Kc"] = {"Required":True, "Type":TABLE_DATA, "Description":"Valores tabelados de Kc. Ex.: '1-2':1.2,'2-6:0.8..'"}
        self.descriptionIN["semeadura"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de semeadura"}
        self.descriptionIN["colheira"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de colheita"}  
        self.descriptionIN["noData"] = {"Required":None, "Type":None, "Description":"Valor a ser ignorado (verificado na da data de semeadura)"}
        self.descriptionIN["mask_et0"] = {"Required":True, "Type":None, "Description":"mascara para conversão em data"}
        self.descriptionIN["pref_etc"] = {"Required":True, "Type":None, "Description":"prefixo do etc"}
        self.descriptionIN["sufix_etc"] = {"Required":True, "Type":None, "Description":"sufixo do etc"}
    
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
        kc_tabelado = self.paramentrosIN_carregados["Kc"]
        FKc = self.kc_TabletoVector(kc_tabelado)
        pf = len(FKc)
        
        
        n_imagens = len(serie_et0_)
        n_linhas = len(serie_et0_[0])
        n_colunas = len(serie_et0_[0][0])
        
        serie_etc_ = np.zeros((n_imagens, n_linhas, n_colunas,))
        
        for i_linha in range(0, n_linhas):
            for i_coluna in range(0, n_colunas):
                Ds = self.to_date(semeadura_[i_linha][i_coluna])
                Dc = self.to_date(colheita_[i_linha][i_coluna])
                delta_c = Dc - Ds
                
                for i_etc in range(0, len(serie_et0_)) :
                    j0 = self.etc_name_to_date(serie_et0_[i_etc].file_name)
                    jn = self.etc_name_to_date(serie_et0_[i_etc+1].file_name)
                    
                    ET0 = serie_et0_[i_etc][i_linha][i_coluna]/int(jn-j0)
                    
                    ETc = 0
                    
                    for k in range(j0-Ds, jn):
                        if (0 < k and k <= delta_c):
                            i_FKc = int(k * delta_c * pf)
                            Kc = FKc[i_FKc]
                        else: Kc = 1
                        
                        ETc += ET0 * Kc
                        
                serie_etc_[i_etc][i_linha][i_coluna]
        
        serie_etc = SerialFiles(data=serie_etc_)
        
        return serie_etc
    
    def Ds_DC_to_date(self, data):
        
        n = len(str(data))
        year = int(str(data)[0:4])    
        days = int(str(data)[4:n])
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
        return date
    
    def kc_TabletoVector(self, kc_t):
        
        kc_v = list()
        for key in kc_t.keys():
            fim = int(key.split("-")[-1])
            inicio = int(key.split("-")[0])
            for dia in range(inicio, fim+1):
                kc_v.append(kc_t[key])
        return kc_v
    
    def etc_name_to_date(self, name):
        
        if self.paramentrosIN_carregados["pref_etc"]!=None : name = name.replace(self.paramentrosIN_carregados["pref_etc"],"")
        if self.paramentrosIN_carregados["sufix_etc"]!=None :name = name.replace(self.paramentrosIN_carregados["sufix_etc"],"")
        
        decend = int(name[-1])
        data = name[0:-1]
        
        # decend -1 pra começar no 0 multiplicado por 10 dias de um decend pra saber qual o dia inicial do decend
        dias = datetime.timedelta(((decend - 1) * 10)) 
        ano_mes = datetime.datetime.strptime(data, '%Y%m') 
        date_object = ano_mes + dias
        
        return date_object
        