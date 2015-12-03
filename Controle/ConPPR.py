# -*- coding: utf-8 -*-
'''
Created on Nov 27, 2015

@author: rennan.paloschi
'''
from Controle import AbstractController
from Modelo.beans.SerialFileData import SerialTemporalFiles
from Modelo.Funcoes.BalancoHidrico.BHFAO import PPR
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
         
    def parametros_teste(self):
    
        self.serie_T = SerialTemporalFiles(root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\8-Diario\\tav")
        self.serie_T.prefixo = "tav_"  
        self.serie_T.date_mask = "%Y%m%d" 

        self.serie_PPR = SerialTemporalFiles(root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\PPR")
        self.serie_PPR.prefixo = "ppr_"  
        self.serie_PPR.date_mask = "%Y-%m-%d"      
         
    def executa(self):
        self.function = PPR.PPR()
        
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