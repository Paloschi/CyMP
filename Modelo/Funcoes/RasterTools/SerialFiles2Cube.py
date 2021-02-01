'''
Created on 04/12/2015

@author: Paloschi
'''
from Modelo.beans.SerialFileData import SerialFile

nome_cubo = "ETo_9km_daily"

if __name__ == '__main__':
    
    imagens = SerialFile(root_path="D:\\ClimatcDataECMWF_ERA5LAND\\ECMWF_ERA5LAND\\1-ETo\\2-ETo_9km_daily")
    imagens.saveListLike1Image(name=nome_cubo, root_path="D:\\ClimatcDataECMWF_ERA5LAND\\ECMWF_ERA5LAND\\1-ETo")
    