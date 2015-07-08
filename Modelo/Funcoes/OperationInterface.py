# -*- coding: utf-8 -*-

'''
Created on May 11, 2015
@author: Paloschi
'''
from Modelo.beans import Dados
from abc import ABCMeta, abstractmethod
from numpy.distutils.environment import __metaclass__



class Operation(Dados.AbtractData):
    
    '''
    Essa classe representa o padrão das operações e todas as operações devem herda-la
    ela descreve como deve ser as estruturas dentro da função para o correto funcionamento do software
    '''
    
    __metaclass__ = ABCMeta # Essa classe é abstrata, não pode ser instanciada
    
    descriptionIN = None # Descrição dos parametros de entrada das funções   
    descriptionOUT = None # descrição dos parametros de saída das funções
    paramentrosIN_carregados = dict() # parametros de entrada carrecados
    progresso = float(1)
    
    @abstractmethod # esse parametro deve ser implementado na classe filha
    def __setParamIN__(self):
        '''
            Esse método e o próximo (__setParamOut__) devem ser implementados conforme a operação
            estes meta-dados são importantes para o funcionamento mais automático possivel do software
        '''
        #self.descriptionIN["parametro1"] = "Descrição do primeiro parametro de entrada"
        #self.descriptionIN["parametro2"] = "Descrição do segundo parametro de entrada"
        pass
    
    @abstractmethod  # esse parametro deve ser implementado na classe filha 
    def __setParamOUT__(self):
        #self.descriptionOUT["parametro1"] = "Descrição do primeiro parametro de saída"
        #self.descriptionOUT["parametro2"] = "Descrição do segundo parametro de saída"    
        pass
    

    def __init__(self, params = None):
        '''
        Constructor padrão cuida da inicialização do objeto
        '''
        self.descriptionIN = dict()
        self.descriptionOUT = dict()
        
        self.__setParamIN__() # inicializa descrição de entrada
        self.__setParamOUT__() # inicializa descrição de saída
        
        self.data_type = Dados.AbtractData.OperationData #Seta o tipo de dado
        
        if(params!=None) : self.__LoadParams__(params) # caso os parametros sejam indicados no inicio, já são carregados

    def __LoadParams__(self, params):
        '''
        O for a serguir carrega os elementos necessários para funcionamento da função
        '''
        print "---------------"
        print self.descriptionIN
        print params
        print "---------------"
         
        for key in self.descriptionIN.keys():
            if (params[key].data_type != Dados.AbtractData.ListData) : self.paramentrosIN_carregados[key] = params[key].data
            else : self.paramentrosIN_carregados[key] = params[key].loadData()
            
        self.brutedata = params # caso a função precise do dado bruto
            
    @property    
    def data(self):
        if (self.data_name!=None) : print ("Iniciando Operação: " + self.data_name)
        resultado = self.__execOperation__()
        if (self.data_name!=None) : print ("Operação " + self.data_name + " concluída!")
        return resultado
        
    @data.setter
    def data(self, params):
        self.__LoadParams__(params)
        
    @abstractmethod # esse parametro deve ser implementado na classe filha   
    def __execOperation__(self):
        pass
    
    
        
        