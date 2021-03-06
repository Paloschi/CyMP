﻿# -*- coding: utf-8 -*-
'''
Created on Aug 4, 2015

@author: Paloschi
'''
from Modelo.beans import FileData
from Modelo.beans.TableData import TableData

try:
    import rasterio
except:
    print u"ERRO - não foi possível carregar a biblioteca rasterIO, tente configurar as variáveis de ambiente"
import subprocess

class RasterFile(FileData):
    '''
    essa classe representa o tipo de dado Raster (tif, img etc)
    '''
    metadata = None
    caption_nx_ny_name = 'Size is ' 
    caption_xmin_ymin = 'Upper Left'
    caption_xmax_xmin = 'Lower Right'
    caption_NoDataValue = 'NoData Value='
        
    def loadRasterData(self, isCube = False):
        
        if self.data != None : return self.data
        
        try :
        
            with rasterio.open(self.file_full_path) as raster:
                
                self.metadata = raster.meta
                if (not isCube) : 
                    return raster.read_band(1)
                else :
                    cubo = list()
                    i_band = 1
                    while True :
                        try:
                            cubo.append(raster.read_band(i_band))
                            i_band+=1
                        except :
                            break
                    print ("imagem lida, numero de bandas:", i_band-1)
                    return cubo
                
                return self
        
        except :
            
            print "Falha ao tentar abrir imagem", self.file_full_path   
            return None
        
    def saveRasterData(self, band_matrix=None, metadata=None, file_path=None, ext=None):
        '''
            #Salva imagem em uma determinada pasta
        '''
        
        if file_path != None : self.file_path = file_path
        if ext != None : self.file_ext = ext
        if band_matrix != None : self.data = band_matrix
        if metadata != None : self.metadata = metadata
        
        try: 

            '''
                Listas de Drivers GDAL: http://www.gdal.org/formats_list.html
            '''
            #print ("salvando imagem  " + self.file_full_path)
            
            if self.file_ext == "tif" : self.metadata.update(driver="GTiff") 
            elif self.file_ext == "img" : self.metadata.update(driver="HFA") 
            self.metadata.update(dtype=self.data.dtype, compress='lzw')
        

            
            #print(metadata)
            #print(len(self.data), len(self.data[0]))
            
            
            #import os

            #os.chdir(self.file_path)

            #for nome in os.listdir('.'):
                #novo_nome = nome.replace(".tif_EbM", "")
                #os.rename(nome, novo_nome)
                #print nome
                
            #print self.file_full_path
            
            with rasterio.open(path = str(self.file_full_path), mode = 'w', **self.metadata) as dst:
                try:
                    dst.write(self.data, 1)
                except ValueError, e: 
                    print str(e)
                    print "ERRO - Erro ao tentar salvar a imagem: ", self.file_full_path
                    print "MOTIVO - índices inconsistentes, erro ao escrever banda"
            
        except ValueError: 
            print u"ERRO - Erro ao tentar criar imagem "+ self.file_name +u", verificar a existência do diretório informado ou se a imagem esta aberta em outro software"
            
    def getLoadJustMetaData(self):
        
        try :
            with rasterio.open(self.file_full_path) as raster:
                
                self.metadata = raster.meta
        
        except :
            print "Falha ao tentar abrir imagem", self.file_full_path   
            return None
            
    def getRasterInformation(self):
           
        data = TableData()
        
        print("Obtendo informacao da imagem")
               
        info = subprocess.check_output(['gdalinfo', '-nogcp','-nomd', '-norat', '-noct', str(self.file_full_path)])
        
        # recupera numero de linhas e colunas
        
        index_init = info.index(self.caption_nx_ny_name)
        text_rest = info[index_init:]
        index_end = text_rest.index('\n') + index_init
        
        info_s = info[index_init + len(self.caption_nx_ny_name):index_end]
        info_s = info_s.replace('\r', '').split(', ')
        
        data['nx'] = info_s[0]
        data['ny'] = info_s[1]
        
        # recupera numero inicio do mapa xmax e ymax
        index_init = info.index(self.caption_xmin_ymin)
        text_rest = info[index_init:]
        index_end = text_rest.index('\n') + index_init
        
        info_s = info[index_init + len(self.caption_xmin_ymin):index_end]
        info_s = info_s.replace('\r', '').replace('(','').replace(')','').split(' ')
        
        for atr in info_s:
            if atr == '':
                info_s.remove(atr)
        
        data['xmin'] = info_s[0].replace(' ', '').replace(',', '')
        data['ymin'] = info_s[1].replace(' ', '').replace(',', '')
        
        # recupera numero inicio do mapa xmin e ymin
        index_init = info.index(self.caption_xmax_xmin)
        text_rest = info[index_init:]
        index_end = text_rest.index('\n') + index_init
        
        info_s = info[index_init + len(self.caption_xmax_xmin):index_end]
        info_s = info_s.replace('\r', '').replace('(','').replace(')','').split(' ')
        
        for atr in info_s:
            if atr == '':
                info_s.remove(atr)
        
        data['xmax'] = info_s[0].replace(' ', '').replace(',', '')
        data['ymax'] = info_s[1].replace(' ', '').replace(',', '')
        
        #Recupera NoDataValue
        try: 
            index_init = info.index(self.caption_NoDataValue)
        
            text_rest = info[index_init:]
            index_end = text_rest.index('\n') + index_init
            
            info_s = info[index_init + len(self.caption_NoDataValue):index_end]
            
            data['NoData'] = info_s.replace('\r', '')
        except : 
            data['NoData'] = None
            
        print("Informacoes da imagem lidas")
       
        return data 