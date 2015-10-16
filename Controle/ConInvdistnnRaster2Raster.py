# -*- coding: utf-8 -*-
'''
Created on 13/10/2015

@author: Rennan
'''
from Modelo.Funcoes.RasterTools import RasterToCSVeVRT
from Modelo.Funcoes.Interpoladores import IDW
from Modelo.beans import SerialFile, TableData
from PyQt4 import QtCore
from Controle import AbstractController
from numpy import double
import os.path
from Modelo.beans.RasterData import RasterFile

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Controller(AbstractController.Controller):
    '''
    classdocs
    
    '''
    def findInFolder(self):
        self.findPath(self.ui.txInFolder, "folder")
        
    def findOutFolder(self):
        self.findPath(self.ui.txOutFolder, "folder")
  
    def findImgRef(self):
        self.findPath(self.ui.txImgReference)

    def valida_form(self):
        if not os.path.exists(self.ui.txInFolder.text()):
            self.message(u"Pasta de entrada das imagens não encontrada, verifique o endereço.")
            return False   
        if not os.path.exists(self.ui.txOutFolder.text()):
            self.message(u"Pasta de saida das imagens não encontrada, verifique o endereço.")
            return False
        if not os.path.exists(self.ui.txImgReference.text()):
            self.message(u"Imagem de referencia das imagens não encontrada, verifique o endereço.")
            return False     
        return True

    def executa(self):
        
        self.function = RasterToCSVeVRT()
        
        paramIn = dict()
        paramIn["images"] = SerialFile(root_path=self.ui.txInFolder.text())
        paramIn["out_folder"] = self.ui.txOutFoldertext()
        
        CSVs, VRTs = self.function.executar(paramIn)
        
        for i in len(range(CSVs)):
            
            conf_algoritimo = dict()
            conf_algoritimo["power"] = double(self.ui.txPower.text())
            conf_algoritimo["radius"] = double(self.ui.txRadius.text())
            conf_algoritimo["max_points"] = double(self.ui.txMaxPoint.text())
            conf_algoritimo["min_points"] = double(self.ui.txMinPoint.text())
            
            conf_img_out = RasterFile(file_full_path=self.ui.txImgReference.text()).getRasterInformation()
            
            img_out = RasterFile(file_full_path=VRTs[i].file_full_path)
            img_out.ext = "tif"           
            
            paramIn = dict()
            paramIn["csv"] = CSVs[i]
            paramIn["vrt"] = VRTs[i]
            paramIn["img_out"] = img_out
            paramIn["conf_algoritimo"] = conf_algoritimo
            paramIn["img_out"] = img_out
            
            self.function = IDW()
            imagem_interpolada = self.function.executar(paramIn)


            
            
            
            
            
            
            
            
            
