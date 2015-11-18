'''
Created on Nov 18, 2015

@author: rennan.paloschi
'''

from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA
import threading
import numpy
from Modelo.beans.RasterData import RasterFile

class Eta(AbstractFunction):
    
        def __setParamIN__(self):
        
        self.descriptionIN["RAW"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"S�rie de imagem RAW"}
        self.descriptionIN["TAW"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"S�rie de imagens TAW"}
        self.descriptionIN["Dr"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"S�rie de imagem Dr"}
        self.descriptionIN["Ks"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"S�rie de imagem Ks"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["Ks"] = {"Type":SERIAL_FILE_DATA, "Description":"S�rie de imagen Ks"}
    
    def __execOperation__(self):
