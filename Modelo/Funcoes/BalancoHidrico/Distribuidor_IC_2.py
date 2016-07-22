# -*- coding: utf-8 -*-
'''
Created on Sep 10, 2015

@author: rennan.paloschi
'''

import warnings
warnings.filterwarnings('ignore')

from Modelo.Funcoes import AbstractFunction
from Modelo.beans import TABLE_DATA, FILE_DATA, RasterFile
import datetime
import numpy as np
import gdal
from Modelo.beans.SerialFileData import SerialFile
from Modelo.GeneralTools import available_cpu_count
progress = gdal.TermProgress_nocb   
from multiprocessing import Process
import threading
import time

def distribuir_kc(dia, semeadura_, colheita_, ano_inicio, dia_inicio, periodo_kc, kc_vetorizado, path_img_referencia, path_out):
    
        threading.currentThread().terminada = False
        imagem_kc = RasterFile(file_full_path = path_img_referencia)
        imagem_kc.loadRasterData()
        imagem_kc.file_path = path_out

        n_linhas = len(semeadura_)
        n_colunas = len(semeadura_[0])
        
        delta_c = colheita_ - semeadura_

        tempo_em_campo = dia - semeadura_
            
        i_FKc = np.zeros((n_linhas, n_colunas)).astype(dtype="uint8")
                        
        for i in range(n_linhas) :
            mask = ((tempo_em_campo[i] > 0) & (tempo_em_campo[i] < delta_c[i]))
            i_FKc[i][mask] = (tempo_em_campo[i][mask] * (periodo_kc-1))/delta_c[i][mask]
            i_FKc[i][mask] +=1
        

                       
        for i in range(n_linhas) :
            i_FKc[i] = [kc_vetorizado[int(index)] for index in i_FKc[i]]

        imagem_kc.file_name = str(datetime.datetime(ano_inicio, 1, 1) + datetime.timedelta(dia + dia_inicio - 1))[:10]
        imagem_kc.metadata.update(nodata=0)
        imagem_kc.saveRasterData(band_matrix = i_FKc)
            
        print "retornando do processo", dia

        threading.currentThread().terminada = True
                
        return


