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
progress = gdal.TermProgress_nocb   
from multiprocessing import Process, Queue
import time

def Ds_DC_to_date(data):
        
        n = len(str(data))
        year = int(str(data)[0:4])    
        days = int(str(data)[4:n])
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
        return date

def distribuir_kc(data_minima, data_maxima, semeadura_, colheita_, periodo_kc, kc_vetorizado, path_img_referencia, i, path_out):
    
        imagem_kc = RasterFile(file_full_path = path_img_referencia)
        imagem_kc.loadRasterData()
        imagem_kc.file_path = path_out
        
        #print imagem_kc.metadata
        
        n_linhas = len(semeadura_)
        n_colunas = len(colheita_[0])
        
        imagem_kc_ = np.zeros((n_linhas, n_colunas))
        imagem_kc_ = array(imagem_kc_).astype(dtype="uint8")
        
        delta_total = (data_maxima-data_minima).days
        
        
        
        for i_dia in range (delta_total):
            
            dia = data_minima + timedelta(i_dia)
            
            imagem_kc.data = array(semeadura_)
            imagem_kc.file_name = str(dia.date())
            
            #print imagem_kc.file_name
            
            progress(i_dia/float(delta_total))
                    
            for i_linha in range(0, n_linhas):
                ini = time.time()
                for i_coluna in range(0, n_colunas):
            
                    try:
                        #print  semeadura_[i_linha][i_coluna], colheita_[i_linha][i_coluna]
                        
                        Ds = Ds_DC_to_date(semeadura_[i_linha][i_coluna])
                        Dc = Ds_DC_to_date(colheita_[i_linha][i_coluna])
                        delta_c = (Dc - Ds).days
                        
                        #print Ds, Dc, dia
                        
                        if(dia >= Ds and dia <= Dc):
                            #print Ds, Dc, dia
                            k = dia - Ds 
                            #print k, 1
   
                            #print a, 2
                            i_FKc = int( (k * periodo_kc).days / delta_c)
                            #print i_FKc, 3
                            Kc = kc_vetorizado[i_FKc]
                            #print Kc, 4
                            imagem_kc_[i_linha][i_coluna] = Kc
                            #print imagem_kc_[i_linha][i_coluna]
                            
                        #else: 
                            #Kc = 1
                            #imagem_kc.data[i_linha][i_coluna] = Kc
                    except :
                        pass 
                        #Kc = 1
                        #imagem_kc.data[i_linha][i_coluna] = Kc
                        
                if i == 0 :
                    fim = time.time()
                    #print "Tempo restante pra 1 imagem: "
                    print (int((fim-ini) * (n_linhas - i_linha))/60)
                    
            imagem_kc.metadata.update(nodata=0)
            imagem_kc.saveRasterData(band_matrix = imagem_kc_)
        return None


class DistribuidorKC(AbstractFunction):
    
    ''' Essa classe pega o KC tabelado e transforma em um cubo temporal de kc pra cada cultura dependendo da data de colheita e semeadura '''
    
    def __setParamIN__(self):
        self.descriptionIN["Kc"] = {"Required":True, "Type":TABLE_DATA, "Description":"Dados Kc tabelado"}
        self.descriptionIN["semeadura"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de semeadura"}
        self.descriptionIN["colheita"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem de colheita"} 
        self.descriptionIN["path_out"] = {"Required":True, "Type":None, "Description":"Caminho de saida das imagens"}   
        
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
        
        kc_vetorizado = self.vetorizar_kc()
        periodo_kc = len(kc_vetorizado)
        delta_total = (data_maxima-data_minima).days
        
        print data_maxima
        
        print "total de dias", delta_total
        
        metadata = self.paramentrosIN_carregados["semeadura"].metadata
        
        print metadata
        
        n_of_process = 5
        for i in range (0, n_of_process):
            
            path_img_semeadura = self.paramentrosIN_carregados["semeadura"].file_full_path
        
            q = Queue()
            
            data_minima_process = data_minima + timedelta(i*(delta_total/n_of_process)) # Acrescenta as partes na data minima
            data_maxima_process = data_maxima - timedelta((n_of_process-1-i)*(delta_total/n_of_process)) #Retira as partes da data maxim
            
            p = Process(target=distribuir_kc, args=(data_minima_process, 
                                                     data_maxima_process, 
                                                     semeadura_, colheita_, periodo_kc, kc_vetorizado, path_img_semeadura, 
                                                     i, self.paramentrosIN_carregados["path_out"]))
            p.start()
            
        for i in range (0, n_of_process):
            q.get()
                
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
    
    import ctypes
    
    myappid = ("NTX.Gafanhoto.Distibuidorkc.0.1")
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    paramIN = dict()
    paramIN["semeadura"] = RasterFile(file_full_path="C:\\Gafanhoto WorkSpace\\Soja11_12\\Datas_DS-DC\\semeadura_soja_11-12.tif")
    paramIN["colheita"] = RasterFile(file_full_path="C:\\Gafanhoto WorkSpace\\Soja11_12\\Datas_DS-DC\\colheita_soja_11-12.tif")
    paramIN["path_out"] = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Kc_distribuido"
    paramIN["Kc"] = TableData()
    paramIN["Kc"]["1-10"]=40
    paramIN["Kc"]["10-50"]=80
    paramIN["Kc"]["50-85"]=115
    paramIN["Kc"]["85-125"]=80
    paramIN["Kc"]["125-140"]=50
    
    Kc_distribuido = DistribuidorKC().executar(paramIN)
    
    #print Kc_distribuido[0]
    
    