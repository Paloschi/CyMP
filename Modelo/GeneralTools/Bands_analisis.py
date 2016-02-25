# -*- coding: utf-8 -*-

'''
Created on 08/01/2016

@author: Paloschi
'''

from Modelo.beans import RasterFile
import sys

root = "C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\"
path = root + "ya_invertido_soma.tif"
import numpy as np

raster = RasterFile(file_full_path = path)
data_raster = raster.loadRasterData(True)

nodata = raster.metadata["nodata"]

print nodata

print ""


sys.stdout.write( "media" + "\t") 
sys.stdout.write( "minimo" + "\t") 
sys.stdout.write( "maximo" + "\t") 
sys.stdout.write( "coeficiente de variação" + "\t") 
print("")
    
for band in data_raster:
    mean = list()
    for x in band:
        for y in x:
            if (not np.ma.is_masked(y) and y != 0):
                mean.append(y)
    
    if len(mean)== 0:
        mean = 0
    media = np.mean(mean)
    sys.stdout.write( str(media) + "\t")
    sys.stdout.write( str(np.min(mean)) + "\t")
    sys.stdout.write( str(np.max(mean)) + "\t")
    sd = np.nanstd(mean) 
    if media!= 0:
        cv = sd / (media) * 100
    else :
        cv = 0
    
    sys.stdout.write( str(sd) + "\t")
    print ""
    

for band in data_raster:
    mean = list()
    for x in band:
        for y in x:
            if (not np.ma.is_masked(y)):
                mean.append(y)
    
                      