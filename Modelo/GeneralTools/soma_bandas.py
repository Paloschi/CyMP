'''
Created on 10/01/2016

@author: Paloschi
'''

from Modelo.beans import RasterFile
root = "D:\\1 - Mestrado (segundo semestre)\\Dissertacao\\Estudo de caso\\Cubos\\"
path = root + "Cubo_Ya_invertido.tif"
import numpy as np

raster = RasterFile(file_full_path = path)
data_raster = raster.loadRasterData(True)



nodata = raster.metadata["nodata"]

metadata = raster.metadata
metadata["count"] = 1

print raster.metadata

soma = imagem_kc_ = np.zeros((len(data_raster[1]), len(data_raster[1][0]))).astype(dtype="float32")

for band in data_raster:
    soma += band

saida = RasterFile(file_full_path= path)
saida.file_name = "ya_invertido_soma"
saida.metadata = raster.metadata
saida.data = soma

saida.saveRasterData()
    
