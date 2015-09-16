'''
Created on Mar 6, 2015

@author: Paloschi
'''
from PyQt4.QtGui import QFileDialog, QMessageBox
from Modelo.beans import TableData, FileData, VectorData
from Modelo.Funcoes.VectorTools import SplitTable
from Modelo.Funcoes.Interpoladores import Interpola
import sys
from PyQt4 import QtCore, QtGui
from Controle import AbstractController

class Controller(AbstractController.Controller):
    '''
    classdocs
    '''
    ShapeSelected = None
    ImgRefSelected = None
        
    def btn_OK_ClickAction(self):
        print("OK")
        self.executar()
        
    def btn_Cancel_ClickAction(self):
        print("Cancel")
        self.ui.close()
        
    def btn_FindShp_ClickAction(self):
        fname = QFileDialog.getOpenFileName()
        self.ui.leShapePath.setText(fname)

    def btn_FindImgRef_ClickAction(self):
        fname = QFileDialog.getOpenFileName()
        self.ui.leImgRefPath.setText(fname)

    def le_shapePath_ChangeAction(self):
        if (self.ShapeSelected == None):
            self.ShapeSelected = VectorData(file_full_path = self.ui.leShapePath.text())
        else:
            self.ShapeSelected.file_full_path = self.ui.leShapePath.text()
            
        itens = self.ShapeSelected.readVectorData().keys()
        self.ui.cbAtribute.addItems(itens)
        self.ui.cbAtribute.setEnabled(True)
        self.ui.cbAtribute.setCurrentIndex(0)
        
    def le_imgRefPath_ChangeAction(self):
        if (self.ImgRefSelected == None):
            self.ImgRefSelected = FileData(file_full_path = self.ui.leImgRefPath.text())
        else:
            self.ImgRefSelected.data = self.ui.leImgRefPath.text()
        
    def cb_Atribute_ChangeAction(self):

        itens = self.ShapeSelected.readVectorData.keys()   
        itens.remove(self.ui.cbAtribute.currentText())
        
        self.ui.lwGroupAtributes.clear()
        
        for item in itens:
        
            item = QtGui.QListWidgetItem(item)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.lwGroupAtributes.addItem(item)
            
        self.ui.lwGroupAtributes.setEnabled(True)
        __sortingEnabled = self.ui.lwGroupAtributes.isSortingEnabled()
        self.ui.lwGroupAtributes.setSortingEnabled(__sortingEnabled)
      
    
    def executar(self):
        
        separador = SplitTable()   
        
        dados_separador = TableData()
        
        atributos = list()
        
        for index in xrange(self.ui.lwGroupAtributes.count()):
            if self.ui.lwGroupAtributes.item(index).checkState() == 2:
                atributos.append(str(self.ui.lwGroupAtributes.item(index).text()))
        
        dados_separador.data = {'table' : self.ShapeSelected.readVectorData(), 'atributos' : atributos}
        
        separador.data = dados_separador
          
        dados_interpolador = TableData()
        
        image_information = self.ImgRefSelected.readVectorData()
        
        dados_interpolador.data = {'table_data' : separador, 'atributo' : str(self.ui.cbAtribute.currentText()), "format_image_data" : image_information}
        
        interpolador = Interpola.InterpolaTabela("teste ECMWF")
        interpolador.data = dados_interpolador

        mensagem  = interpolador.data
        
        

    def valida_form(self):
        pass
    def executa(self):
        pass
