# -*- coding: utf-8 -*-
'''
Created on 21 de abr de 2017

@author: Rennan
'''

from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA, SerialFile, TableData
import matplotlib.pyplot as plt
import numpy as np
import math
import gdal

progress = gdal.TermProgress_nocb


class PrintPerfilChart(AbstractFunction):
    
    def __setParamIN__(self):
        self.descriptionIN["IMG"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagems"}
    
    def __setParamOUT__(self):
        return None
    
    def __execOperation__(self):
        serie_img = self.paramentrosIN_carregados["IMG"].loadListByRoot()
        
        n_linhas = len(serie_img[0].loadRasterData())
        n_colunas = len(serie_img[0].loadRasterData()[0])
        n_imagens = len(serie_img)
        
        profiles = np.zeros((n_linhas * n_colunas, n_imagens))
        progress(0.0)
        
        n_blocks = 1
        linha_inicio = 0
        linha_limite = 0
        
        n_profiles = float(n_linhas*n_blocks*n_imagens)
        
        for i_block in range(1, n_blocks+1):
            
            linha_inicio = linha_limite
            linha_limite = (n_linhas/n_blocks) * (i_block)
            if (i_block == n_blocks):
                linha_limite = n_linhas 
            
            #print(linha_inicio, linha_limite, n_colunas, n_imagens)
        
            for i_img in range(n_imagens):
                img_ = serie_img[i_img].loadRasterData()
                for i in range(linha_inicio, linha_limite):  
                    for ii in range(n_colunas):
                        profiles[i*ii][i_img] = img_[i][ii]
                        
                    progress( float((i+1) * i_block * (i_img+1)) / n_profiles)
            
            
            for profile in profiles:
                if (not (math.isnan(profile[0]))) : plt.plot(profile)
                    
        plt.show()
        
        #for i in range(n_linhas):    
        #    profile = []
        #    for ii in range(n_colunas):
        #       for img in serie_img:
        #           img_ = img.loadRasterData()
                    #NoData = img.getRasterInformation()["NoData"] 
        #           profile.append(img_[i][ii])
        #           print(ii)
        #    profiles.append(profile)
            
        #    progress( i / float(n_linhas))
        

            
       
        
        #plot_url = py.plot_mpl()
        
if __name__ == '__main__':
    
    imagens = SerialFile(root_path="C:\\CyMP\\Gafanhoto\\DADOS\\Imagens Cascavel\\Modis\\")
    
    param = TableData()
    param["IMG"] = imagens
    
    print_perfil = PrintPerfilChart()
    print_perfil.paramentrosIN_carregados = param
    
    print_perfil.data
    
