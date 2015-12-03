# -*- coding: utf-8 -*-
'''
Created on Nov 19, 2015

@author: rennan.paloschi
'''

from Modelo.Funcoes import AbstractFunction
import numpy as np
from Modelo.beans import RasterFile, SERIAL_FILE_DATA
from Modelo.beans.SerialFileData import  SerialTemporalFiles
import gdal
progress = gdal.TermProgress_nocb
import time
import threading

class PPR(AbstractFunction):
    
    def __setParamIN__(self):
        self.descriptionIN["T"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de temperatura média"}
        self.descriptionIN["Cc"] = {"Required":True, "Type":None, "Description":"ìndice de colheita, valor double"}
        self.descriptionIN["PPR"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Configuração de imagens produtividade potencial bruta"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["PPR"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens produtividade potencial bruta"}
    
    def __execOperation__(self):
        
        serie_T = self.paramentrosIN_carregados["T"].loadListByRoot()
        serie_PPR = self.paramentrosIN_carregados["PPR"]
        self.Cc = self.paramentrosIN_carregados["Cc"]
        
        matriz = serie_T[0]
        matriz_ = matriz.loadRasterData()
        info = matriz.getRasterInformation()
        nullValue = info["NoData"]
        
        img_lat = self.img_lat_long(info, matriz_, nullValue)
        lat_rad = np.radians(img_lat)
        
        a = float(180)/np.pi
        
        ii=1
        
        for T in serie_T:
            
            if threading.currentThread().stopped()  : return 

            
            start = time.time()
            T_ = np.array(T.loadRasterData()).astype(dtype="float32")
            data_T = serie_T.getDate_time(file=T)
            dj = data_T.timetuple().tm_yday # Dia Juliano
            
            #print dj
            
            declinacao_solar = 23.45 * np.sin(np.radians((float(360)/float(365)) * (float(dj)-float(80))))
            declinacao_solar_r = np.radians(declinacao_solar)
            
            angulo_solar = np.arccos(np.radians(-np.tan(lat_rad) * np.tan(declinacao_solar_r))) * a

            "DR = Distancia relativa sol-terra"
            agulo_solar_r = np.radians(angulo_solar)
            if declinacao_solar != 0:
                DR = 1 + 0.0033 * np.cos(np.radians(360/(365*declinacao_solar)))
            else :
                DR = 1
            
            radiacao_topo_atmosfera = 37.6 * DR * ((np.pi/180) * angulo_solar * np.sin(declinacao_solar_r) * np.sin(lat_rad) + np.cos(declinacao_solar_r) * np.cos(lat_rad) * np.sin(agulo_solar_r))
            radiacao_topo_atmosfera = radiacao_topo_atmosfera * 23.92344
            
            ctn = 0.583 + 0.014 * T_ + 0.0013 * (T_**2) - 0.000037 * (T_**3)
            ctc = -0.0425 + 0.035 * T_ + 0.00325 * (T_**2) - 0.0000925 * (T_**3)
            
            n_t = range(len(T_))
            
            for i in n_t: 
                
                index = [(T_[i]<16.5) & (T_[i]>37)]
                
                ctn[i][index] = -0.0425 + 0.035 * T_[i][index] + 0.00325 * (T_[i][index]**2) - 0.0000925 * (T_[i][index]**3)
                ctc[i][index] = -1.085 + 0.07 * T_[i][index] + 0.0065 * (T_[i][index]**2) - 0.000185 * (T_[i][index]**3)
                
            
            PPBn = (31.7+0.219*radiacao_topo_atmosfera) * ctn * 0.6
            
            PPBc = (107.2+0.219*radiacao_topo_atmosfera) * ctc * 0.6
            
            PPBp = PPBn + PPBc
            
            PPR_ = 0.265455 * self.Cc * PPBp

            PPR = RasterFile(file_path=serie_PPR.root_path, ext="tif")
            PPR = serie_PPR.setDate_time(data_T, file=PPR)       
            PPR.metadata = T.metadata
            PPR.data = PPR_
            PPR.saveRasterData()
            PPR.data = None
            serie_PPR.append(PPR)
            
            ii +=1
            end = time.time()
            
            self.console("tempo restante(m):" + str( np.round(((end - start)  * (len(serie_T)-ii)) /60, 2)))
            self.setProgresso(ii, len(serie_T))
            
        return serie_PPR
            
            
    def img_lat_long(self, info, matriz_, nullValue):
        
        n_linhas = len(matriz_)
        n_colunas = len(matriz_[0])
        
        img_lat = np.zeros((n_linhas, n_colunas)).astype(dtype="float32")
        #img_long = np.zeros((n_linhas, n_colunas)).astype(dtype="float32")
        
        x_pixelSize, y_pixelSize = self.pixel_size(info)
        
        init_y_position = float(info["ymax"]) - (y_pixelSize/2)
        #init_x_position = float(info["xmin"]) + (x_pixelSize/2)
        
        for i_linha in range(0, n_linhas):
            
            self.setProgresso(i_linha, n_linhas)
            progress(self.progresso/100) 
            cy = init_y_position - (y_pixelSize * i_linha)
            img_lat[i_linha][:] = cy
        
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
        self.paramentrosIN_carregados["images"] = SerialTemporalFiles(root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\8-Diario\\tav")
        self.paramentrosIN_carregados["images"].prefixo = "tav_"  
        self.paramentrosIN_carregados["images"].date_mask = "%Y%m%d" 

        self.paramentrosIN_carregados["PPR"] = SerialTemporalFiles(root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\PPR")
        self.paramentrosIN_carregados["PPR"].prefixo = "ppr_"  
        self.paramentrosIN_carregados["PPR"].date_mask = "%Y-%m-%d" 
                
        self.Cc = 0.355994271009505
         
        self.__execOperation__()
        
    
if __name__ == '__main__':
    ppr = PPR()
    ppr.testar()