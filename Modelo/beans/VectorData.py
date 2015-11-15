'''
Created on Aug 4, 2015

@author: Paloschi
'''

from Modelo.beans import FileData
import fiona
import gdal
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
    

        

        