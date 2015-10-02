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
        self.descriptionIN["Kc"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de Kc distribuido"}
        self.descriptionIN["ETc"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Objeto série de imagens configurao para saida"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["ETc"] = {"Type":SERIAL_FILE_DATA, "Description":"Série de imagens de evapotranspiração da cultura"}
    
    def __execOperation__(self):
        '''
            Por padrão agora assumo que, quando uma variavel tiver como sufixo um underline "_"
            é porque esta variavel contem os valores carregados (matrizes brutas) dos dados
        '''
        
        print("Carregando imagens (ET0, semeadura, colheita): ")
        
        serie_ET0 = self.paramentrosIN_carregados["ET0"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_Kc = self.paramentrosIN_carregados["Kc"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_ETc = self.paramentrosIN_carregados["Kc"] # pucha lista
        
        Kc_factor = str(serie_Kc.mutiply_factor)
        ET0_factor = str(serie_Kc.mutiply_factor)
        ETC_factor = str(serie_Kc.mutiply_factor)
        
        
        
        for i_Kc in range(len(serie_Kc)):
            #gdal_calc.py [-A <filename>] [--A_band] [-B...-Z filename] [other_options]
            Kc = serie_Kc[i_Kc]
            data_kc = serie_Kc.getDate_time(file=Kc)
            
            ET0 = self.procurar_descende_correspondente(data_kc, serie_ET0)
            
            serie_ETc.append(RasterFile(file_path=serie_ETc.root_path))
            serie_ETc.setDate_time(data_kc, i_Kc)
            serie_ETc[i_Kc].ext = "tif"
            
            calculo = '(A *' + Kc_factor +') * ((B *' + ET0_factor + ") / " + str(self.dias_decend) + ") * " + ETC_factor # (A * Kc_factor) * (B * ET0_factor) / dias_decend) * ETC_factor
            
            string_execucao = [sys.executable, 'C:\\Program Files\\GDAL\\gdal_calc.py',  
                               '-A', Kc.file_full_path,
                               '-B', ET0.file_full_path, 
                               '--outfile=', serie_ETc[i_Kc].file_full_path,
                               '--calc=', calculo] 
            try:
                print ("string de execucao: ", str(string_execucao))
                subprocess.call (string_execucao) 
            
            except Exception as e:  
                print e
                print 'erro ao chamar subprocesso gdal_grid, verifiquei se a GDAL core está instalada e a variavel de ambiente está setada'
    
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
    serie_Kc.mutiply_factor = 0.001
    serie_Kc.date_mask = "%Y-%m-%d"
    
    serie_ET0 = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\6-MPMS-11-12_Comprimido\\evpt")
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
    


