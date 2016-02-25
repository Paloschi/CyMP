# -*- coding: utf-8 -*-
'''
Created on Aug 4, 2015

@author: Paloschi
'''

from Modelo.beans import FileData
try:
    import fiona
except:
    print u"ERRO - não foi possível carregar a biblioteca fiona, tente configurar as variáveis de ambiente"
try:
    import gdal
except:
    print u"ERRO - não foi possível carregar a biblioteca gdal, tente configurar as variáveis de ambiente"
       
progress = gdal.TermProgress_nocb



class VectorFile(FileData):
    '''
    essa classe representa um arquivo do tipo vetorial (shp)
    '''


    def readVectorData(self):
        
        print("Lendo Shape...")
        
        data_values = list()
        data = dict()
        
        progress( 0.0 )
        
        i = float(0) 
        with fiona.open(self.file_full_path, 'r') as shape:
            total = len(shape)  
            data['properties'] = shape.schema.copy()['properties']
            for polygon in shape:
                data_values.append(polygon)
                i +=1
                progress( i / total)
            
        data['table_data'] = data_values
        
        print('Leitura completada')  
         
        return data    
    

        

        