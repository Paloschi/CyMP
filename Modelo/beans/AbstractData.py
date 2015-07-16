'''
Created on Jul 14, 2015

@author: Paloschi
'''
from abc import ABCMeta

FILE_DATA = 1
SERIAL_FILE_DATA = 2
TABLE_DATA = 3
FUNCTION_DATA = 4

class ABData(object):
    '''
    classdocs
    '''
    
    name = None
    file_name = None
    __data_type = None
    __metaclass__ = ABCMeta
    
    def __init__(self, data_type):
        self.__data_type = data_type
        
    @property    
    def data_type(self):
        return self._data_type
    
    @data_type.setter
    def data_type(self, param):
        pass