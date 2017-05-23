'''
Created on May 23, 2017

@author: Rennan Andres Paloschi
'''


import math
import numpy
from Modelo.beans.RasterData import RasterFile
from Modelo.beans.SerialFileData import SerialFile


path = "C:/Users/PGSERE16/OneDrive - inpe.br/1- Doutorado/Quarto Trimestre/Geo/Trabalho/Dados GEO/Imagens LISS/Corrigidas/"

lista_rasters = SerialFile()
lista_rasters.loadListByRoot(path)

for raster in lista_rasters:
    imagem_ = raster.loadRasterData()
    
    print(numpy.min(imagem_))
    
