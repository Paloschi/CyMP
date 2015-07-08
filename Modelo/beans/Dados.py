# -*- coding: utf-8 -*-
'''
Created on Jan 21, 2015

@author: Paloschi
'''
from abc import ABCMeta, abstractmethod, abstractproperty
import rasterio
import os
import gdal
progress = gdal.TermProgress_nocb

#from numpy.core.numeric import dtype
#from bz2 import compress

class AbtractData(object):
    
    __metaclass__ = ABCMeta # Essa classe � abstrata, n�o pode ser instanciada
    
    SimpleData = 1
    ListData = 2
    DictData = 3
    OperationData = 4

    data_name = None
    data_type = None 
    data_path = None
    data_ext = None
    data_metadata = None
    __data = None   
    
    @property    
    def data(self):
        return self.__data
        
    @data.setter
    def data(self, data):
        self.__data = data


    
class SimpleData(AbtractData):
    'Classe com um mapa concreto'
    
    def __init__(self, path=None, data=None):
        
        if(path!=None):
            path_ext = str(path).split('.') # separa o path da extencao
            
            ext = path_ext[-1] # pega soh a extencao
            
            path_without_ext = str(path).replace("." + ext, "") # tira a extencao do path
            
            if(path_without_ext.find("/") != -1):
                data_name = path_without_ext.split("/")[-1]
                data_path = path_without_ext.replace(data_name, "")
            elif(path_without_ext.find("\\") != -1):
                data_name = path_without_ext.split("\\")[-1]
                data_path = path_without_ext.replace(data_name, "")
            else:
                data_name = path_without_ext
                data_path = ""                
            
            self.data_name = data_name
            self.data_ext = ext
            self.data_path = data_path
            
        self.data = data
        self.data_type = AbtractData.SimpleData
        
    def loadData(self):
        
        with rasterio.open(self.data) as map:
            self.data_metadata = map.meta
            return map.read_band(1)  # pixel values
        
    @property    
    def data(self):
        return self.__data
        
    @data.setter
    def data(self, data):
        self.__data = data 
        
    def saveImage(self, rootdir=None, image=None, ext=None):
        '''
            Salva imagem em uma determinada pasta
        '''
        
        if image==None:
            image = self.data
            image_name = (self.data_name.split("/")[-1])
        else:   
            image_name = image.data_name.split("/")[-1]
            
        if ext!=None:
            image_name = image_name + ext
            
 
        
        print("image name: " + image_name)    
        saida = rootdir + image_name
                
        try: 
            metadata = self.data_metadata
            metadata.update(driver="GTiff", count=1, dtype=rasterio.int16) 
            print(metadata)
            with rasterio.open(path = saida, mode = 'w', **metadata) as dst:
                dst.write_band(1, image)
                
        except:
            metadata = self.data_metadata
            metadata.update(driver="GTiff", count=1, dtype=rasterio.int32) 
            with rasterio.open(path = saida, mode = 'w', **metadata) as dst:
                dst.write_band(1, image)
    
       
class SerialData(AbtractData, list):
      
    def __init__(self, data_name=None, data=None):
        super(SerialData, self).__init__()
        self.data_type = "SerialData"
        self.data = data
    
    def loadData(self):
        
        total = len(self)
        maps = list()    
        n_iteracoes= 0
        progress( 0.0)
        for map in self:
            maps.append(map.loadData())
            n_iteracoes+=1
            progress( n_iteracoes / float(total))    
        self.dada_loaded = maps
        
        return maps
    

    def loadListByRoot(self, rootDir=None, filter=None):
        '''
            Abre uma lista de mapas localizados em uma determinada pasta
        ''' 
        if rootDir == None : rootDir = self.data
        
        for root, dirs, files in os.walk(rootDir):
            for f in files:
                if(filter==None):
                    self.append(SimpleData(data=rootDir+f))
                    #print(rootDir+f)
                else:
                    if(str(f).split('.')[-1]==filter):
                        self.append(SimpleData(path=rootDir+f, data=rootDir+f))
                        #print(rootDir+f)
        
        return self
    
    def saveListByRoot(self, imagens, rootdir, ext=None):
        
        '''
            Salva lista de dados presentes em uma determinada pasta
        '''
        print(self.data_metadata)
        
        i = 0
        if (len(imagens) > 0):
        
            for img in imagens: 
                print("====================== Extportando Imagem =======================")
                print("data name: " + str(self[i].data_name))
                image_name = self[i].data_name.split("/")[-1]    
                print("image name: " + image_name)    
                saida = rootdir + image_name + "." + ext
                print("caminho de saida: " + str(saida))
                print("imagem : \n" + str(img.data))
                
                metadata = self.data_metadata
                metadata.update(driver="GTiff", count=1, dtype=img.data.dtype) 
                with rasterio.open(path = saida, mode = 'w', **metadata) as dst:
                    dst.write_band(1, img.data)
                i+=1

            
    def saveListLike1Image(self, imagens, rootdir, ext=None):
        
        i = 0
        n_img = len(imagens)
        if (n_img > 0):
            metadata = self.data_metadata
            saida = rootdir + "cubo.tif"
            
            metadata.update(driver="GTiff", count=n_img, dtype=imagens[0].data.dtype)          
            with rasterio.open(path = saida, mode = 'w', **metadata) as dst:
                i = 0
                print("numero de bandas a escrever: " + str(len(imagens)))
                for img in imagens: 
                        print (img.data)
                        print (img.data_name)
                        dst.write_band(1, img.data)
                        print("banda escrita: " + str(i))
                        i+=1  
                
class TableData(dict, AbtractData):

    def __init__(self, data_name=None):
        self.data = dict()
        self.data_name = data_name
        self.data_type = "TableData"