'''
Created on Mar 2, 2015

@author: Paloschi
'''

import fiona
from Modelo.beans import ABData
import gdal
progress = gdal.TermProgress_nocb

class GetShapeData(ABData):
    '''
    classdocs
    '''
    
    def __execOperation__(self):
        dados = self.__data.data
        
        print("Lendo Shape...")
        
        data_values = list()
        data = dict()
        
        progress( 0.0 )
        i = float(0) 
        with fiona.open(dados, 'r') as shape:
            total = len(shape)  
            for polygon in shape:
                data_values.append(polygon)
                i +=1
                progress( i / total)
                
            data['properties'] = shape.schema.copy()['properties']
        data['table_data'] = data_values
        data['data_path'] = self.__data.data
        data['data_name'] = self.__data.data_name
        
        print('Leitura completada')   
        return data        