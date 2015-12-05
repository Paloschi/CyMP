
from numpy import ma
import numpy
from Modelo.beans.RasterData import RasterFile

if __name__ == '__main__':
    img = RasterFile(file_full_path="C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\Modis\\DATAS\\32bSigned\\semeadura.tif")
    img_ = img.loadRasterData()

    
    print numpy.min(img_)