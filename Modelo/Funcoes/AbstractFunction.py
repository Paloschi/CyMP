# -*- coding: utf-8 -*-

'''
Created on May 11, 2015
@author: Paloschi
'''

from Modelo.beans.AbstractData import ABData, FUNCTION_DATA
from abc import ABCMeta, abstractmethod
#from numpy.distutils.environment import __metaclass__
import numpy
import configparser
import threading
import logging as log


class Function(ABData):
    
    '''
    Essa classe representa o padrão das operações e todas as operações devem herda-la
    ela descreve como deve ser as estruturas dentro da função para o correto funcionamento do software
    '''
    
    __metaclass__ = ABCMeta # Essa classe é abstrata, não pode ser instanciada
    
    descriptionIN = None # Descrição dos parametros de entrada das funções   
    descriptionOUT = None # descrição dos parametros de saída das funções
    paramentrosIN_carregados = dict() # parametros de entrada carrecados
    progresso = float(1)
    console = None
    
    @abstractmethod # esse parametro deve ser implementado na classe filha
    def __setParamIN__(self):
        '''
            Esse método e o próximo (__setParamOut__) devem ser implementados conforme a operação
            estes meta-dados são importantes para o funcionamento mais automático possivel do software
        '''
        #self.descriptionIN["nome_atributo"] = {"Required":True, "Type":FILE_DATA, "Description":"um arquivo qualquer requerido"}
        pass
    
    @abstractmethod  # esse parametro deve ser implementado na classe filha 
    def __setParamOUT__(self):
        #self.descriptionOUT["parametro1"] = "Descrição do primeiro parametro de saída"
        #self.descriptionOUT["parametro2"] = "Descrição do segundo parametro de saída"    
        pass
    

    def __init__(self, param=None):
        '''
        Constructor padrão cuida da inicialização do objeto
        '''
        super(Function, self).__init__(FUNCTION_DATA) # seta o tipo do objeto
        
        self.descriptionIN = dict()
        self.descriptionOUT = dict()
        
        self.__setParamIN__() # inicializa descrição de entrada
        self.__setParamOUT__() # inicializa descrição de saída
        

    def __LoadParams__(self, params):
        '''
        O for a serguir carrega os elementos necessários para funcionamento da função
        
        Por enquanto não é recusivo com tabelas
        '''
        log.debug("---------------") 
        log.debug(self.descriptionIN)
        log.debug(params)
        log.debug("---------------")
         
        for key in self.descriptionIN.keys():
            
            if key not in params.keys() or params[key] is None:
                if self.descriptionIN[key]["Required"] :
                    raise Exception((u"Parametro " + key + u" é requerido na função " + self.__class__.__name__))   
                else :
                    self.paramentrosIN_carregados[key] = None
            elif self.descriptionIN[key]["Type"] == FUNCTION_DATA:         
                self.paramentrosIN_carregados[key] = params[key].data    
            else:
                self.paramentrosIN_carregados[key] = params[key]      
            
            if self.paramentrosIN_carregados[key]!=None and self.descriptionIN[key]["Type"]!=None:
                if self.paramentrosIN_carregados[key].data_type != None:
                    if self.paramentrosIN_carregados[key].data_type != self.descriptionIN[key]["Type"]:
                        raise Exception("Parametro incompativel: " + key)   
            
    @property    
    def data(self):
        #if (self.data_name!=None) : print ("Iniciando Operação: " + self.data_name)
        resultado = self.__execOperation__()
        #if (self.data_name!=None) : print ("Operação " + self.data_name + " concluída!")
        return resultado
        
    @data.setter
    def data(self, params):
        self.__LoadParams__(params)
        
    @abstractmethod # esse parametro deve ser implementado na classe filha   
    def __execOperation__(self):
        pass
    
    def executar(self, parametros):
        config = configparser.RawConfigParser()
        config.read('workspace.properties')
        #DebugMode=config.get('Config', 'DebugMode')
        DebugMode = "True"

        if DebugMode == "True" :
            
            #print ("Esperando console carregar")
            #while self.console is None : pass
            #print ("Console carregado")
    
            try:
                self.data = parametros
                return self.data
            except Exception as e:
                print(e)
                #self.console(str(e))
                #self.console(u"Função interrompida")
                self.setProgresso(100, 100)
                threading.currentThread().stop()
                return None
        
        else:
            while self.console is None : pass
            try: 
                self.data = parametros
                return self.data
            except:
                self.console(u"Erro desconhecido, reveja os parametros ou ative o DebugMode para saber mais")
                self.console(u"Função interrompida")
                self.setProgresso(100, 100)
                threading.currentThread().stop()
                return None
        
    def setProgresso (self, indice, total):
        self.progresso = (indice / float(total) * 100)
        
    def compactar(self, imagem_):
        
        minimo = numpy.min(imagem_)
        maximo = numpy.max(imagem_) 
            
        if minimo >= 0 :
            #if maximo <= 255:
            #    imagem_ = numpy.array(imagem_).astype("uint8")
            if maximo <= 65535:
                imagem_ = numpy.array(imagem_).astype("uint16")
            elif maximo <= 4294967295:
                imagem_ = numpy.array(imagem_).astype("uint32")
        else :
            if minimo >= -128 and maximo <=127 : 
                imagem_ = numpy.array(imagem_).astype("int8")
            elif minimo >= -32768 and maximo <= 32767 : 
                imagem_ = numpy.array(imagem_).astype("int16")
        
        return imagem_

    def procura_img_por_data(self, serie, data):
        img = None
        for i in range(len(serie)):
            data_i = serie.getDate_time(file=serie[i])
            if data_i == data:
                img = serie[i]
                break  
        return img
        