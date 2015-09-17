'''
Created on Sep 17, 2015

@author: rennan.paloschi
'''

from Modelo.Funcoes import AbstractFunction
from Modelo.beans import FILE_DATA, TABLE_DATA

class RasterCuterTool(AbstractFunction):
    '''
    Corta um raster
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    
    def __setParamIN__(self):
        self.descriptionIN["image"] = {"Required":True, "Type":FILE_DATA, "Description":"Imagem a ser cortada"}
        self.descriptionIN["out_full_path"] = {"Required":True, "Type":None, "Description":"Endereço completo para saida da imagem"}
        
        cut_description = dict()
        cut_description["xmin"] = {"Required":True, "Type":None, "Description":u"posição inicial x"}
        cut_description["xmax"] = {"Required":True, "Type":None, "Description":u"posição final x"}
        cut_description["ymin"] = {"Required":True, "Type":None, "Description":u"posição inicial y"}
        cut_description["ymax"] = {"Required":True, "Type":None, "Description":u"posição final y"}
        
        self.descriptionIN["img_out_config"] =  {"Required":True, "Type":TABLE_DATA, "Table_Description":cut_description, "Description":"configuração do corte"}
        
    def __setParamOUT__(self):
        self.descriptionOUT["CSVs"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"lista de arquivos CSV"}
        self.descriptionOUT["VRTs"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"lista de arquivos vrt"}    
        
        