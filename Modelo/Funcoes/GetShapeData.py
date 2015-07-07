'''
Created on Mar 2, 2015

@author: Paloschi
'''

import fiona
from beans import Dados
import gdal
progress = gdal.TermProgress_nocb

class GetShapeData(Dados.AbtractData):
    '''
    classdocs
    '''
    def __init__(self, nome=None):
        self.__data = None
        self.data_name = nome
        self.data_type = "operation"
        
    def getDataProperties(self):
        dados = self.__data.data
        
        with fiona.open(dados, 'r') as shape:
            
            data_properties = shape.schema.copy()['properties']
        
    
        return data_properties
    
    @property    
    def data(self):
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
                
        data['table_data'] = data_values
        data['data_path'] = self.__data.data
        data['data_name'] = self.__data.data_name
        
        print('Leitura completada')   
        return data        

    @data.setter
    def data(self, data):
        self.__data = data