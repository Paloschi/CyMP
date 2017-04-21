'''
Created on 04/12/2015

@author: Paloschi
'''
from Modelo.beans.SerialFileData import SerialFile

nome_cubo = "Cubo_EVI_Modis_cascavel_2011_12.tif"

if __name__ == '__main__':
    
    imagens = SerialFile(root_path="C:\\CyMP\\\Gafanhoto\\\DADOS\\\Imagens Cascavel\\\Modis\\")
    imagens.saveListLike1Image(nome_cubo)
    