'''
Created on Mar 6, 2015

@author: Paloschi
'''
from PyQt4.QtGui import QFileDialog, QMessageBox
from beans import Dados
from Operations import GetShapeData
from Operations import GetImageInformation
from Operations import Interpola
from Operations import SplitTable
import sys
from PyQt4 import QtCore, QtGui


class InterpoladorECMWF_Demo_Controller(object):
    '''
    classdocs
    '''
    ShapeSelected = None
    ImgRefSelected = None
    form = None

    def __init__(self):
        '''
        Constructor
        '''
    def btn_OK_ClickAction(self):
        print("OK")
        self.executar()
        
    def btn_Cancel_ClickAction(self):
        print("Cancel")
        sys.exit()
        
    def btn_FindShp_ClickAction(self):
        fname = QFileDialog.getOpenFileName()
        self.form.leShapePath.setText(fname)

    def btn_FindImgRef_ClickAction(self):
        fname = QFileDialog.getOpenFileName()
        self.form.leImgRefPath.setText(fname)

    def le_shapePath_ChangeAction(self):
        if (self.ShapeSelected == None):
            self.ShapeSelected = Dados.SimpleData(data = str(self.form.leShapePath.text()))
        else:
            self.ShapeSelected.data = self.form.leShapePath.text()
        
        getShapeProperties = GetShapeData.GetShapeData()
        getShapeProperties.data = self.ShapeSelected
        itens = getShapeProperties.getDataProperties().keys()
        self.form.cbAtribute.addItems(itens)
        self.form.cbAtribute.setEnabled(True)
        self.form.cbAtribute.setCurrentIndex(0)
        
    def le_imgRefPath_ChangeAction(self):
        if (self.ImgRefSelected == None):
            self.ImgRefSelected = Dados.SimpleData(data = self.form.leImgRefPath.text())
        else:
            self.ImgRefSelected.data = self.form.leImgRefPath.text()
        
    def cb_Atribute_ChangeAction(self):
        getShapeProperties = GetShapeData.GetShapeData()
        getShapeProperties.data = self.ShapeSelected
        itens = getShapeProperties.getDataProperties().keys()   
        itens.remove(self.form.cbAtribute.currentText())
        
        self.form.lwGroupAtributes.clear()
        
        for item in itens:
        
            item = QtGui.QListWidgetItem(item)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.form.lwGroupAtributes.addItem(item)
            
        self.form.lwGroupAtributes.setEnabled(True)
        __sortingEnabled = self.form.lwGroupAtributes.isSortingEnabled()
        self.form.lwGroupAtributes.setSortingEnabled(__sortingEnabled)
      
    
    def executar(self):
         
        getData = GetShapeData.GetShapeData()
        
        getData.data = self.ShapeSelected
        
        separador = SplitTable.SplitTable()   
        
        dados_separador = Dados.TableData()
        
        atributos = list()
        
        for index in xrange(self.form.lwGroupAtributes.count()):
            if self.form.lwGroupAtributes.item(index).checkState() == 2:
                atributos.append(str(self.form.lwGroupAtributes.item(index).text()))
        
        dados_separador.data = {'table' : getData, 'atributos' : atributos}
        
        separador.data = dados_separador
          
        dados_interpolador = Dados.TableData('tabela pro interpolador')
        
        getImageInformatio = GetImageInformation.GetImgInfo("Pegar informacoes da imagem modis")
        getImageInformatio.data = self.ImgRefSelected
        image_information = getImageInformatio.data
        
        dados_interpolador.data = {'table_data' : separador, 'atributo' : str(self.form.cbAtribute.currentText()), "format_image_data" : image_information}
        
        interpolador = Interpola.InterpolaTabela("teste ECMWF")
        interpolador.data = dados_interpolador

        mensagem  = interpolador.data
        
        #QtGui.QMessageBox("Informacao", mensagem, QMessageBox.Icon(), )
        