# -*- coding: utf-8 -*-
'''
Created on Apr 8, 2015

@author: Paloschi
'''
                                  
from numpy.core.numeric import array
import numpy as np
from Modelo.beans import SerialFile, TableData, SERIAL_FILE_DATA, RasterFile
from Modelo.Funcoes import AbstractFunction
import gdal
from Modelo import GeneralTools
import images

progress = gdal.TermProgress_nocb
import Modelo.GeneralTools
import multiprocessing
import threading
from multiprocessing import Pool
from multiprocessing import Process
    

def processa_linha (linha_img, do):
        
        tamanho = len(linha)   
        status = float(i_linha)

        for i_coluna in range(0, n_colunas):
            line = list()

            if nullValue != None and float(nullValue) == images[1][i_linha][i_coluna] :
                pass
                    
            else:              
                for img in images:
                    
                    line.append(img[0][i_coluna])
                    
                    mean = None
                    if do["Media"] : 
                        mean = np.mean(line) # calcula a média
                        imagem_media[i_linha][i_coluna] = mean
                    sd = None
                    if do["SD"] : 
                        sd = np.nanstd(line) # calcula o desvio padrão
                        imagem_sd[i_linha][i_coluna] = sd
                    if do["CV"] : 
                        if mean == None : mean = np.mean(line)
                        if sd == None : sd = np.nanstd(line) 
                        divisor = mean * 100
                        if divisor != 0 : cv = sd / mean * 100 
                        else : cv = 0
                        imagem_cv[i_linha][i_coluna] = cv
                    if do["Soma"] : 
                        soma = np.sum(line)
                        imagem_soma[i_linha][i_coluna] = soma
                    min = None 
                    if do["Min"] : 
                        min = np.min(line)
                        imagem_min[i_linha][i_coluna] = min
                    max = None
                    if do["Max"] : 
                        max = np.max(line)
                        imagem_max[i_linha][i_coluna] = max
                    if do["Mediana"] :
                        mediana = np.median(line)
                        imagem_mediana[i_linha][i_coluna] = mediana
                    if do["Amplitude"] :
                        if min == None : min = np.min(line)
                        if max == None : max = np.max(line)
                        amplitude = max - min
                        imagem_amplitude[i_linha][i_coluna] = amplitude
        
        threads_ready +=1
        
        print ("Tread Pronta", threads_ready)

