# -*- coding: utf-8 -*-
'''
Created on 03/12/2015

@author: Paloschi
'''
from Controle import AbstractController
from Modelo.Funcoes.BalancoHidrico.BHFAO.Ya import Ya
from Modelo.beans.TableData import TableData
from Modelo.beans.SerialFileData import SerialTemporalFiles

class Controller(AbstractController.Controller):
    
    serie_ETa = None
    serie_ETc = None
    serie_Yx = None
    serie_Ya = None
    serie_Kc = None
    
    def setSerie_ETa(self):
        imagens = self.getSerieTemporal(self.serie_ETa)
        if imagens is not None:
            self.serie_ETa = imagens
            self.ui.chETa.setCheckState(True)

    def setSerie_ETc(self):
        imagens = self.getSerieTemporal(self.serie_ETc)
        if imagens is not None:
            self.serie_ETc = imagens
            self.ui.chETc.setCheckState(True)

    def setSerie_Yx(self):
        imagens = self.getSerieTemporal(self.serie_Yx)
        if imagens is not None:
            self.serie_Yx = imagens
            self.ui.chYx.setCheckState(True)

    def setSerie_Ya(self):
        imagens = self.getSerieTemporal(self.serie_Ya)
        if imagens is not None:
            self.serie_Ya = imagens
            self.ui.chYa.setCheckState(True)
            
    def setSerie_Kc(self):
        imagens = self.getSerieTemporal(self.serie_Kc)
        if imagens is not None:
            self.serie_Kc = imagens
            self.ui.chKc.setCheckState(True)

    def executa(self):
        self.function = Ya()
        
        param = TableData()
        
        param["ETa"] = self.serie_ETa
        param["ETc"] = self.serie_ETc
        param["Ky"] = self.ui.txKy.value()
        param["Yx"] = self.serie_Yx
        param["Ya"] = self.serie_Ya
        param["Kc"] = self.serie_Kc
        
        resultado = self.function.executar(param)
        
        if self.funcao_cancelada():
            self.console(u"Função interrompida")
            self.finalizar()
        elif resultado is not None:
            self.console(u"Função conluída")
            
            self.finalizar()
    
    def valida_form(self):
        if self.serie_ETa == None :
            self.message(u"Série de imagens de ETa não configurada.")
            return False
        elif self.serie_ETc == None:
            self.message(u"Série de imagens de ETc não configurada.")
            return False
        elif self.serie_Yx == None:
            self.message(u"Série de imagens de Yx não configurada.")
            return False
        elif self.serie_Ya == None:
            self.message(u"Série de imagens de Ya não configurada.")
            return False
        return True
    
    def parametros_teste(self):


        self.serie_ETa = SerialTemporalFiles(root_path="C:\\CyMP\\Gafanhoto\\DADOS\\Imagens Cascavel\\ETa")
        self.serie_ETa.prefixo = "ETa_"
        self.serie_ETa.date_mask = "%Y%m%d"
        self.serie_ETa.mutiply_factor = 1
        
        self.serie_ETc = SerialTemporalFiles(root_path="C:\\CyMP\\Gafanhoto\\DADOS\\Imagens Cascavel\\ETc")
        self.serie_ETc.prefixo = "ETc_"
        self.serie_ETc.date_mask = "%Y%m%d"
        self.serie_ETc.mutiply_factor = 1
        
        self.serie_Yx = SerialTemporalFiles(root_path="C:\\CyMP\\Gafanhoto\\DADOS\\Imagens Cascavel\\PPB")
        self.serie_Yx.prefixo = "ppb_"
        self.serie_Yx.date_mask = "%Y%m%d"
        self.serie_Yx.mutiply_factor = 1
        
        self.serie_Ya = SerialTemporalFiles(root_path="C:\\CyMP\\Gafanhoto\\DADOS\\Imagens Cascavel\\Ya")
        self.serie_Ya.prefixo = "Ya_"
        self.serie_Ya.date_mask = "%Y%m%d"
        self.serie_Ya.mutiply_factor = 1
        
        self.serie_Kc = SerialTemporalFiles(root_path="C:\\CyMP\\Gafanhoto\\DADOS\\Imagens Cascavel\\Kc")
        self.serie_Kc.date_mask = "%Y-%m-%d"
    
