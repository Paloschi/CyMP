'''
Created on Aug 4, 2015

@author: Paloschi
'''
from Modelo.beans import FileData
import rasterio
import subprocess

class RasterFile(FileData):
    '''
    essa classe representa o tipo de dado Raster (tif, img etc)
    '''
    metadata = None
    caption_nx_ny_name = 'Size is ' 
    caption_xmin_ymin = 'Upper Left'
    caption_xmax_xmin = 'Lower Right'
        
    def loadRasterData(self, isCube = False):
        
        if self.data != None : return self.data
        
        with rasterio.open(self.file_full_path) as raster:
            
            self.metadata = raster.meta
            if (not isCube) : 
                return raster.read_band(1)
            else :
                while True :
                    cubo = list()
                    i_band = 1
                    try:
                        cubo.append(raster.read_band(i_band))
                        i_band+=1
                    except :
                        break
                print ("imagem lida, numero de bandas:", i_band)
        
    def saveRasterData(self, band_matrix=None):
        '''
            #Salva imagem em uma determinada pasta
        '''
        
        if band_matrix == None : band_matrix = self.data
        
        try: 
            metadata = self.metadata
            
            '''
                Listas de Drivers GDAL: http://www.gdal.org/formats_list.html
            '''
            
            if self.file_ext == "tif" : metadata.update(driver="GTiff") 
            elif self.file_ext == "img" : metadata.update(driver="HFA") 

            with rasterio.open(path = self.file_full_path, mode = 'w', **metadata) as dst:
                try:
                    dst.write_band(1, band_matrix)
                except ValueError: 
                    print "ERRO - Erro ao tentar salvar a imagem: ", self.file_full_path
                    print "MOTIVO - Índices inconsistentes, erro ao escrever banda"
        except ValueError: 
            print "ERRO - Erro ao tentar criar arquivo, verificar a existencia do diretório informado"
            
    def getRasterInformation(self):
           
        data = dict()
        
        print("Obtendo informacao da imagem")
               
        info = subprocess.check_output(['gdalinfo', '-nogcp','-nomd', '-norat', '-noct', str(self.file_full_path)])
        
        print info
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
        data['ymax'] = info_s[1].replace(' ', '').replace(',', '')
        
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
        data['ymin'] = info_s[1].replace(' ', '').replace(',', '')
       
        print("Informacoes da imagem lidas")
       
        return data 