# -*- coding: utf-8 -*-
'''
Created on Mar 6, 2015

@author: Paloschi
'''
from PyQt4.QtGui import QFileDialog, QMessageBox
from Modelo.beans import TableData, FileData, VectorFile, RasterFile
from Modelo.Funcoes.VectorTools import SplitTable
from Modelo.Funcoes.Interpoladores import Interpola
import sys
from PyQt4 import QtCore, QtGui
from Controle import AbstractController
import os.path

class Controller(AbstractController.Controller):
    '''
    classdocs
    '''
    ShapeSelected = None
    ImgRefSelected = None
    
    def inicializar(self):
        
        self.ui.leImgRefPath.setText("C:\\Gafanhoto WorkSpace\\DataTestes\\raster\\semeadura_soja_11-12.tif")
        self.ui.leShapePath.setText("C:\\Gafanhoto WorkSpace\\DataTestes\\shape\\Contorno_Agassis_Pontos_2015.shp")
        
    def btn_FindShp_ClickAction(self):
        self.findPath(self.ui.leShapePath)

    def btn_FindImgRef_ClickAction(self):
        self.findPath(self.ui.leImgRefPath)

    def le_shapePath_ChangeAction(self):
        if (self.ShapeSelected == None):
            text = str(self.ui.leShapePath.text())
            self.ShapeSelected = VectorFile(file_full_path = text)
        else:
            self.ShapeSelected.file_full_path = self.ui.leShapePath.text()
            
        itens = self.ShapeSelected.readVectorData()["properties"].keys()
        self.ui.cbAtribute.addItems(itens)
        self.ui.cbAtribute.setEnabled(True)
        self.ui.cbAtribute.setCurrentIndex(0)
        
    def le_imgRefPath_ChangeAction(self):
        if (self.ImgRefSelected == None):
            self.ImgRefSelected = RasterFile(file_full_path = str(self.ui.leImgRefPath.text()))
        else:
            self.ImgRefSelected.file_full_path = str(self.ui.leImgRefPath.text())
        
    def cb_Atribute_ChangeAction(self):
        
        itens = self.ShapeSelected.readVectorData()["properties"].keys()   
        
        itens.remove(self.ui.cbAtribute.currentText())
        
        self.ui.lwGroupAtributes.clear()
        
        for item in itens:
        
            item = QtGui.QListWidgetItem(item)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.lwGroupAtributes.addItem(item)
            
        self.ui.lwGroupAtributes.setEnabled(True)
        __sortingEnabled = self.ui.lwGroupAtributes.isSortingEnabled()
        self.ui.lwGroupAtributes.setSortingEnabled(__sortingEnabled)
      
    def executa(self):
        
        print "executando.."
        
        self.function = Interpola.InterpolaTabela()
        self.function.console = self.print_text
        
        self.print_text("Executando..")
        
        separador = SplitTable()   
        dados_separador = TableData()
        atributos = list()
        
        for index in xrange(self.ui.lwGroupAtributes.count()):
            if self.ui.lwGroupAtributes.item(index).checkState() == 2:
                atributos.append(str(self.ui.lwGroupAtributes.item(index).text()))
        
        
        vector_table = self.ShapeSelected.readVectorData()
        
        dados_separador.data = {'table' : vector_table, 'atributos' : atributos}
        dados_separador.data["data_path"] = self.ui.leShapePath.text()
        
          
        dados_interpolador = TableData()
        image_information = self.ImgRefSelected.getRasterInformation()

        dados_interpolador['table_data'] = dados_separador
        dados_interpolador['atributo'] = str(self.ui.cbAtribute.currentText())
        dados_interpolador["format_image_data"] = image_information

        
        self.print_text("Interpolando")
        
        mensagem = self.function.executar(dados_interpolador)
        self.finalizar()
        

    def valida_form(self):
        if self.ShapeSelected is None:
            self.message(u"Shape para interpolação não encontrado.")
            return False   
        if self.ImgRefSelected is None:
            self.message(u"Imagem de referencia não encontrada.")
            return False   
        return True
    
