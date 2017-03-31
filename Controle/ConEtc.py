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
    
    etc = True
    
    def MudaPraETc(self):
        self.ui.label_5.setText(u"Imagens diárias de ETc")
        self.ui.label_2.setText(u"Imagens diárias de ET0")
        self.ui.label_3.setText(u"Imagens diárias de Kc")
        self.etc = True
    
    def MudaPraETa(self):
        self.ui.label_5.setText(u"Imagens diárias de ETa")
        self.ui.label_2.setText(u"Imagens diárias de Ks")
        self.ui.label_3.setText(u"Imagens diárias de ETc")
        self.etc = False

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
            self.finalizar()
        elif resultado is not None:
            self.console(u"Função conluída")
            self.finalizar()

    def valida_form(self):
        
        if self.etc :
            if self.serie_ET0 is None :
                self.message(u"Série de imagens de ET0 não configurada.")
                return False
            elif self.serie_Kc is None:
                self.message(u"Série de imagens de Kc não configurada.")
                return False
            elif self.serie_ETc is None:
                self.message(u"Série de imagens de ETc não configurada.")
                return False
        else :
            if self.serie_ET0 is None :
                self.message(u"Série de imagens de Etc não configurada.")
                return False
            elif self.serie_Kc is None:
                self.message(u"Série de imagens de Ks não configurada.")
                return False
            elif self.serie_ETc is None:
                self.message(u"Série de imagens de ETa não configurada.")
                return False           
        return True

    def parametros_teste(self):
        root_path = "C:\\CyMP\\Gafanhoto\\DADOS para Dr\\Imagens Cascavel\\ECMWF\\ET0_diario"
        self.serie_ET0 = SerialTemporalFiles()
        self.serie_ET0.root_path = root_path
        self.serie_ET0.prefixo = "evpt_diario_"
        self.serie_ET0.mutiply_factor = 1
        self.serie_ET0.date_mask = "%Y-%m-%d"
        
        root_path = "C:\\CyMP\\Gafanhoto\\DADOS para Dr\\Imagens Cascavel\\Kc"
        self.serie_Kc = SerialTemporalFiles()
        self.serie_Kc.root_path = root_path
        self.serie_Kc.prefixo = ""
        self.serie_Kc.mutiply_factor = 1
        self.serie_Kc.date_mask = "%Y-%m-%d"
        
        root_path = "C:\\CyMP\\Gafanhoto\\DADOS para Dr\\Imagens Cascavel\\ETc"
        self.serie_ETc = SerialTemporalFiles()
        self.serie_ETc.root_path = root_path
        self.serie_ETc.prefixo = "ETc_"
        self.serie_ETc.date_mask = "%Y%m%d"    
        self.serie_ETc.mutiply_factor = 1   
        