# -*- coding: utf-8 -*-
'''
Created on 11/11/2015

@author: Rennan
'''
from Controle import AbstractController
from Modelo.beans.TableData import TableData
from Modelo.beans.SerialFileData import SerialTemporalFiles
from Modelo.Funcoes.BalancoHidrico.BHFAO.Dr import Dr
import os.path as path
from Modelo.beans import RasterData

class Controller(AbstractController.Controller):
    
    serie_ETc = None
    serie_PPP = None
    serie_TAW = None
    serie_Dr = None

    def findImgCAD(self):
        self.findPath(self.ui.txImgCAD)

    def setSeriePPP(self):
        imagens = self.getSerieTemporal(self.serie_PPP)
        if imagens is not None:
            self.serie_PPP = imagens
            self.ui.chPPP.setCheckState(True)

    def setSerie_ETc(self):
        imagens = self.getSerieTemporal(self.serie_ETc)
        if imagens is not None:
            self.serie_ETc = imagens
            self.ui.chETc.setCheckState(True)

    def setSerie_TAW(self):
        imagens = self.getSerieTemporal(self.serie_TAW)
        if imagens is not None:
            self.serie_TAW = imagens
            self.ui.chTAW.setCheckState(True)

    def setSerie_Dr(self):
        imagens = self.getSerieTemporal(self.serie_Dr)
        if imagens is not None:
            self.serie_Dr = imagens
            self.ui.chDr.setCheckState(True)
    
    def executa(self):
        self.function = Dr()
        
        parametros = TableData()
        parametros["Etc"] = self.serie_ETc
        parametros["PPP"] = self.serie_PPP
        parametros["TAW"] = self.serie_TAW
        parametros["Dr"] = self.serie_Dr
        parametros["CAD"] = RasterData.RasterFile(file_full_path=str(self.ui.txImgCAD.text()))
        
        resultado = self.function.executar(parametros)
        
        if self.funcao_cancelada():
            self.console(u"Função interrompida")
            self.finalizar()
        elif resultado is not None:
            self.console(u"Função conluída")
            self.finalizar()

    def valida_form(self):
        if self.serie_ETc == None :
            self.message(u"Série de imagens de ETc não configurada.")
            return False
        elif self.serie_PPP == None:
            self.message(u"Série de imagens de PPP não configurada.")
            return False
        elif self.serie_TAW == None:
            self.message(u"Série de imagens de TAW não configurada.")
            return False
        elif self.serie_Dr == None:
            self.message(u"Série de imagens de Dr não configurada.")
            return False
        elif not path.exists(str(self.ui.txImgCAD.text())):
            self.message(u"Imagem CAD não encontrada.")
            return False
        return True

    def parametros_teste(self):
        root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\ETc\\ETC_soltas"
        self.serie_ETc = SerialTemporalFiles()
        self.serie_ETc.root_path = root_path
        self.serie_ETc.prefixo = "etc_"
        self.serie_ETc.date_mask = "%Y-%m-%d"     
        self.serie_ETc.mutiply_factor = 0.01
        
        root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\8-Diario\\PPP"
        self.serie_PPP = SerialTemporalFiles()
        self.serie_PPP.root_path = root_path
        self.serie_PPP.prefixo = "rain_diario_"
        self.serie_PPP.mutiply_factor = 0.01
        self.serie_PPP.date_mask = "%Y-%m-%d"
        
        root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\TAW\\soltas"
        self.serie_TAW = SerialTemporalFiles()
        self.serie_TAW.root_path = root_path
        self.serie_TAW.prefixo = "TAW_"
        self.serie_TAW.mutiply_factor = 1
        self.serie_TAW.date_mask = "%Y%m%d"
        
        self.ui.txImgCAD.setText("C:\\Gafanhoto WorkSpace\\Soja11_12\\Mapa_solo\\soloVSMascaraSoja11_12.tif")
        
        root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\Dr"
        self.serie_Dr = SerialTemporalFiles()
        self.serie_Dr.root_path = root_path
        self.serie_Dr.prefixo = "dr_"
        self.serie_Dr.mutiply_factor = 100

        self.serie_Dr.date_mask = "%Y-%m-%d"  
        