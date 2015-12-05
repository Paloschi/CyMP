# -*- coding: utf-8 -*-
'''
Created on 03/12/2015

@author: Paloschi
'''
from Controle import AbstractController

class Controller(AbstractController.Controller):
    
    serie_ETa = None
    serie_ETc = None
    serie_Yx = None
    serie_Ya = None
    
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

    def executa(self):
        pass
    
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
        pass
    
