'''
Created on Mar 3, 2015

@author: Paloschi
'''
from beans import Dados

class SplitTable(Dados.AbtractData):
    '''
    separa uma tabela baseado em uma lista de atributos
    '''
    
    def __init__(self, nome=None):
        self.__data = None
        self.data_name = nome
        self.data_type = "operation"
    
    @property    
    def data(self):
        dados = self.__data.data
        dados_tabela = dados['table'].data # se tiver mais que uma tabela, so faz a primeira
        tabela = dados_tabela['table_data']
        atributos = dados['atributos']
        data = dict()
        data['data_path'] = dados_tabela['data_path']
        
        if atributos == None:
            data["unicMap"] = tabela
            return data
        
        print("Dividindo tabela de dados em grupos...")  
        
        for tupla in tabela:
            id = str()
            
            for atributo in atributos:
                id += str(tupla['properties'][atributo]) 
            
            try:
                data[id].append(tupla)
            
            except:
                tuplas = list()
                tuplas.append(tupla)
                data[id] = tuplas
        
        print ("Seperacao em gupos Completada")
        
        return data
        

    @data.setter
    def data(self, data):
        self.__data = data