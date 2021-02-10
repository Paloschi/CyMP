# -*- coding: utf-8 -*-
'''
Created on 11/11/2015

@author: Rennan
'''
from Controle import AbstractController
from Modelo.beans.TableData import TableData
from Modelo.beans.SerialFileData import SerialTemporalFiles
from Modelo.beans import RasterData
from Modelo.Funcoes.BalancoHidrico.BHFAO.Ks import Ks

class Controller(AbstractController.Controller):
    
    serie_Ks = None
    serie_RAW = None
    serie_TAW = None
    serie_Dr = None

    def setSerieRAW(self):
        imagens = self.getSerieTemporal(self.serie_RAW)
        if imagens is not None:
            self.serie_RAW = imagens
            self.ui.chRAW.setCheckState(True)

    def setSerie_Ks(self):
        imagens = self.getSerieTemporal(self.serie_Ks)
        if imagens is not None:
            self.serie_Ks = imagens
            self.ui.chKs.setCheckState(True)

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
        self.function = Ks()
        
        parametros = TableData()
        parametros["RAW"] = self.serie_RAW
        parametros["TAW"] = self.serie_TAW
        parametros["Dr"] = self.serie_Dr
        parametros["Ks"] = self.serie_Ks
        
        resultado = self.function.executar(parametros)
        
        if self.funcao_cancelada():
            self.console(u"Função interrompida")
            self.finalizar()
        elif resultado is not None:
            self.console(u"Função conluída")
            self.finalizar()

    def valida_form(self):
        
        if self.serie_Ks == None :
            self.message(u"Série de imagens de Ks não configurada.")
            return False
        elif self.serie_RAW == None:
            self.message(u"Série de imagens de RAW não configurada.")
            return False
        elif self.serie_TAW == None:
            self.message(u"Série de imagens de TAW não configurada.")
            return False
        elif self.serie_Dr == None:
            self.message(u"Série de imagens de Dr não configurada.")
            return False
        return True

    def parametros_teste(self):
        root_path = "C:\\Data\\1-FAO ESTIMATION\\Ks"
        self.serie_Ks = SerialTemporalFiles()
        self.serie_Ks.root_path = root_path
        self.serie_Ks.prefixo = ""
        self.serie_Ks.date_mask = "%Y-%m-%d"     
        self.serie_Ks.mutiply_factor = 1
        
        root_path = "C:\\Data\\1-FAO ESTIMATION\\RAW"
        self.serie_RAW = SerialTemporalFiles()
        self.serie_RAW.root_path = root_path
        self.serie_RAW.prefixo = ""
        self.serie_RAW.mutiply_factor = 1
        self.serie_RAW.date_mask = "%Y-%m-%d"
        
        root_path = "C:\\Data\\1-FAO ESTIMATION\\TAW"
        self.serie_TAW = SerialTemporalFiles()
        self.serie_TAW.root_path = root_path
        self.serie_TAW.prefixo = ""
        self.serie_TAW.mutiply_factor = 1
        self.serie_TAW.date_mask = "%Y-%m-%d"
        
        root_path = "C:\\Data\\1-FAO ESTIMATION\\Dr"
        self.serie_Dr = SerialTemporalFiles()
        self.serie_Dr.root_path = root_path
        self.serie_Dr.prefixo = ""
        self.serie_Dr.mutiply_factor = 1
        self.serie_Dr.date_mask = "%Y-%m-%d"  
        