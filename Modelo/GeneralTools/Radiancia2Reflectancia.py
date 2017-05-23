'''
Created on May 22, 2017

@author: Rennan Andres Paloschi
'''

import math
import numpy
from Modelo.beans.RasterData import RasterFile

path_saida = "D:/OneDrive - inpe.br/1- Doutorado/Quarto Trimestre/Geo/Trabalho/Dados GEO/Imagens LISS/Corrigidas"
path_entrada = "D:/OneDrive - inpe.br/1- Doutorado/Quarto Trimestre/Geo/Trabalho/Dados GEO/Imagens LISS/Reprojetadas/"
image_name = "LISS3_20130716_336_082_L2_BAND2_S200"
radiance_name = "LISS3_20130716_336_082_B2_S200"  + "_Radiance"
reflectance_name = "LISS3_20130716_336_082_B2_S200" + "_Reflectance"
extensao = "tif"

Lmax = 12.064
Lmin = 0.00
Qcalmax = 255
ESUN = 1849.5
astronomic_distance = 1.0016411972894357
azimutal_angle = 22.43492934531324

Imagem_raster = RasterFile(file_name = image_name, file_path=path_entrada, ext=extensao)
Imagem_ = numpy.array(Imagem_raster.loadRasterData()).astype(dtype="float32")

#Image_radiance_ = ((Lmax - Lmin) / Qcalmax) * Imagem_ + Lmin
Image_radiance_ = (Imagem_ / numpy.max(Imagem_)) * (Lmax - Lmin) + Lmin

image_radiance = RasterFile(data = Image_radiance_, file_path=path_saida, file_name=radiance_name, ext=extensao)
image_radiance.metadata = Imagem_raster.metadata
image_radiance.metadata.update(dtype = image_radiance.data.dtype)
image_radiance.saveRasterData()


Image_reflectance_ = (math.pi * Image_radiance_ * 1000 * pow(astronomic_distance, 2)) / (ESUN * math.cos(azimutal_angle * math.pi / 180.0))

image_reflectance = RasterFile(data = Image_reflectance_, file_path=path_saida, file_name=reflectance_name, ext=extensao)
image_reflectance.metadata = Imagem_raster.metadata
image_reflectance.metadata.update(dtype = image_reflectance.data.dtype)
image_reflectance.saveRasterData()

        

        

