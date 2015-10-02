# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2015

@author: Paloschi
'''

from AbstractData import ABData, SERIAL_FILE_DATA
from Modelo.beans import RasterFile, FILE_DATA 
import os
import gdal
progress = gdal.TermProgress_nocb
import rasterio
import sys
import datetime

class SerialFile(ABData, list):
    '''
        Por default le somente tif e img
        A menos que uma classe especifica precise de outros arquivos
        entao deve-se modificar os filtros
    '''
    
    __root_path = None
    root_filter = ("tif", "img")
    metadata = None    

    def __init__(self, **params):
        super(SerialFile, self).__init__(SERIAL_FILE_DATA)
        
        if params.get("root_filter") != None : self.root_filter = params.get("root_filter")
        if params.get("root_path") != None : self.root_path = params.get("root_path")
    
    @property
    def root_path(self):
        return self.__root_path
    
    @root_path.setter
    def root_path(self, root_path):
        self.__root_path = os.path.normpath(root_path)  
        
    def loadListByRoot(self, rootDir=None, filtro=None):
        '''
            Abre uma lista de mapas localizados em uma determinada pasta
        ''' 
        
        
        if rootDir != None : self.root_path = rootDir
        if filtro != None : self.root_filter = filtro
        
        print("endereco das imagens: ", self.root_path)
        
        for a, b, files in os.walk(self.root_path):
            for f in files:
                f = RasterFile(file_full_path = self.root_path + "\\" + f)  
                if(self.root_filter==None):
                    self.append(f)
                else:
                    if( f.file_ext in self.root_filter):
                        self.append(f)
                        
        return self 
        
    def loadListRasterData(self):
        '''
            Carreca os dados matriciais e forma uma matriz de 3 dimenções
            As configurações de metadado raster que serão consideradas, serão do primeiro raster lido
        '''
        
        if len(self) == 0 : self.loadListByRoot()
        n_files = len(self)
        
        sys.stdout.write( "Carregando arquivos (" + str(n_files) + " arquivos): ")
        
        
        files = list()    
        n_iteracoes = 0
        progress(0.0)
        
        for f in self:
            files.append(f.loadRasterData())
            n_iteracoes+=1
            progress( n_iteracoes / float(n_files))
        
         
        
        if len(self)!=0:
            progress( float(1)) 
            self.metadata = self[0].metadata
            return files
        else:
            print "nenhuma imagem caregada"
            return None
        
    def saveListByRoot(self, root_path=None, ext=None, sufixo=None):
        
        '''
            Salva lista de dados presentes em uma determinada pasta
            
            Se não tiver extenção declarada, será gravado na primeira extençao da primeira imagem
        '''
        
        if len(self) == 0:
            print "não há nenhuma imagem a ser salva"
            
        if root_path != None : self.root_path = root_path
        
        
        n_images =  len(self)
        
        sys.stdout.write( "Salvando arquivos (" + str(n_images) + " arquivos): ")
        progress(0.0)
        
        for i in range(0, n_images): 
            
            image = self[i]
            
            if sufixo != None : image.file_name = image.file_name + sufixo
            if ext != None : image.file_ext = ext
            if root_path != None : image.file_path = root_path
            
            image.saveRasterData(image, metadata= self.metadata)
            progress( i+1 / float(n_images)) 

    def saveListLike1Image(self, name=None, images_bands_matrix=None, root_path=None, ext=None):
 
        if images_bands_matrix != None : 
            self.metadata.update(dtype=images_bands_matrix.dtype) 
            n_images =  len(images_bands_matrix)

        else:
            images_bands_matrix = self.loadListRasterData()
            n_images =  len(self)
            
        if root_path != None : self.root_path = root_path
        if ext == None : ext = self[0].file_ext
        if name != None : self.name = name
        
        if ext == "tif" : self.metadata.update(driver="GTiff") 
        elif ext == "img" : self.metadata.update(driver="HFA") 
        
        self.metadata.update(count=n_images)
        
        print self.metadata
        
        path = self.root_path + "\\" + name + "." + ext
        
        sys.stdout.write( "Salvando bandas em unico arquivo (" + str(n_images) + " bandas): ")
        progress(0.0)  
               
        with rasterio.open(path = path, mode = 'w', **self.metadata) as dst:
            
            for i in range(0, n_images):
                #print(i)
                dst.write_band(i+1, images_bands_matrix[i])
                progress( i / float(n_images)) 
             
class SerialTemporalFiles(SerialFile):
    
    prefixo = ""
    sufixo = ""
    date_mask = ""
    mutiply_factor = 1
    
    def getDate_time(self, i=None, file=None):
        '''
            Essa função foi criada para facilitar a obtenção da data do arquivo como objeto date
        '''
        
        
        if file==None : file = self[i]
        
        only_date = file.file_name

        if self.prefixo!=None : 
            only_date = only_date.replace(self.prefixo,"")
        if self.sufixo!=None : only_date = only_date.replace(self.sufixo, "")  
        date = datetime.datetime.strptime(only_date, self.date_mask) 

        return date  

    def setDate_time(self, date, i):
        '''
            Essa função foi criada para facilitar a criação do nome baseado em data
        '''
        
        file = self[i]
        only_date = date.strftime(self.date_mask)   
        name = self.prefixo + only_date + self.sufixo
        file.file_name = name
    
        

    