'''
Created on Nov 19, 2015

@author: rennan.paloschi
'''

from Modelo.Funcoes import AbstractFunction
import threading
import numpy
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
        
        img_lat, img_long = self.img_lat_long(info, matriz_, nullValue)
        
        a = (float(180)/numpy.pi)
        
        
        for T in serie_T:
            T_ = T.loadRasterData()
            data_T = serie_T.getDate_time(file=T)
            dj = data_T.timetuple().tm_yday # Dia Juliano

            #print numpy.sin(numpy.radians(397.4794521))
            
            aa = float(360)/float(365)
            
            declinacao_solar = 23.45 * numpy.sin(numpy.radians(aa * (float(dj)-float(80))))
            
            b = numpy.tan(numpy.radians(declinacao_solar))
            
            
            hora_nascer_sol = numpy.arccos(numpy.radians(-numpy.tan(numpy.radians(img_lat) * numpy.tan(numpy.radians(b)) * a)))
            
            #hora_nascer_sol = numpy.arccos(-numpy.tan(img_lat) * numpy.tan(b) * a)
            #c = -numpy.tan(img_lat) * numpy.tan(b)
            #print c
            #print numpy.arccos(c)
            #hora_nascer_sol = (float(2)/5) * numpy.arccos(c)
            #hora_nascer_sol = (hora_nascer_sol/2)


            
            print hora_nascer_sol


    def img_lat_long(self, info, matriz_, nullValue):
        
        n_linhas = len(matriz_)
        n_colunas = len(matriz_[0])
        
        img_lat = numpy.zeros((n_linhas, n_colunas)).astype(dtype="float32")
        img_long = numpy.zeros((n_linhas, n_colunas)).astype(dtype="float32")
        
        x_pixelSize, y_pixelSize = self.pixel_size(info)
        
        init_y_position = float(info["ymax"]) - (y_pixelSize/2)
        init_x_position = float(info["xmin"]) + (x_pixelSize/2)
        
        for i_linha in range(0, n_linhas/4):
            
            self.setProgresso(i_linha, n_linhas)
            progress(self.progresso/100)
            
            cy = init_y_position - (y_pixelSize * i_linha)
            
            for i_coluna in range(0, n_colunas/4):
                
                value = matriz_[i_linha][i_coluna]
                        
                #if threading.current_thread().stopped() : return None
                        
                #if value != nullValue:                 
                cx = init_x_position + (x_pixelSize * i_coluna)
                img_lat[i_linha][i_coluna] = cy
                img_long[i_linha][i_coluna] = cx
        
        return img_lat, img_long       
                      
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