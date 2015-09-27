'''
Created on 27/09/2015

@author: Rennan
'''

from Modelo.beans import RasterFile
import datetime

def Ds_DC_to_date(data):
        
        n = len(str(data))
        year = int(str(data)[0:4])    
        days = int(str(data)[4:n])
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
        return date



raster = RasterFile(file_full_path="C:\\Gafanhoto WorkSpace\\Soja11_12\\Datas_DS-DC\\semeadura_soja_11-12.tif")
matriz = raster.loadRasterData()


matriz = Ds_DC_to_date(matriz)



print matriz[600:1000,700:1200]