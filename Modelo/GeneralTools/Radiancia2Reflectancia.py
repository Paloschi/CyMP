'''
Created on May 22, 2017

@author: Rennan Andres Paloschi
'''

import math
import numpy
from Modelo.beans.RasterData import RasterFile

path_saida = "C:/Users/PGSERE16/OneDrive - inpe.br/1- Doutorado/Quarto Trimestre/Geo/Trabalho/Dados GEO/Imagens LISS/Corrigidas/"
path_entrada = "C:/Users/PGSERE16/OneDrive - inpe.br/1- Doutorado/Quarto Trimestre/Geo/Trabalho/Dados GEO/Imagens LISS/Reprojetadas/"
image_name = "LISS3_20120304_337_082_L2_BAND3_S2000"
radiance_name = "LISS3_20120304_337_082_B3_S2000"  + "_Radiance"
reflectance_name = "LISS3_20120304_337_082_B3_S2000" + "_Reflectance"
extensao = "tif"

#Lmax = 120.6400 # banda 2
Lmax = 151.3100 # banda 3
Lmin = 0.00
Qcalmax = 255
#ESUN = 1846.77 # banda 2
ESUN = 1575.50 # banda 3

astronomic_distance = 0.992 # para o dia 20120304
sun_elevation_angle = 61.2456329971 # para o dia 20120304

#astronomic_distance = 1.0016411972894357 # para o dia 20130716
#sun_elevation_angle = 55.7933619326 # para o dia 20130716
zenital_angle = 90 - sun_elevation_angle

Imagem_raster = RasterFile(file_name = image_name, file_path=path_entrada, ext=extensao)
Imagem_ = numpy.array(Imagem_raster.loadRasterData()).astype(dtype="float32")

#Image_radiance_ = ((Lmax - Lmin) / Qcalmax) * Imagem_ + Lmin
Image_radiance_ = (Imagem_ / numpy.max(Imagem_)) * (Lmax - Lmin) + Lmin

image_radiance = RasterFile(data = Image_radiance_, file_path=path_saida, file_name=radiance_name, ext=extensao)
image_radiance.metadata = Imagem_raster.metadata
image_radiance.metadata.update(dtype = image_radiance.data.dtype)
image_radiance.saveRasterData()


Image_reflectance_ = (math.pi * Image_radiance_ * pow(astronomic_distance, 2)) / (ESUN * math.cos(zenital_angle * math.pi / 180.0))

image_reflectance = RasterFile(data = Image_reflectance_, file_path=path_saida, file_name=reflectance_name, ext=extensao)
image_reflectance.metadata = Imagem_raster.metadata
image_reflectance.metadata.update(dtype = image_reflectance.data.dtype)
image_reflectance.saveRasterData()

        

        

