# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2015

@author: Paloschi
'''
from PyQt4.QtGui import QFileDialog
from Modelo.Funcoes.BalancoHidrico import ExtratorSemeaduraColheita
from Modelo.beans import FileData, SerialFile, TableData
from PyQt4 import QtCore
from Controle import AbstractController
from numpy import double

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
class Controller(AbstractController.Controller):
    
    def findInFolder(self):
        self.findPath(self.ui.leInFolder, "folder")
        
    def findOutFolder(self):
        self.findPath(self.ui.leOutFolder, "folder")
  
    def executa(self):
        
        extractor = ExtratorSemeaduraColheita()
        
        root_out = self.ui.leOutFolder.text()
        
        extractor.data = self.carregarParamIN()
        
        imagens = extractor.data
        
        semeadura = imagens["imagem_semeadura"]
        semeadura.data_name = self.ui.leImgSemeadura.text()
        colheita = imagens["imagem_colheita"]
        colheita.data_name = self.ui.leImgColheita.text()
        pico = imagens["imagem_pico"]
        pico.data_name = self.ui.leImgPico.text()
        
        semeadura.saveImage(root_out, ext=".tif")
        colheita.saveImage(root_out, ext=".tif")
        pico.saveImage(root_out, ext=".tif")
        
        
    def carregarParamIN(self):

        
        parametrosIN = TableData()
        
        root_in = self.ui.leInFolder.text()
        
        images = SerialFile(root_path=root_in)
        
        parametrosIN["images"] = images
        parametrosIN["avanco_semeadura"] = double(self.ui.dspASemeadura.value())
        parametrosIN["avanco_colheita"] = double(self.ui.dsbAColheita.value())
        parametrosIN["intervalo_pico"] = self.ui.lePPico.text()
        parametrosIN["intervalo_semeadura"] = self.ui.lePSemeadura.text()
        parametrosIN["intervalo_colheita"] = self.ui.lePColheita.text()
        parametrosIN["null_value"] = double(self.ui.leNullValue.text())

        return parametrosIN

    def valida_form(self):
        '''
        Esse método tem que existir nas classes controladoras
        aqui serão feitas todas as validações do form    
        '''
        return True
