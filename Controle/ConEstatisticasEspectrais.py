# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2015

@author: Paloschi
'''

from Modelo.Funcoes import StatisticalStractor
from Modelo.beans import Dados
from Controle import AbstractController

class Controller(AbstractController.Controller):
    '''
    classdocs
    '''
    
    def findInFolder(self):
        self.findPath(self.ui.leInFolder, "folder")
        
    def findOutFolder(self):
        self.findPath(self.ui.leOutFolder, "folder")
  
    def executa(self):
        
        root_in = self.ui.leInFolder.text()
        root_in = self.ajeitarPath(root_in)
        
        imagens_entrada = Dados.SERIAL_DATA()
        imagens_entrada = imagens_entrada.loadListByRoot(root_in, "tif")
        
        root_out = self.ui.leOutFolder.text()
        root_out = self.ajeitarPath(root_out)
        
        statistical_list = Dados.SERIAL_DATA(data=self.statistical_list)
        null_value = Dados.FILE_DATA(data=None)
        
        paramsIN = Dados.TABLE_DATA()
        paramsIN["images"] = imagens_entrada
        paramsIN["null_value"] = null_value
        paramsIN["statistics"] = statistical_list
        
        self.function = StatisticalStractor.SpectreStatisticalStractor()
        self.function.data = paramsIN
        images_saida = self.function.data
        images_saida.saveListByRoot(images_saida, root_out, "tif")      
        
        
    def valida_form(self):
        
        self.statistical_list = list()
        
        if self.ui.cbMax.isChecked() : self.statistical_list.append("max")
        if self.ui.cbMedia.isChecked() : self.statistical_list.append("media")
        if self.ui.cbMediana.isChecked() : self.statistical_list.append("mediana")
        if self.ui.cbMin.isChecked() : self.statistical_list.append("min")
        if self.ui.cbModa.isChecked() : self.statistical_list.append("moda")
        if self.ui.cbSD.isChecked() : self.statistical_list.append("sd")
        if self.ui.cbSoma.isChecked() : self.statistical_list.append("soma")
        if self.ui.cbCV.isChecked() : self.statistical_list.append("cv")
        
        if len(self.statistical_list) == 0 :
            self.message(u"Selecione pelo menos uma opção na aba Configuração")
            return False
        return True