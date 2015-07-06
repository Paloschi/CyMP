# -*- coding: utf-8 -*-
'''
Created on Apr 8, 2015

@author: Paloschi
'''

from beans import Dados                                  
from numpy.core.numeric import array
import numpy as np
import gdal
from Operations import OperationInterface
from matplotlib.axis import Axis
progress = gdal.TermProgress_nocb   
import scipy 

class SpectreStatisticalStractor(OperationInterface.Operation):
    '''
    Essa função extrai estatisticas do perfil temporal de cada pixel gerando uma imagem separada pra cada pixel
    
    '''

    def __setParamIN__(self):
        self.descriptionIN["images"] = "Série de imagens para procurar as datas"
        self.descriptionIN["null_value"] = "valor nulo a ser ignorado"
        self.descriptionIN["statistics"] = "lista de estatisticas a serem feitas, nesta versão são suportados: Media (media), Coeficiente de variação (cv) e desvio padrão (sd)"
     
    def __setParamOUT__(self):
        self.descriptionOUT["imagens de saida"] = "imagens com as estatisticas" 
        
    def __execOperation__(self):
        
        print("executando operação")
        
        images_super = self.brutedata["images"]
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
        doModa = "moda" in statistics
        
        images = images_super.loadData()
        
        
        print("Numero de imagens lidas: " + str(len(images)))

        n_linhas = len(images[0])
        n_colunas = len(images[0][0])
        
        print("numero de colunas e linhas: " + str(n_linhas) + " : " + str(n_colunas))
        
        imagem_referencia = [[0 for x in range(n_colunas)] for x in range(n_linhas)]  
        
        if doMedia : imagem_media = array(imagem_referencia)#.astype(dtype="int16")
        if doCV : imagem_cv = array(imagem_referencia)#.astype(dtype="int16")
        if doSD : imagem_sd = array(imagem_referencia)#.astype(dtype="int16")
        if doSoma : imagem_soma = array(imagem_referencia)#.astype(dtype="int16")
        if doMin : imagem_min = array(imagem_referencia)#.astype(dtype="int16")
        if doMax : imagem_max = array(imagem_referencia)#.astype(dtype="int16")
        if doMediana : imagem_mediana = array(imagem_referencia)#.astype(dtype="int16")
        if doModa : imagem_moda = array(imagem_referencia)#.astype(dtype="int16")

        progress( 0.0)
        
        for i_linha in range(0, n_linhas):
            
            status = i_linha+1/float(n_linhas)
            progress(status)
            self.progresso = status*100

            for i_coluna in range(0, n_colunas):
                line = list()

                if nullValue != None and float(nullValue) == images[1][i_linha][i_coluna] :
                    pass
                    
                else:              
                    for img in images:
                        line.append(img[i_linha][i_coluna])
                    
                    if doMedia : 
                        mean = np.mean(line) # calcula a média
                        imagem_media[i_linha][i_coluna] = mean
                        
                    if doSD : 
                        sd = np.nanstd(line) # calcula o desvio padrão
                        imagem_sd[i_linha][i_coluna] = sd
                        
                    if doCV : 
                        if sd != None : cv = sd / mean * 100 # calcula o coeficiente de variação
                        else : cv = np.nanstd(line) / mean * 100
                        imagem_cv[i_linha][i_coluna] = cv
                        
                    if doSoma : 
                        soma = np.sum(line)
                        imagem_soma[i_linha][i_coluna] = soma
                        
                    if doMin : 
                        min = np.min(line)
                        imagem_min[i_linha][i_coluna] = min
                    
                    if doMax : 
                        max = np.max(line)
                        imagem_max[i_linha][i_coluna] = max
                    
                    if doMediana :
                        mediana = np.median(line)
                        imagem_mediana[i_linha][i_coluna] = mediana
                    
                    #if doModa :
                        #moda = line.mode()[0] # não habilitado
                                  
        saida = Dados.SerialData()
        saida.data_metadata = self.brutedata["images"][0].data_metadata
        
        if doMedia: 
            imagem_media = Dados.SimpleData( data = imagem_media)
            imagem_media.data_name = "imagem_media"
            saida.append(imagem_media) 
        if doCV:
            imagem_cv = Dados.SimpleData( data = imagem_cv)
            imagem_cv.data_name = "imagem_coeficiente_variacao"
            saida.append(imagem_cv)
        if doSD : 
            imagem_sd = Dados.SimpleData( data = imagem_sd)
            imagem_sd.data_name = "imagem_desvio_padrao"
            saida.append(imagem_sd)
        if doSoma : 
            imagem_soma = Dados.SimpleData( data = imagem_soma)
            imagem_soma.data_name = "imagem_soma"
            saida.append(imagem_soma)
        if doMin : 
            imagem_min = Dados.SimpleData( data = imagem_min)
            imagem_min.data_name = "imagem_minimo"
            saida.append(imagem_min)
        if doMax : 
            imagem_max = Dados.SimpleData( data = imagem_max)
            imagem_max.data_name = "imagem_maximo"
            saida.append(imagem_max)
        if doMediana : 
            imagem_mediana = Dados.SimpleData( data = imagem_mediana)
            imagem_mediana.data_name = "imagem_mediana"
            saida.append(imagem_mediana)
            
        return saida
    
if __name__ == '__main__':   
    ss = SpectreStatisticalStractor()
    
    root_ = "C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\entrada\\"
    images = Dados.SerialData()
    
    images.loadListByRoot(root_, "tif")
    
    parametrosIN = Dados.TableData()
    
    parametrosIN["images"] = images
    parametrosIN["null_value"] = Dados.SimpleData(data=0) 
    
    statistics = list()
    statistics.append("media")
    parametrosIN["statistics"] = Dados.SerialData(data = statistics)

    ss.data = parametrosIN
    resultados = ss.data
    
    media = resultados["imagem_media"]
    #cv = resultados["imagem_cv"]
    #sd = resultados["imagem_sd"]
    
    #imagens_lista = Dados.SerialData()
    #imagens_lista.append(media)
    #imagens_lista.append(cv)
    
    #print (media)
    #print (media.data)
    
    
    #imagens_lista.data_metadata = media.data_metadata
    
    #imagens_lista.saveListLike1Image(imagens_lista, "C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")
    
    media.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext="vermelho.tif")
    #cv.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")
    #sd.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")

    



