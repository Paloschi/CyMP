# -*- coding: utf-8 -*-
'''
Created on 11/11/2015

@author: Rennan
'''
from Controle import AbstractController
from Modelo.Funcoes.BalancoHidrico import Etc
from Modelo.beans.TableData import TableData
from Modelo.beans.SerialFileData import SerialTemporalFiles

class Controller(AbstractController.Controller):
    
    serie_ET0 = None
    serie_ETc = None
    serie_Kc = None

    def setSerieET0(self):
        imagens = self.getSerieTemporal(self.serie_ET0)
        if imagens is not None:
            self.serie_ET0 = imagens
            self.ui.chET0.setCheckState(True)

    def setSerie_ETc(self):
        imagens = self.getSerieTemporal(self.serie_ETc)
        if imagens is not None:
            self.serie_ETc = imagens
            self.ui.chETc.setCheckState(True)

    def setSerie_Kc(self):
        imagens = self.getSerieTemporal(self.serie_Kc)
        if imagens is not None:
            self.serie_Kc = imagens
            self.ui.chKc.setCheckState(True)
    
    def executa(self):
        self.function = Etc()
        
        parametros = TableData()
        parametros["ET0"] = self.serie_ET0
        parametros["Kc"] = self.serie_Kc
        parametros["ETc"] = self.serie_ETc
        
        resultado = self.function.executar(parametros)
        
        if self.funcao_cancelada():
            self.console(u"Função interrompida")
        elif resultado is not None:
            self.console(u"Função conluída")
            self.finalizar()

    def valida_form(self):
        if self.serie_ET0 is None :
            self.message(u"Série de imagens de ET0 não configurada.")
            return False
        elif self.serie_Kc is None:
            self.message(u"Série de imagens de Kc não configurada.")
            return False
        elif self.serie_ETc is None:
            self.message(u"Série de imagens de ETc não configurada.")
            return False
        return True

    def parametros_teste(self):
        root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\8-Diario\\EVPT"
        self.serie_ET0 = SerialTemporalFiles()
        self.serie_ET0.root_path = root_path
        self.serie_ET0.prefixo = "evpt_diario_"
        self.serie_ET0.mutiply_factor = 0.01
        self.serie_ET0.date_mask = "%Y-%m-%d"
        
        root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\Kc_distribuido\\soltas"
        self.serie_Kc = SerialTemporalFiles()
        self.serie_Kc.root_path = root_path
        self.serie_Kc.prefixo = ""
        self.serie_Kc.mutiply_factor = 0.01
        self.serie_Kc.date_mask = "%Y-%m-%d"
        
        root_path = "C:\\Gafanhoto WorkSpace\\DataTestes\\out\\Primeira tentativa"
        self.serie_ETc = SerialTemporalFiles()
        self.serie_ETc.root_path = root_path
        self.serie_ETc.prefixo = "teste_etc_"
        self.serie_ETc.date_mask = "%Y%m%d"        
        