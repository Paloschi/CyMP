# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2015

@author: Paloschi
'''

from Modelo.Funcoes.BalancoHidrico import ExtratorSemeaduraColheita
from Modelo.beans import SerialFile, TableData
from PyQt4 import QtCore
from Controle import AbstractController
from numpy import double
import os.path

#try:
#    _fromUtf8 = QtCore.QString.fromUtf8
#except AttributeError:
#    def _fromUtf8(s):
#        return s
    
class Controller(AbstractController.Controller):
    
    def findInFolder(self):
        self.findPath(self.ui.leInFolder, "folder")
        
    def findOutFolder(self):
        self.findPath(self.ui.leOutFolder, "folder")
  
    def executa(self):
        
        self.function = ExtratorSemeaduraColheita()
        
        root_out = str(self.ui.leOutFolder.text())
        root_in = str(self.ui.leInFolder.text())
        
        parametrosIN = TableData()
        images = SerialFile(root_path=root_in)
        parametrosIN["images"] = images
        parametrosIN["avanco_semeadura"] = double(self.ui.dspASemeadura.value())
        parametrosIN["avanco_colheita"] = double(self.ui.dsbAColheita.value())
        parametrosIN["intervalo_pico"] = str(self.ui.lePPico.text())
        parametrosIN["intervalo_semeadura"] = str(self.ui.lePSemeadura.text())
        parametrosIN["intervalo_colheita"] = str(self.ui.lePColheita.text())
        parametrosIN["null_value"] = double(self.ui.leNullValue.text())
        parametrosIN["prefixo"] = str(self.ui.lePrefixo.text())
        parametrosIN["sufixo"] = str(self.ui.leSufixo.text())
        parametrosIN["mask"] = str(self.ui.leMascara.text())
        
        images = self.function.executar(parametrosIN)
        
        semeadura = images["imagem_semeadura"]
        semeadura.file_name = self.ui.leImgSemeadura.text()
        semeadura.file_path = "C://Gafanhoto WorkSpace//DataTestes//out"
        semeadura.file_ext = "tif"
        semeadura.saveRasterData()
        
        colheita = images["imagem_colheita"]
        colheita.file_name = self.ui.leImgColheita.text()
        colheita.file_path = "C://Gafanhoto WorkSpace//DataTestes//out"
        colheita.file_ext = "tif"
        colheita.saveRasterData()
        
        pico = images["imagem_pico"]
        pico.file_name = self.ui.leImgPico.text()
        pico.file_path = "C://Gafanhoto WorkSpace//DataTestes//out"
        pico.file_ext = "tif"
        pico.saveRasterData()

    def valida_form(self):
        '''
        Esse método tem que existir nas classes controladoras
        aqui serão feitas todas as validações do form    
        '''

        if not os.path.exists(self.ui.leInFolder.text()):
            self.message(u"Pasta de entrada das imagens não encontrada, verifique o endereço.")
            return False   
        if not os.path.exists(self.ui.leOutFolder.text()):
            self.message(u"Pasta de saida das imagens não encontrada, verifique o endereço.")
            return False    
        if str(self.ui.lePPico.text()) == "" : 
            self.message(u"Preencha o intervalo para as imagens de pico (ex.: 10-20).")
            return False
        if str(self.ui.lePSemeadura.text()) == "" : 
            self.message(u"Preencha o intervalo para as imagens de semeadura (ex.: 20-30).")
            return False
        if str(self.ui.lePColheita.text()) == "" : 
            self.message(u"Preencha o intervalo para as imagens de colheita (ex.: 30-40).")
            return False
        if str(self.ui.leMascara.text())  == "" : 
            self.message(u"É necessário informar uma máscara, (ex.: %Y%m%d).")
            return False    
        if not os.path.exists(self.ui.leImgSemeadura.text()):
            self.message(u"Imagem de semeadura não encontrada, verifique o endereço.")
            return False
        if not os.path.exists(self.ui.leImgColheita.text()):
            self.message(u"Imagem de colheita não encontrada, verifique o endereço.") 
            return False         
        if not os.path.exists(self.ui.leImgPico.text()):
            self.message(u"Imagem de pico não encontrada, verifique o endereço.") 
            return False    
        return True
