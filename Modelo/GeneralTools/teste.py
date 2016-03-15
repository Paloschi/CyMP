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



raster = RasterFile(file_full_path="C:\\Gafanhoto WorkSpace\\DataTestes\\out\\interpolado_no_gafanhoto\\evpt_20110101.tif")
raster.loadRasterData()
print raster.getRasterInformation()
raster = RasterFile(file_full_path="C:\\Gafanhoto WorkSpace\\DataTestes\\out\\interpolado_no_arcgis\\evpt_20110101.tif")
raster.loadRasterData()
print raster.getRasterInformation()
#print raster.metadata


