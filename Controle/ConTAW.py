# -*- coding: utf-8 -*-
'''
Created on 11/11/2015

@author: Rennan
'''
from Controle import AbstractController
from Modelo.Funcoes.BalancoHidrico import Etc
from Modelo.beans.TableData import TableData
from Modelo.beans.SerialFileData import SerialTemporalFiles, SerialFile
import os.path as path
from Modelo.Funcoes.BalancoHidrico.BHFAO.TAW import TAW
from Modelo.beans.FileData import FileData
from Modelo.beans import RasterData

class Controller(AbstractController.Controller):
    
    serie_Zr = None
    serie_TAW = None
    
    def findImgCAD(self):
        self.findPath(self.ui.txImgCAD)

    def setSerieZr(self):
        imagens = self.getSerieTemporal(self.serie_Zr)
        if imagens is not None:
            self.serie_Zr = imagens
            self.ui.chZr.setCheckState(True)

    def setSerie_TAW(self):
        imagens = self.getSerieTemporal(self.serie_TAW)
        if imagens is not None:
            self.serie_TAW = imagens
            self.ui.chTAW.setCheckState(True)
            
    def habilitaPValue(self):
        if self.ui.chPValor.isChecked():
            self.ui.txPvalor.setEnabled(True)
        else:
            self.ui.txPvalor.setEnabled(False)
            
    
    def executa(self):

        self.function = TAW()
        
        parametros = TableData()
        parametros["CAD"] = RasterData.RasterFile(file_full_path=str(self.ui.txImgCAD.text()))
        parametros["Zr"] = self.serie_Zr
        parametros["TAW"] = self.serie_TAW
        
        if self.ui.chPValor.isChecked():
            parametros["p"] = float(self.ui.txPvalor.value())
        else:
            parametros["p"] = 1
            
        print ("controller: " + str(parametros["p"]))
        
        resultado = self.function.executar(parametros)
        
        if self.funcao_cancelada():
            self.console(u"Função interrompida")
            self.finalizar()
        elif resultado is not None:
            self.console(u"Função conluída")
            self.finalizar()

    def valida_form(self):
        if not path.exists(str(self.ui.txImgCAD.text())):
            self.message(u"Imagem CAD não encontrada.")
            return False
        if self.serie_Zr is None :
            self.message(u"Série de imagens Zr não configurada.")
            return False
        elif self.serie_TAW is None:
            self.message(u"Série de imagens TAW não configurada.")
            return False
        return True

    def parametros_teste(self):
        
        self.ui.txImgCAD.setText("C:\\CyMP\\Gafanhoto\\DADOS para Dr\\Imagens Cascavel\\CAD\\CAD.tif")
        
        root_path = "C:\\CyMP\\Gafanhoto\\DADOS para Dr\\Imagens Cascavel\\Zr"
        self.serie_Zr = SerialTemporalFiles()
        self.serie_Zr.root_path = root_path
        self.serie_Zr.prefixo = ""
        self.serie_Zr.mutiply_factor = 1
        self.serie_Zr.date_mask = "%Y-%m-%d"
        
        root_path = "C:\\CyMP\\Gafanhoto\\DADOS para Dr\\Imagens Cascavel\\RAW"
        self.serie_TAW = SerialTemporalFiles()
        self.serie_TAW.root_path = root_path
        self.serie_TAW.prefixo = "RAW_"
        self.serie_TAW.mutiply_factor = 1
        self.serie_TAW.date_mask = "%Y%m%d"
        
        self.ui.txPvalor.setValue(0.5)   
        