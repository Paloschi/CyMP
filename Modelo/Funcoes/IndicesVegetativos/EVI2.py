# -*- coding: utf-8 -*-
'''
Created on Aug 17, 2015

@author: Paloschi
'''

from Modelo.beans import SerialFile
import rasterio
from numpy.core.numeric import array
import numpy

pathIn = "C:\\Users\\Paloschi\\Desktop\\New folder\\recortadas"
pathOut = "C:\Users\Paloschi\Desktop\New folder\EVI2"

imagens_rgb = SerialFile(root_path=pathIn)
imagens_rgb.loadListByRoot(filtro = "tif")

for img in imagens_rgb:
    with rasterio.open(img.file_full_path) as raster:
        r, g, b = raster.read()
        metadata = raster.meta
        
        '''EVI2= 2,5 [(N-R) / (N + 2,4R+1)] '''
        
    N = r.astype(rasterio.float64)# vermelho é o infravermelho próximo 
    R = b.astype(rasterio.float64) # azul é o vermelho
    
    #print r
    #print b
    
    #print N

    EVI2 = numpy.zeros(r.shape, dtype=rasterio.float64)
    
    EVI2 += 2.5 * (N - R) / (N + 2.4 * R + 1)
    
    #print("linhas e colunas: ", len(EVI2), len(EVI2[0]))
    #EVI2 = array(EVI2)
    
    #print EVI2.dtype
    
    img.data = EVI2
    img.file_name = img.file_name + "EVI2"
    img.file_path = pathOut
    metadata.update(dtype="float64")
    img.saveRasterData(band_matrix=EVI2, metadata=metadata)