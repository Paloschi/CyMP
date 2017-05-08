# -*- coding: utf-8 -*-

'''
Created on Jun 10, 2015

@author: Paloschi
'''
from PyQt4.QtGui import QFileDialog
from Modelo.Funcoes.Filtros import FiltroSavitz
from Modelo.beans import TableData, SerialFile
from PyQt4 import QtCore
from Controle import AbstractController
import os

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
        
        self.function = FiltroSavitz()
        
        self.function.console = self.print_text
        
        self.print_text(u"Inicializando filtro.")
        
        root_out = self.ui.leOutFolder.text()
        root_out = _fromUtf8(str(root_out) + "\\")
        root_out = str(root_out).replace("\\", "/")
        
        parametrosIn = self.carregarParamIN()
        
        self.print_text(u"Filtrando imagens...")
        imagens_filtradas = self.function.executar(parametrosIn)
        
        if self.funcao_cancelada() : return None
        elif imagens_filtradas == None :
            self.print_text(u"Erro desconhecido.")
            self.finalizar()
        else :
            imagens_filtradas.saveListByRoot(root_path=root_out, ext="tif") 
            self.print_text(u"Função concluída")
            self.finalizar()
        
    def carregarParamIN(self):
        
        images = SerialFile()
        parametrosIN = TableData()
        root_in = self.ui.leInFolder.text()
        root_in = _fromUtf8(str(root_in) + "\\")
        root_in = str(root_in).replace("\\", "/")

        images.loadListByRoot(root_in)
        self.print_text(u"Numero de imagens encontradas:" + str(len(images)))
        
        parametrosIN["images"] = images
        
        conf_algoritimo = TableData()
        conf_algoritimo["window_size"] = self.ui.leWindowSize.text()
        conf_algoritimo["order"] = self.ui.leOrdem.text()
        #if self.ui.checkBox.isChecked() : conf_algoritimo["null_value"] = double(self.ui.leNullValue.text())
        #else : conf_algoritimo["null_value"] = FileData(data= None)
        
        parametrosIN["conf_algoritimo "] = conf_algoritimo
        
        return parametrosIN
    
    def valida_form(self):
        
        if not os.path.exists(self.ui.leInFolder.text()):
            self.message(u"Pasta de entrada das imagens não encontrada, verifique o endereço.")
            return False   
        if not os.path.exists(self.ui.leOutFolder.text()):
            self.message(u"Pasta de saida das imagens não encontrada, verifique o endereço.")
            return False 
        return True
    
    def parametros_teste(self):
        self.ui.leInFolder.setText("Dados\\1-Tratamento de dados\\3-Indice de Vegetacao EVI\\1- EVI Modis recortado")
        self.ui.leOutFolder.setText("Dados\\1-Tratamento de dados\\3-Indice de Vegetacao EVI\\2- EVI Modis filtrado")
        