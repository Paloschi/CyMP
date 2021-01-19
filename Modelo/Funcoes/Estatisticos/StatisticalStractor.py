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
import threading

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
        
        self.print_text(u"Iniciando função")


        images_super = self.paramentrosIN_carregados["images"]

        n_images = len(images_super)
        self.console(u"Número de imagens para ler: " + str(n_images))
        #nullValue = self.paramentrosIN_carregados["null_value"]
        statistics = self.paramentrosIN_carregados["statistics"]
        
        #self.print_text("Estatisticas a fazer: ", statistics)
        
        doMedia = "media" in statistics 
        doCV = "cv" in statistics
        doSD = "sd" in statistics
        doSoma = "soma" in statistics
        doMin = "min" in statistics
        doMax = "max" in statistics
        doMediana = "mediana" in statistics
        doAmplitude = "amplitude" in statistics

        imagem_referencia = images_super[0].loadRasterData()
        n_linhas = len(imagem_referencia)
        n_colunas = len(imagem_referencia[0])

        self.console(u"Tamanho das imagens")
        self.console(u"Numero de linhas: " + str(n_linhas))
        self.console(u"Numero de colunas: " + str(n_colunas))

        imagem_referencia = np.zeros((n_linhas, n_colunas))


        
        if doMedia or doCV: imagem_media = array(imagem_referencia).astype(dtype="float32")
        if doCV : imagem_cv = array(imagem_referencia).astype(dtype="float32")
        if doSD or doCV : imagem_sd = array(imagem_referencia).astype(dtype="float32")
        if doSoma or doMedia or doCV : imagem_soma = array(imagem_referencia).astype(dtype="float32")
        if doMin or doAmplitude: imagem_min = array(imagem_referencia).astype(dtype="float32")
        if doMax or doAmplitude: imagem_max = array(imagem_referencia).astype(dtype="float32")
        if doMediana : imagem_mediana = array(imagem_referencia).astype(dtype="float32")
        if doAmplitude : imagem_amplitude = array(imagem_referencia).astype(dtype="float32")
        
        self.print_text(u"Processando:")
        print(doMedia)
        if (doSoma or doMedia or doCV):
            self.print_text(u"Somando Imagens:")
            for i in range(n_images-1):
                imagem_soma += images_super[i+1].loadRasterData()   
                self.setProgresso(i, n_images)
                if threading.currentThread().stopped(): return

        if doMedia:
            imagem_media = imagem_soma / n_images

        self.print_text(u"Calculando as outras estatísticas:")

        if doCV or doSD or doMin or doMax or doMediana or doAmplitude:

            self.print_text(u"Carregando imagens na memória...")
            self.setProgresso(0, 1)
            images = images_super.loadListRasterData()

            for i_linha in range(0, n_linhas):

                self.progresso = (float(i_linha/float(n_linhas)))*100
                if threading.currentThread().stopped(): return

                for i_coluna in range(0, n_colunas):
                        line = list()

                        for img in images:
                            line.append(img[i_linha][i_coluna])

                        if doSD or doCV:
                            sd = np.nanstd(line)  # calcula o desvio padrão
                            imagem_sd[i_linha][i_coluna] = sd

                        if doCV :
                            mean = imagem_media[i_linha][i_coluna]
                            divisor = mean * 100
                            if divisor != 0: cv = sd / mean * 100
                            else: cv = 0
                            imagem_cv[i_linha][i_coluna] = cv

                        if doMin or doAmplitude:
                            minimo = np.nanmin(line)
                            imagem_min[i_linha][i_coluna] = minimo

                        if doMax or doAmplitude:
                            maximo = np.nanmax(line)
                            imagem_max[i_linha][i_coluna] = maximo

                        if doMediana :
                            mediana = np.nanmedian(line)
                            imagem_mediana[i_linha][i_coluna] = mediana

                        if doAmplitude :
                            amplitude = maximo - minimo
                            imagem_amplitude[i_linha][i_coluna] = amplitude


        print(u"Arrumando imagens de saida")
        self.print_text(u"Arrumando imagens de saida")
        
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
            i=0
            i+=1
            print(i)
            imagem_soma = RasterFile(data = imagem_soma)
            i += 1
            print(i)
            imagem_soma.metadata = saida.metadata
            i += 1
            print(i)
            imagem_soma.file_name = "imagem_soma"
            i += 1
            print(i)
            saida.append(imagem_soma)
            i += 1
            print(i)
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
            imagem_amplitude = RasterFile(data = imagem_amplitude)
            imagem_amplitude.metadata = saida.metadata
            imagem_amplitude.file_name = "imagem_amplitude"
            saida.append(imagem_amplitude)
            
        self.print_text(u"imagens prontas para gravar, statistical stractor completo")

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
    statistics.append("cv")
    
    parametrosIN["statistics"] = statistics

    ss.data = parametrosIN
    resultados = ss.data
    
    imagens = resultados

    imagens.saveListByRoot (root_path="C:\\Users\\Paloschi\\Desktop\\data\\Testes\\saida", ext="tif")
    #cv.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")
    #sd.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida\\", ext=".tif")