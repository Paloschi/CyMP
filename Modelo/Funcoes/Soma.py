# -*- coding: utf-8 -*-

'''
Created on Jan 21, 2015
@author: Paloschi
'''

from Modelo.beans import Dados
from Modelo.Funcoes import AbstractFunction

class RasterToCSVeVRT(AbstractFunction.Function):
    '''
    Operacao de soma de mapas
    '''
    def __setParamIN__(self):

        self.descriptionIN["numero1"] = "um numero"
        self.descriptionIN["numero2"] = "outro numero"
        
    def __setParamOUT__(self):
        self.descriptionOUT["resultado"] = "Soma de saída"  
        
    def __execOperation__(self):
        soma = self.paramentrosIN_carregados["numero1"] + self.paramentrosIN_carregados["numero2"]
        return soma
    
    
#params = Dados.TableData()

#params["numero1"] = Dados.SimpleData(data=1)
#params["numero2"] = Dados.SimpleData(data=2)

#fsoma = RasterToCSVeVRT(params)

#print (fsoma.data) 