class DistribuidorKC_(AbstractFunction):
    
    ''' Essa classe pega o KC tabelado e transforma em um cubo temporal de kc pra cada cultura dependendo da data de colheita e semeadura '''
    
    def __setParamIN__(self):
        self.descriptionIN["Kc"] = {"Required":True, "Type":TABLE_DATA, "Description":"Dados Kc tabelado"}
        self.descriptionIN["semeadura"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de semeadura"}
        self.descriptionIN["colheita"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de colheita"} 
        self.descriptionIN["path_out"] = {"Required":True, "Type":None, "Description":"Caminho de saida das imagens"}   
        self.descriptionIN["multply_factor"] = {"Required":False, "Type":None, "Description":"Fator multiplicador pelo indice"}   
        
    def __setParamOUT__(self):
        self.descriptionOUT["images"] = "Série de imagens kc distribuidas de acordo com as imagens de semeadura e  colheita" 
            
    def __execOperation__(self):
        
        #self.console(u"Iniciando distribuidor")
        
        try:
            semeadura_ = self.paramentrosIN_carregados["semeadura"].loadRasterData()
            colheita_ = self.paramentrosIN_carregados["colheita"].loadRasterData()
        except: 
            print "não foi possivel carregar as imagens de semeadura e colheita"
            return None
        try:
            data_minima = self.Ds_DC_to_date(np.min(semeadura_))
            data_maxima = self.Ds_DC_to_date(np.max(colheita_))          
    
        except:
            print u"não foi possivel converter os valores das imagens de semeadura e colheita em datas"
            return None     
        
        semeadura_, colheita_, primeiro_ano, primeiro_dia = self.normalize_datas(semeadura_, colheita_)
        
        

        kc_vetorizado = self.vetorizar_kc()
        periodo_kc = len(kc_vetorizado)
        
        delta_total = (data_maxima-data_minima).days
        
        self.console(u"Numero de dias da primeira DS à ultima DC: " +  str(delta_total))
        self.console(u"Numero de processadores identificados: " +  str(available_cpu_count()))

        if (available_cpu_count()>4):
            n_of_process = available_cpu_count() - 2
        elif (available_cpu_count()>1) :
            n_of_process = available_cpu_count() - 1
        else :
            n_of_process = 1
        
        self.console(u"Numero de processadores utilizados: "+  str(n_of_process))

        processos = list()
        
        path_img_semeadura = self.paramentrosIN_carregados["semeadura"].file_full_path
        
        processadores_disponiveis = n_of_process
        
        self.console("Processando...")
        
        for dia in range (0, delta_total):
            
            if threading.currentThread().stopped()  : return 
        
            p = Process(target=distribuir_kc, args=(dia,      
                                                        semeadura_, colheita_,
                                                        primeiro_ano, primeiro_dia,
                                                        periodo_kc, kc_vetorizado, path_img_semeadura, 
                                                        self.paramentrosIN_carregados["path_out"]))
            p.daemon = True
            processos.append(p)
            p.start()
            
            processadores_disponiveis -=1
                    
            while (processadores_disponiveis == 0): 
                for p in processos:
                    if not p.is_alive(): 
                        processadores_disponiveis += 1
                        processos.remove(p)
                time.sleep(0.5)
            
            self.setProgresso(dia, delta_total)
            
        print "Acabou, retornando ----------------------------------------------------"
        
        return SerialFile(root_path = self.paramentrosIN_carregados["path_out"])
                
    def vetorizar_kc(self): 
        
        if self.paramentrosIN_carregados.has_key("multply_factor") :
            multply_factor = self.paramentrosIN_carregados["multply_factor"]
        else :
            multply_factor = 1
        
        if multply_factor is None :  multply_factor = 1
        tamanho = 0
        for key in self.paramentrosIN_carregados["Kc"].keys():
            fim = int(key.split("-")[1])
            if fim > tamanho : tamanho = fim
        
        kc_vetorizado = np.zeros(tamanho+1)
        
        for key in self.paramentrosIN_carregados["Kc"].keys():
            inicio = int(key.split("-")[0])
            fim = int(key.split("-")[1])
            for x in range(inicio, fim+1):
                kc_vetorizado[x] = self.paramentrosIN_carregados["Kc"][key] * multply_factor
                
        kc_vetorizado[0] = 0
        return kc_vetorizado
        
    def normalize_datas(self, semeadura, colheita):
        
        ano_semeadura = semeadura.astype(int)/1000
        dia_semeadura = semeadura - ano_semeadura * 1000
        
        ano_colheita = colheita.astype(int)/1000
        dia_colheita = colheita - ano_colheita * 1000
        
        primeira_data = np.min(semeadura)
        primeiro_ano = primeira_data/1000
        primeiro_dia = primeira_data - primeiro_ano * 1000
        
        dias_no_ano = self.dias_ano(primeiro_ano)
        
        semeadura_normalizada = (ano_semeadura - primeiro_ano - 1) * (primeiro_dia - dia_semeadura)  + (ano_semeadura - primeiro_ano) * dia_semeadura + (ano_semeadura - primeiro_ano) * (dias_no_ano - primeiro_dia) 
        colheita_normalizada = ((ano_colheita - primeiro_ano) - 1) * (primeiro_dia - dia_colheita)  + (ano_colheita - primeiro_ano) * dia_colheita + (ano_colheita - primeiro_ano) * (365 - primeiro_dia)
        
        return semeadura_normalizada, colheita_normalizada, primeiro_ano, primeiro_dia
    
    def dias_ano(self, ano):
        if ano%4==0:
            if ano%100==0:
                if ano%400==0:
                    return 366
                else:
                    return 365
            else:
                return 366
        else:
            return False
        
    def Ds_DC_to_date(self, data):
        n = len(str(data))
        year = int(str(data)[0:4])    
        days = int(str(data)[4:n])
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
        return date
    
if __name__ == '__main__':   
    
    from Modelo.beans import TableData
    
    import ctypes
    
    myappid = ("NTX.Gafanhoto.Distibuidorkc.0.1")
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    paramIN = dict()
    paramIN["semeadura"] = RasterFile(file_full_path="C://Users//Paloschi//Desktop//2013-2014//semeadura.tif")
    paramIN["colheita"] = RasterFile(file_full_path="C://Users//Paloschi//Desktop//2013-2014//colheita.tif")
    paramIN["path_out"] = "C://Users//Paloschi//Desktop//saida_teste"
    paramIN["Kc"] = TableData()
    paramIN["Kc"]["0-10"]=40
    paramIN["Kc"]["10-50"]=80
    paramIN["Kc"]["50-85"]=115
    paramIN["Kc"]["85-125"]=80
    paramIN["Kc"]["125-140"]=50
    #paramIN["Kc"]["0-10"]=10
    #paramIN["Kc"]["10-50"]=25
    #paramIN["Kc"]["50-85"]=60
    #paramIN["Kc"]["85-125"]=60
    #paramIN["Kc"]["125-140"]=60
    
    print "chamando funcao"
    
    funcao = DistribuidorKC_()
    
    #funcao.console = console
    
    Kc_distribuido = funcao.executar(paramIN)
    


    
    
    #print Kc_distribuido[0]

