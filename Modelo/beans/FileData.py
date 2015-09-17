# -*- coding: utf-8 -*-
'''
Created on Jul 12, 2015

@author: Paloschi
'''

from AbstractData import ABData, FILE_DATA
import os

class FileData(ABData):
    '''
    Classe file data, essa classe abstrai um arquivo, e fornece algumas facilidades
    para manipular arquivos com mais praticidade
    '''
    __file_ext = None
    __file_path = None
    file_name = None
    
    def __init__(self, **params):
        
        super(FileData, self).__init__(FILE_DATA) # seta o tipo do objeto
        
        if params.get("data") != None : self.data = params.get("data")
        if params.get("ext") != None : self.file_ext = params.get("ext")
        if params.get("file_name") != None : self.file_name = params.get("file_name")
        if params.get("name") != None : self.name = params.get("name")
        if params.get("file_path") != None : self.file_path = params.get("file_path")
        if params.get("file_full_path") != None : self.file_full_path = params.get("file_full_path")
    
    @property
    def file_path(self):
        return self.__file_path
    
    @file_path.setter
    def file_path(self, data_path):
        self.__file_path = os.path.normpath(data_path) 
    
    @property
    def file_full_path(self):
        full_path = self.file_path + "\\" + self.file_name + "." + self.file_ext 
        return full_path
    
    @file_full_path.setter
    def file_full_path(self, file_full_path):
        full_path = os.path.normpath(file_full_path)
        name, ext = os.path.splitext(os.path.basename(full_path))
        self.file_name = name
        self.file_ext = ext
        self.__file_path = os.path.dirname(full_path)
        
    @property
    def file_ext(self):
        return self.__file_ext
    
    @file_ext.setter
    def file_ext(self, ext):
        ext = ext.replace(".", "")
        self.__file_ext = ext
            
        

