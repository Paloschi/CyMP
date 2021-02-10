# -*- coding: utf-8 -*-
'''
Created on Nov 27, 2015

@author: rennan.paloschi
'''
from Controle import AbstractController
from Modelo.beans.SerialFileData import SerialTemporalFiles
from Modelo.Funcoes.BalancoHidrico.BHFAO import PPR, PPR_Parallel
from Modelo.beans.TableData import TableData

class Controller(AbstractController.Controller):

    serie_T = None
    serie_PPR = None
    
    def setSerieT(self):
        imagens = self.getSerieTemporal(self.serie_T)
        if imagens is not None:
            self.serie_T = imagens
            self.ui.chT.setCheckState(True)

    def setSeriePPR(self):
        imagens = self.getSerieTemporal(self.serie_PPR)
        if imagens is not None:
            self.serie_PPR = imagens
            self.ui.chPPR.setCheckState(True)
         
    def executa(self):
        self.function = PPR_Parallel.PPR()
        
        param = TableData()
        param["T"] = self.serie_T
        param["PPR"] = self.serie_PPR
        param["Cc"] = self.ui.txCc.value()
        
        resultado = self.function.executar(param)
           
        if self.funcao_cancelada():
            self.console(u"Função interrompida")
            self.finalizar()
        elif resultado is not None:
            self.console(u"Função conluída")
            self.finalizar()
    
    def valida_form(self):
        if self.serie_T == None :
            self.message(u"Série de imagens de Temperatura média não configurada.")
            return False
        elif self.serie_PPR == None:
            self.message(u"Série de imagens de PPR não configurada.")
            return False
        return True

    def parametros_teste(self):

        self.serie_T = SerialTemporalFiles(root_path="C:\\Data\\1-FAO ESTIMATION\\temperature")
        self.serie_T.prefixo = ""
        self.serie_T.date_mask = "%Y-%m-%d"
        self.serie_T.mutiply_factor = 1

        self.serie_PPR = SerialTemporalFiles(root_path="C:\\Data\\1-FAO ESTIMATION\\ppb")
        self.serie_PPR.prefixo = ""
        self.serie_PPR.date_mask = "%Y-%m-%d"
        self.serie_PPR.mutiply_factor = 1

        #self.ui.txCc.setValue(0.35599427)
        self.ui.txCc.setValue(0.2795)  # Tirado do artigo http://www.dsr.inpe.br/sbsr2015/files/p0690.pdf

