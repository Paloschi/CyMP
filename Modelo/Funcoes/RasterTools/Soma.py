'''
Created on 04/12/2015

@author: Paloschi
'''
from Modelo.beans.SerialFileData import SerialFile
from Modelo.beans import RasterData
import numpy

nome_cubo = "Cubo_dr_soja_2011_12"

if __name__ == '__main__':
    
    imagens = SerialFile(root_path="C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\7-Ya2")
    imagens.loadListByRoot()
    
    img_ = numpy.array(imagens[0].loadRasterData()).astype(dtype="uint32")
    print "tamanho:", len(imagens)
    
    for i in range(len(imagens)-1):
        img_ += imagens[i+1].loadRasterData()
        print i
        
    img_total = RasterData.RasterFile()
    img_total.file_full_path = "C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\7-Ya2\\soma.tif"
    img_total.saveRasterData(img_, imagens[0].metadata)
        
        
    