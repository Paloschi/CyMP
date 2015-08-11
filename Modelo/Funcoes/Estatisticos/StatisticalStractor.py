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
progress = gdal.TermProgress_nocb


class SpectreStatisticalStractor(AbstractFunction):
    '''
    Essa função extrai estatisticas do perfil temporal de cada pixel gerando uma imagem separada pra cada pixel
    
    '''

    def __setParamIN__(self):
        self.descriptionIN["images"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens para procurar as datas"}
        self.descriptionIN["null_value"] = {"Required":False, "Type":None, "Description":"valor nulo a ser ignorado"}
        self.descriptionIN["statistics"] = {"Required":True, "Type":None, "Description":"lista de estatisticas a serem feitas, nesta versão são suportados: Media (media), Coeficiente de variação (cv) e desvio padrão (sd)"}
     
    def __setParamOUT__(self):
        self.descriptionOUT["imagens de saida"] = "imagens com as estatisticas" 
        
    def __execOperation__(self):
        
        print("executando operação")
        
        images_super = self.paramentrosIN_carregados["images"]
        print("Numero de imagens para ler: " + str(len(images_super)))
        nullValue = self.paramentrosIN_carregados["null_value"]
        statistics = self.paramentrosIN_carregados["statistics"]
        
        doMedia = "media" in statistics 
        doCV = "cv" in statistics
        doSD = "sd" in statistics
        doSoma = "soma" in statistics
        doMin = "min" in statistics
        doMax = "max" in statistics
        doMediana = "mediana" in statistics
        doAmplitude = "amplitude" in statistics
        
        images = images_super.loadListRasterData()
        
        print("Numero de imagens lidas: " + str(len(images)))

        n_linhas = len(images[0])
        n_colunas = len(images[0][0])
        
        print("numero de colunas e linhas: " + str(n_linhas) + " : " + str(n_colunas))
        
        #imagem_referencia = [[0 for x in range(n_colunas)] for x in range(n_linhas)]  
        imagem_referencia = np.zeros((n_linhas, n_colunas))
        
        print(imagem_referencia)
        
        if doMedia : imagem_media = array(imagem_referencia)#.astype(dtype="int16")
        if doCV : imagem_cv = array(imagem_referencia)#.astype(dtype="int16")
        if doSD : imagem_sd = array(imagem_referencia)#.astype(dtype="int16")
        if doSoma : imagem_soma = array(imagem_referencia)#.astype(dtype="int16")
        if doMin : imagem_min = array(imagem_referencia)#.astype(dtype="int16")
        if doMax : imagem_max = array(imagem_referencia)#.astype(dtype="int16")
        if doMediana : imagem_mediana = array(imagem_referencia)#.astype(dtype="int16")
        if doAmplitude : imagem_amplitude = array(imagem_referencia)#.astype(dtype="int16")

        print("processando:")
        
        
        progress( 0.0)
        
        for i_linha in range(0, n_linhas):
            
            #status = i_linha+1/float(n_linhas)
            progress(float(i_linha/float(n_linhas)))
            #self.progresso = status*100

            for i_coluna in range(0, n_colunas):
                line = list()

                if nullValue != None and float(nullValue) == images[1][i_linha][i_coluna] :
                    pass
                    
                else:              
                    for img in images:
                        line.append(img[i_linha][i_coluna])
                    
                    mean = None
                    if doMedia : 
                        mean = np.mean(line) # calcula a média
                        imagem_media[i_linha][i_coluna] = mean
                    
                    sd = None
                    if doSD : 
                        sd = np.nanstd(line) # calcula o desvio padrão
                        imagem_sd[i_linha][i_coluna] = sd
                        
                    if doCV : 
                        if mean == None : mean = np.mean(line)
                        if sd == None : sd = np.nanstd(line) 
                        cv = sd / mean * 100 
                        imagem_cv[i_linha][i_coluna] = cv
                        
                    if doSoma : 
                        soma = np.sum(line)
                        imagem_soma[i_linha][i_coluna] = soma
                    
                    min = None 
                    if doMin : 
                        min = np.min(line)
                        imagem_min[i_linha][i_coluna] = min
                    
                    max = None
                    if doMax : 
                        max = np.max(line)
                        imagem_max[i_linha][i_coluna] = max
                    
                    if doMediana :
                        mediana = np.median(line)
                        imagem_mediana[i_linha][i_coluna] = mediana
                    
                    if doAmplitude :
                        if min == None : min = np.min(line)
                        if max == None : max = np.max(line)
                        amplitude = max - min
                        imagem_amplitude[i_linha][i_coluna] = amplitude
        
        print("Arrumando imagens de saida")
        
        saida = SerialFile ()
        saida.metadata = self.paramentrosIN_carregados["images"][0].metadata
        
        if doMedia: 
            imagem_media = RasterFile(data = imagem_media)
            imagem_media.metadata = saida.metadata
            imagem_media.file_name = "imagem_media"
            saida.append(imagem_media) 
        if doCV:
            imagem_cv = RasterFile(data = imagem_cv)
            imagem_cv.metadata = saida.metadata
            imagem_cv.file_name = "imagem_coeficiente_variacao"
            saida.append(imagem_cv)
        if doSD : 
            imagem_sd = RasterFile(data = imagem_sd)
            imagem_sd.metadata = saida.metadata
            imagem_sd.file_name = "imagem_desvio_padrao"
            saida.append(imagem_sd)
        if doSoma : 
            imagem_soma = RasterFile(data = imagem_soma)
            imagem_soma.metadata = saida.metadata
            imagem_soma.file_name = "imagem_soma"
            saida.append(imagem_soma)
        if doMin : 
            imagem_min = RasterFile(data = imagem_min)
            imagem_min.metadata = saida.metadata
            imagem_min.file_name = "imagem_minimo"
            saida.append(imagem_min)
        if doMax : 
            imagem_max = RasterFile(data = imagem_max)
            imagem_max.metadata = saida.metadata
            imagem_max.file_name = "imagem_maximo"
            saida.append(imagem_max)
        if doMediana : 
            imagem_mediana = RasterFile(data = imagem_mediana)
            imagem_mediana.metadata = saida.metadata
            imagem_mediana.file_name = "imagem_mediana"
            saida.append(imagem_mediana)
        if doAmplitude : 
            imagem_amplitude = RasterFile(imagem_amplitude)
            imagem_amplitude.metadata = saida.metadata
            imagem_amplitude.file_name = "imagem_amplitude"
            saida.append(imagem_amplitude)
            
        print("imagens prontas para gravar, statistical stractor completo")
        
        return saida
    
if __name__ == '__main__':   
    
    ss = SpectreStatisticalStractor()
    
    root_ = "C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\entrada\\"
    images = SerialFile(root_path  =  root_)
    images.loadListByRoot(filtro = "tif")
    
    parametrosIN = TableData()
    
    parametrosIN["images"] = images
    parametrosIN["null_value"] = 0
    
    statistics = list()
    statistics.append("media")
    
    parametrosIN["statistics"] = statistics

    ss.data = parametrosIN
    resultados = ss.data
    
    imagens = resultados
    #cv = resultados["imagem_cv"]
    #sd = resultados["imagem_sd"]
    
    #imagens_lista = Dados.SerialData()

    #imagens_lista.append(cv)
    
    #print (media)
    #print (media.data)
    
    
    #imagens_lista.data_metadata = media.data_metadata
    
    #imagens_lista.saveListLike1Image(imagens_lista, "C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")
    
    imagens.saveListByRoot (root_path="C:\\Users\\Paloschi\\Desktop\\data\\Testes\\saida", ext="tif")
    #cv.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")
    #sd.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")

    