class SpectreStatisticalStractor_MT(AbstractFunction):
    '''
    Essa função extrai estatisticas do perfil temporal de cada pixel gerando uma imagem separada pra cada pixel
    
    '''

    def __setParamIN__(self):
        self.descriptionIN["images"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens para procurar as datas"}
        self.descriptionIN["statistics"] = {"Required":True, "Type":None, "Description":"lista de estatisticas a serem feitas, nesta versão são suportados: Media (media), Coeficiente de variação (cv) e desvio padrão (sd)"}
     
    def __setParamOUT__(self):
        self.descriptionOUT["imagens de saida"] = "imagens com as estatisticas" 
        
    def __execOperation__(self):
        
        global nullValue, imagem_media, imagem_sd, imagem_cv, imagem_soma, imagem_min, imagem_max
        global imagem_mediana, imagem_amplitude, images, n_linhas, n_colunas, threads_ready, n_threadings
        
        print("executando operação")
        
        images_super = self.paramentrosIN_carregados["images"]
        print("Numero de imagens para ler: " + str(len(images_super)))
        nullValue = np.double(images_super[0].getRasterInformation()["NoData"])
        statistics = self.paramentrosIN_carregados["statistics"]
        
        print("Estatisticas a fazer: ", statistics)
        
        do = dict()
        
        do["Media"] = "media" in statistics 
        do["CV"] = "cv" in statistics
        do["SD"] = "sd" in statistics
        do["Soma"] = "soma" in statistics
        do["Min"] = "min" in statistics
        do["Max"] = "max" in statistics
        do["Mediana"] = "mediana" in statistics
        do["Amplitude"] = "amplitude" in statistics
        
        images = images_super.loadListRasterData()
        
        print("Numero de imagens lidas: " + str(len(images)))
        
        n_linhas = len(images[0])
        n_colunas = len(images[0][0])
        
        for img in images:
            if len(img) != n_linhas or len(img[0]) != n_colunas:
                raise IndexError("Erro - As imagens precisam ter o mesmo número de linhas e colunas")
                   
        print("numero de colunas e linhas: " + str(n_linhas) + " : " + str(n_colunas))
        
        #imagem_referencia = [[0 for x in range(n_colunas)] for x in range(n_linhas)]  
        imagem_referencia = np.zeros((n_linhas, n_colunas))
        
        imagem_out = dict
        
        if do["Media"] : imagem_out["media"] = array(imagem_referencia)#.astype(dtype="int16")
        if do["CV"] : imagem_out["cv"] = array(imagem_referencia)#.astype(dtype="int16")
        if do["SD"] : imagem_out["sd"] = array(imagem_referencia)#.astype(dtype="int16")
        if do["Soma"] : imagem_out["soma"] = array(imagem_referencia)#.astype(dtype="int16")
        if do["Min"] : imagem_out["min"] = array(imagem_referencia)#.astype(dtype="int16")
        if do["Max"] : imagem_out["max"] = array(imagem_referencia)#.astype(dtype="int16")
        if do["Mediana"] : imagem_out["mediana"] = array(imagem_referencia)#.astype(dtype="int16")
        if do["Amplitude"] : imagem_out["amplitude"] = array(imagem_referencia)#.astype(dtype="int16")

        print("processando:") 
        
        numero_de_nucleos = GeneralTools.available_cpu_count()
        n_threadings = int(numero_de_nucleos-2)
        print ("Numero de threads", n_threadings)
        threads_ready = 0
        
        pool = Pool()
        #pool = multiprocessing.Pool(processes=n_threadings)

        for i in range(0, n_threadings):
            #t = threading.Thread(target=thread_process, args=(n_linhas/n_threadings*i, n_linhas/n_threadings*(i+1)))
            #t.start()
            linha_inicial = n_linhas/n_threadings*i
            linha_final = n_linhas/n_threadings*(i+1)
            p = Process(target= thread_process, args=(linha_inicial, linha_final))
            p.start()
            
            #pool.map(thread_process(n_linhas/n_threadings*i, n_linhas/n_threadings*(i+1)))
            #pool.close()
           
        
                    
        
        while (threads_ready < n_threadings):
            pass
       
        print("Arrumando imagens de saida")
        
        saida = SerialFile ()
        saida.metadata = self.paramentrosIN_carregados["images"][0].metadata
        
        if do["Media"]: 
            imagem_media = RasterFile(data = imagem_media)
            imagem_media.metadata = saida.metadata
            imagem_media.file_name = "imagem_media"
            saida.append(imagem_media) 
        if do["CV"]:
            imagem_cv = RasterFile(data = imagem_cv)
            imagem_cv.metadata = saida.metadata
            imagem_cv.file_name = "imagem_coeficiente_variacao"
            saida.append(imagem_cv)
        if do["SD"] : 
            imagem_sd = RasterFile(data = imagem_sd)
            imagem_sd.metadata = saida.metadata
            imagem_sd.file_name = "imagem_desvio_padrao"
            saida.append(imagem_sd)
        if do["Soma"] : 
            imagem_soma = RasterFile(data = imagem_soma)
            imagem_soma.metadata = saida.metadata
            imagem_soma.file_name = "imagem_soma"
            saida.append(imagem_soma)
        if do["Min"] : 
            imagem_min = RasterFile(data = imagem_min)
            imagem_min.metadata = saida.metadata
            imagem_min.file_name = "imagem_minimo"
            saida.append(imagem_min)
        if do["Max"] : 
            imagem_max = RasterFile(data = imagem_max)
            imagem_max.metadata = saida.metadata
            imagem_max.file_name = "imagem_maximo"
            saida.append(imagem_max)
        if do["Mediana"] : 
            imagem_mediana = RasterFile(data = imagem_mediana)
            imagem_mediana.metadata = saida.metadata
            imagem_mediana.file_name = "imagem_mediana"
            saida.append(imagem_mediana)
        if do["Amplitude"] : 
            imagem_amplitude = RasterFile(data = imagem_amplitude)
            imagem_amplitude.metadata = saida.metadata
            imagem_amplitude.file_name = "imagem_amplitude"
            saida.append(imagem_amplitude)
            
        print("imagens prontas para gravar, statistical stractor completo")

        return saida
    
if __name__ == '__main__':   
    
    ss = SpectreStatisticalStractor_MT()
    
    root_ = "C:\\Users\\rennan.paloschi\\Desktop\\Dados_Gerais\\raster\\pesada"
    images = SerialFile(root_path  =  root_)
    images.loadListByRoot(filtro = "tif")
    
    
    linha = list()
    for img in images :
        linha.append(img.loadRasterData()[0][:])
    
    print (len(linha), "----------------------------------")
    print (len(linha[0]), "----------------------------------")

    parametrosIN = TableData()
    
    parametrosIN["images"] = images
    
    statistics = list()
    statistics.append("media")
    statistics.append("cv")
    
    parametrosIN["statistics"] = statistics

    ss.data = parametrosIN
    resultados = ss.data
    
    imagens = resultados
    
    print imagens
    
    imagens.saveListByRoot (root_path="C:\\GafanhotoWorkspace", ext="tif")
    #cv.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")
    #sd.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")

    



