# -*- coding: utf-8 -*-
'''
Created on 31/05/2016

@author: Paloschi

Esse método converterá o formato "AnoDia" (2015045) para um numero começando em uma data informada
'''

import numpy as np
from Modelo.beans import TABLE_DATA, FILE_DATA, RasterFile
from numpy.core.numeric import array
import datetime
import gdal
progress = gdal.TermProgress_nocb   

def Ds_DC_to_date(data):
        n = len(str(data))
        year = int(str(data)[0:4])    
        days = int(str(data)[4:n])
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
        return date

def converter (dia_inicial, imagem):
    
    print "dia inicial: " + str(dia_inicial)
    
    ano_inicial = dia_inicial.year
    
    n_linhas = len(imagem)
    n_colunas = len(imagem[0])
    
    imagem_convertida = np.zeros((n_linhas, n_colunas))     
    imagem_convertida = array(imagem_convertida).astype(dtype="uint16")    
    
    print "iniciando conversão"
    
    progress(0.0)
    
    
    for i in range(0, n_linhas):
        #for ii in range(0, n_colunas):
            #try:
                #data_pixel = Ds_DC_to_date(imagem[i][ii])
                #delta_tempo = (data_pixel - dia_inicial).days
                #imagem_convertida[i][ii] = delta_tempo
                
                #n = len(str(data_pixel))
                #ano_pixel = int(str(data_pixel)[0:4])
                #dia_pixel = int(str(data_pixel)[4:n])
                
                #imagem_convertida[i][ii] = (dia_pixel - dia_inicial) + (ano_pixel - ano_inicial * 365)
                
            #except :
                #pass      
        
        ano_pixel = int(str(data_pixel)[0:4])
        imagem_convertida[i] = imagem[i]
        
        progress(i/float(n_linhas-1))
    print "Conversão terminada, retornando imagem"
    
    return imagem_convertida
    
if __name__ == '__main__':               
    
    imagem = RasterFile(file_full_path="C:\\Gafanhoto WorkSpace\\DataTestes\\raster\\semeadura_soja_11-12.tif")
    imagem_ = imagem.loadRasterData()
    
    data_minima = Ds_DC_to_date(np.min(imagem_))
    
    imagem.data = converter(data_minima, imagem_)
    imagem.file_name = imagem.file_name + "convertida"
    imagem.saveRasterData()
    
    