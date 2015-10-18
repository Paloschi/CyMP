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

class Controller(AbstractController.Controller):
    '''
    classdocs
    '''
    ShapeSelected = None
    ImgRefSelected = None
        
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
        self.print_text("Executando..")
        
        separador = SplitTable()   
        dados_separador = TableData()
        atributos = list()
        
        for index in xrange(self.ui.lwGroupAtributes.count()):
            if self.ui.lwGroupAtributes.item(index).checkState() == 2:
                atributos.append(str(self.ui.lwGroupAtributes.item(index).text()))
        
        dados_separador.data = {'table' : self.ShapeSelected.readVectorData(), 'atributos' : atributos}
        
        separador.data = dados_separador
          
        dados_interpolador = TableData()
        
        image_information = self.ImgRefSelected.getRasterInformation()
        
        dados_interpolador['table_data'] = separador
        dados_interpolador['atributo'] = str(self.ui.cbAtribute.currentText())
        dados_interpolador["format_image_data"] = image_information
        
        interpolador = Interpola.InterpolaTabela()
        
        interpolador.data = dados_interpolador

        mensagem  = interpolador.data
        
        

    def valida_form(self):
        return True
