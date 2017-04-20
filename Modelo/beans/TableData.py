# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2015

@author: Paloschi
'''

from Modelo.beans.AbstractData import ABData, TABLE_DATA

class TableData(ABData, dict):
    '''
    Classe criada pra guardar diversos tipos de valores, é só pra dar uma organizad 
    '''

    def __init__(self, name=None):
        super(self.__class__, self).__init__(TABLE_DATA)
        self.name = name
