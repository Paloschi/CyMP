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
import gdal
from Modelo.beans.SerialFileData import SerialFile
progress = gdal.TermProgress_nocb   
from multiprocessing import Process, Queue
import time
import threading

def Ds_DC_to_date(data):
        
        n = len(str(data))
        year = int(str(data)[0:4])    
        days = int(str(data)[4:n])
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
        return date

def distribuir_kc(data_minima, data_maxima, semeadura_, colheita_, periodo_kc, kc_vetorizado, path_img_referencia, i, path_out, function):
    
        imagem_kc = RasterFile(file_full_path = path_img_referencia)
        imagem_kc.loadRasterData()
        imagem_kc.file_path = path_out
        
        #print imagem_kc.metadata
        
        n_linhas = len(semeadura_)
        n_colunas = len(colheita_[0])
        
        delta_total = (data_maxima-data_minima).days+1

        for i_dia in range (0, delta_total):

            imagem_kc_ = np.zeros((n_linhas, n_colunas))
            imagem_kc_ = array(imagem_kc_).astype(dtype="uint8")
       
            dia = data_minima + timedelta(i_dia)
            
            imagem_kc.data = array(semeadura_)
            imagem_kc.file_name = str(dia.date())
            
            if delta_total > 1 : 
                progress(i_dia/float(delta_total-1))
                function.progresso = (i_dia/float(delta_total))*100
                    
            for i_linha in range(0, n_linhas):
                for i_coluna in range(0, n_colunas):
                    delta_c = None
                    Ds = None
                     
                    try:
                        Ds = Ds_DC_to_date(semeadura_[i_linha][i_coluna])
                        Dc = Ds_DC_to_date(colheita_[i_linha][i_coluna])
                        delta_c = (Dc - Ds).days + 1
                    except :
                        pass                      
                    if Ds != None:
                        if(dia >= Ds and dia <= Dc):
                            k = dia - Ds
                            i_FKc = int( (k * periodo_kc).days / delta_c)
                            Kc = kc_vetorizado[i_FKc]
                            imagem_kc_[i_linha][i_coluna] = Kc
                    
            imagem_kc.metadata.update(nodata=0)
            imagem_kc.saveRasterData(band_matrix = imagem_kc_)
        print "returnando do processo", i
        threading.currentThread().stopped = True
        return None


class DistribuidorKC(AbstractFunction):
    
    ''' Essa classe pega o KC tabelado e transforma em um cubo temporal de kc pra cada cultura dependendo da data de colheita e semeadura '''
    
    def __setParamIN__(self):
        self.descriptionIN["Kc"] = {"Required":True, "Type":TABLE_DATA, "Description":"Dados Kc tabelado"}
        self.descriptionIN["semeadura"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de semeadura"}
        self.descriptionIN["colheita"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de colheita"} 
        self.descriptionIN["path_out"] = {"Required":True, "Type":None, "Description":"Caminho de saida das imagens"}   
        self.descriptionIN["multply_factor"] = {"Required":True, "Type":None, "Description":"Fator multiplicador pelo indice"}   
        
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
            data_minima = self.Ds_DC_to_date(np.min(semeadura_))
            #data_minima = self.Ds_DC_to_date("2013240")
            data_maxima = self.Ds_DC_to_date(np.max(colheita_))
            #data_maxima = self.Ds_DC_to_date("201499")
        except:
            print "não foi possivel converter os valores das imagens de semeadura e colheita em datas"
            return None
        

        #data_minima = datetime.datetime(2012, 04, 19)
        print data_minima        
        #data_maxima = datetime.datetime(2012, 04, 19)

        print data_maxima
        
        kc_vetorizado = self.vetorizar_kc()
        periodo_kc = len(kc_vetorizado)
        
        delta_total = (data_maxima-data_minima).days
        
        print data_maxima
        
        print "total de dias", delta_total
        
        metadata = self.paramentrosIN_carregados["semeadura"].metadata
        
        print metadata
        
        n_of_process = 5

        processos = list()
        
        for i in range (0, n_of_process):
            
            path_img_semeadura = self.paramentrosIN_carregados["semeadura"].file_full_path
        
            q = Queue()
            if i == 0 : data_minima_process = data_minima
            else : 
                dt = data_minima + timedelta(float(i)*int(float(delta_total)/float(n_of_process)))
                data_minima_process =  dt
                print data_minima_process
                print data_minima_process.date()
            #data_minima_process = datetime.datetime(2012, 04, 13)
            
            if i == n_of_process-1 : data_maxima_process = data_maxima
            else : 
                dt = data_minima + timedelta(((i+1)*int(float(delta_total)/float(n_of_process)))-1)
                data_maxima_process =  dt
            #data_maxima_process = datetime.datetime(2012, 04, 19)
            
            print data_minima_process, data_maxima_process
            
            p = Process(target=distribuir_kc, args=(data_minima_process, 
                                                     data_maxima_process, 
                                                     semeadura_, colheita_, periodo_kc, kc_vetorizado, path_img_semeadura, 
                                                     i, self.paramentrosIN_carregados["path_out"], self))
            processos.append(p)
            p.start()
            
            
            
            
        print "vai aguardar processos --------------------------------------------------"
        
        numero_de_processos_prontos = 0        
        processos_prontos = False
        while numero_de_processos_prontos < n_of_process:
            processos_prontos = 0
            for p in processos:
                if p.is_alive() :
                    numero_de_processos_prontos +=1
                    print "mais um processo terminado -------------------------------------"
                
        #for i in range (0, n_of_process):
            #q.join_thread()
            print "pricesso", i, "retornado -------------------------------------------"
        
        print "Acabou, retornando ----------------------------------------------------"
        
        return SerialFile(root_path = self.paramentrosIN_carregados["path_out"])
                
    def vetorizar_kc(self): 
        
        if self.paramentrosIN_carregados.has_key("multply_factor") :
            multply_factor = self.paramentrosIN_carregados["multply_factor"]
        else :
            multply_factor = 1
        
        tamanho = 0
        for key in self.paramentrosIN_carregados["Kc"].keys():
            fim = int(key.split("-")[1])
            if fim > tamanho : tamanho = fim
        
        kc_vetorizado = np.zeros(tamanho)
        
        print len(kc_vetorizado)
        
        for key in self.paramentrosIN_carregados["Kc"].keys():
            inicio = int(key.split("-")[0])
            fim = int(key.split("-")[1])
            print "chave:", key, "- inicio:", inicio, "- fim:", fim, "- tamanho:", fim - inicio
            for x in range(inicio, fim+1):
                kc_vetorizado[x-1] = self.paramentrosIN_carregados["Kc"][key] * multply_factor
                
        print kc_vetorizado
        print len(kc_vetorizado)
        return kc_vetorizado
    
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
    paramIN["semeadura"] = RasterFile(file_full_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Datas_DS-DC\\semeadura_soja_11-12.tif")
    paramIN["colheita"] = RasterFile(file_full_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Datas_DS-DC\\colheita_soja_11-12.tif")
    paramIN["path_out"] = "E:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\Kc_distribuido"
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
    
 
    
    Kc_distribuido = DistribuidorKC().executar(paramIN)
    
    #print Kc_distribuido[0]
    
    