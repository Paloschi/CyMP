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
from multiprocessing import Pool
import multiprocessing as mp

progress = gdal.TermProgress_nocb

# Define an output queue
output = mp.Queue()

def processa_linha (linha_img, do, i_linha, output):
    output.put(i_linha)
    #return i_linha
    

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
        
        
        ''' -------------------- Parametros iniciais ---------------------------- '''
        
        print("executando operação")
        images_super = self.paramentrosIN_carregados["images"]
        print("Numero de imagens para ler: " + str(len(images_super)))
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
                
        numero_de_nucleos = GeneralTools.available_cpu_count()
        n_threadings = int(numero_de_nucleos-2)
        print ("Numero de threads", n_threadings)
        
        ''' ------------------- Descrição das imagens ----------------------- '''
        
        imagem_referencia = images[0].loadRasterData()
        n_imagens = len(images)
        n_linhas = len(imagem_referencia)
        n_colunas = len(imagem_referencia[0])
        
        ''' --------------------------------------------------------'''
        
        for i_linhas in range(0, n_linhas):       
            linhas = list()      
            for i_thread in range (0, n_threadings) :
                pool = Pool(processes=n_threadings)
                linha = list()
                for img in images : linha.append(img.loadRasterData()[i_thread + i_linhas][:])
                linhas.append(linha)
                
            print len(linhas)
            
            processes = [mp.Process(target=processa_linha, args=(linhas[x], do, i_linhas + x, output)) for x in range(n_threadings)]
            
            # Run processes
            for p in processes:
                p.start()
            # Exit the completed processes
            for p in processes:
                p.join()
                
            results = [output.get() for p in processes]
            
            print(results)
                
            i_linhas+=n_threadings
            
        
        
    
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

    



