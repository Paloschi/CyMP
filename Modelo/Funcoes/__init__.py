# -*- coding: utf-8 -*-
#from Filtro import *
#from GetImageInformation import *
#from GetShapeData import *
#from Interpola import *
#from PerfilExtractor import *
#from Soma import *
#from SplitTable import *
#from teste_str import *


if __name__ == '__main__':
    
    import GetImageInformation
    from Modelo.beans import Dados
       
    rootImgTeste = "C://Users//Paloschi//Desktop//data//Testes//ImagemExemploEcmwf//ope_south-america_evpt_20080701.img"
    imgTeste = Dados.SimpleData(data=rootImgTeste)
    
    paramIN = Dados.TableData()
    paramIN["imagem"] = imgTeste
    
    getImgInfo = GetImageInformation.GetImgInfo()
    getImgInfo.data = paramIN
    info = getImgInfo.data
    
    xmin = float(info["xmin"])
    xmax = float(info["xmax"])
    nx = float(info["nx"])
    
    print(xmin)
    print(xmax)
    print(nx)
    
    x_pixelSize = (xmax - xmin) / nx
    
    print (x_pixelSize)
    
    


