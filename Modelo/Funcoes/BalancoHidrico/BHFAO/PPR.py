'''
Created on Nov 19, 2015

@author: rennan.paloschi
'''

from Modelo.Funcoes import AbstractFunction
import threading
import numpy as np

from Modelo.beans.RasterData import RasterFile
from Modelo.beans.SerialFileData import SerialFile, SerialTemporalFiles

import gdal
from math import radians
progress = gdal.TermProgress_nocb

class Ks(AbstractFunction):
    
    def __setParamIN__(self):
        pass
    
    def __setParamOUT__(self):
        pass
    
    def __execOperation__(self):
        
        serie_T = self.paramentrosIN_carregados["images"].loadListByRoot()
        
        matriz = serie_T[0]
        matriz_ = matriz.loadRasterData()
        info = matriz.getRasterInformation()
        nullValue = info["NoData"]
        
        img_lat = self.img_lat_long(info, matriz_, nullValue)
        #img_lat = -26
        lat_rad = np.radians(img_lat)
        
        a = float(180)/np.pi
        b = float(np.pi)/180
        
        
        for T in serie_T:
            T_ = T.loadRasterData()
            data_T = serie_T.getDate_time(file=T)
            dj = data_T.timetuple().tm_yday # Dia Juliano
            
            #print dj
            
            declinacao_solar = 23.45 * np.sin(np.radians((float(360)/float(365)) * (float(dj)-float(80))))
            declinacao_solar_r = np.radians(declinacao_solar)
            
            angulo_solar = np.arccos(np.radians(-np.tan(lat_rad) * np.tan(declinacao_solar_r))) * a
            #angulo_solar = angulo_solar * (float(2)/15)
            #angulo_solar = 12 - (angulo_solar/2)
            "DR = Distancia relativa sol-terra"
            agulo_solar_r = np.radians(angulo_solar)
            if declinacao_solar != 0:
                DR = 1 + 0.0033 * np.cos(np.radians(360/(365*declinacao_solar)))
            else :
                DR = 1
            
            radiacao_topo_atmosfera = 37.6 * DR * ((np.pi/180) * angulo_solar * np.sin(declinacao_solar_r) * np.sin(lat_rad) + np.cos(declinacao_solar_r) * np.cos(lat_rad) * np.sin(agulo_solar_r))
            
            ctn = 0.583 + 0.014 * T + 0.0013 * (T^2) - 0.000037 * (T^3)
            for i in range(len(T)): 
                ctn[i][16.5>T>37] = -0.0425 + 0.035 * T[i][16.5>T>37] + 0.00325 * (T[i][16.5>T>37]^2) - 0.0000925 * (T[i][16.5>T>37]^3)
            
            ctc = -0.0425 + 0.035 * T + 0.00325 * (T^2) - 0.0000925 * (T^3)
            for i in range(len(T)):
                ctc[i][16.5>T>37] = -1.085 + 0.07 * T[i][16.5>T>37] + 0.0065 * (T[i][16.5>T>37]^2) - 0.000185 * (T[i][16.5>T>37]^3)
                
            
            print ctn
            print ctc
            
            
            
    def img_lat_long(self, info, matriz_, nullValue):
        
        n_linhas = len(matriz_)
        n_colunas = len(matriz_[0])
        
        img_lat = np.zeros((n_linhas, n_colunas)).astype(dtype="float32")
        #img_long = np.zeros((n_linhas, n_colunas)).astype(dtype="float32")
        
        x_pixelSize, y_pixelSize = self.pixel_size(info)
        
        init_y_position = float(info["ymax"]) - (y_pixelSize/2)
        init_x_position = float(info["xmin"]) + (x_pixelSize/2)
        
        for i_linha in range(0, n_linhas):
            
            self.setProgresso(i_linha, n_linhas)
            progress(self.progresso/100)
            
            cy = init_y_position - (y_pixelSize * i_linha)
            
            #for i_coluna in range(0, n_colunas/4):
                
                #value = matriz_[i_linha][i_coluna]
                        
                #if threading.current_thread().stopped() : return None
                        
                #if value != nullValue:                 
                #cx = init_x_position + (x_pixelSize * i_coluna)
            img_lat[i_linha][:] = cy
                #img_long[i_linha][i_coluna] = cx
        
        return img_lat#, img_long       
                      
    def pixel_size(self, info):
        
        xmin = float(info["xmin"])
        xmax = float(info["xmax"])
        nx = float(info["nx"])
        x_pixelSize = (xmax - xmin) / nx
        
        ymin = float(info["ymin"])
        ymax = float(info["ymax"])
        ny = float(info["ny"])
        y_pixelSize = (ymax - ymin) / ny  
        
        return x_pixelSize, y_pixelSize
                    
    def testar(self):
        
        self.paramentrosIN_carregados = dict()
        self.paramentrosIN_carregados["images"] = SerialTemporalFiles(root_path = "C:\\GafanhotoWorkspace\\Indices_BH\\ETc")
        self.paramentrosIN_carregados["images"].date_mask = "%Y-%m-%d"  
        self.__execOperation__()
        
    
if __name__ == '__main__':
    ks = Ks()
    ks.testar()