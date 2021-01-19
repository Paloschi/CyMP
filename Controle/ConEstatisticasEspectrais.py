# -*- coding: utf-8 -*-
'''
Created on Jun 10, 2015

@author: Paloschi
'''

from Modelo.Funcoes.Estatisticos import SpectreStatisticalStractor
from Modelo.beans import SerialFile, TableData
from Controle import AbstractController
import os.path as path

class Controller(AbstractController.Controller):
    '''
    classdocs
    '''
    
    def findInFolder(self):
        self.findPath(self.ui.leInFolder, "folder")
        
    def findOutFolder(self):
        self.findPath(self.ui.leOutFolder, "folder")
  
    def executa(self):
        
        self.function = SpectreStatisticalStractor()
        

        self.print_text(u"Organizando dados necessários")
        
        root_in = str(self.ui.leInFolder.text())
        root_in = path.normpath(root_in)
        
        imagens_entrada = SerialFile()
        imagens_entrada = imagens_entrada.loadListByRoot(root_in, "tif, img")
        
        if(len(imagens_entrada)==0):
            self.console(u"Nenhuma imagem encontrada, abortando função")
            self.finalizar()
            self.console(u"Função finalizada")
            return
        
        root_out = str(self.ui.leOutFolder.text())
        root_out = path.normpath(root_out)
        
        paramsIN = TableData()
        paramsIN["images"] = imagens_entrada
        paramsIN["statistics"] = self.statistical_list

        images_saida = self.function.executar(paramsIN)

        print("Salvando imagens")
        self.print_text("Salvando imagens")
        
        if self.funcao_cancelada(): 
            
            return None
        
        for imagem in images_saida :

            try:
                imagem.saveRasterData(file_path=root_out, ext="tif")   
                self.console("Imagem "+ imagem.file_name+" salva.")
            except:
                self.console(u"Não foi possivel salvar a imagem: " + imagem.file_name+ u". Verifique se o arquivo está sendo usado por outro aplicativo.")
            
        self.print_text(u"Conluído.")
        self.finalizar()
        
        
    def valida_form(self):

        if not path.exists(str(self.ui.leInFolder.text())):
            self.message(u"Pasta de entrada nao encontrada")   
            return False     
        if not path.exists(str(self.ui.leOutFolder.text())):
            self.message(u"Pasta de saída nao encontrada")
            return False
        
        self.statistical_list = list()
        
        if self.ui.cbMax.isChecked() : self.statistical_list.append("max")
        if self.ui.cbMedia.isChecked() : self.statistical_list.append("media")
        if self.ui.cbMediana.isChecked() : self.statistical_list.append("mediana")
        if self.ui.cbMin.isChecked() : self.statistical_list.append("min")
        if self.ui.cbAmplitude.isChecked() : self.statistical_list.append("amplitude")
        if self.ui.cbSD.isChecked() : self.statistical_list.append("sd")
        if self.ui.cbSoma.isChecked() : self.statistical_list.append("soma")
        if self.ui.cbCV.isChecked() : self.statistical_list.append("cv")

        if len(self.statistical_list) == 0 :
            self.message(u"Selecione pelo menos uma opção na aba Configuração")
            return False
        
        return True
    
    def parametros_teste(self):
            self.ui.leInFolder.setText("D:\\Agririsk\\Coamo_FAO_estimation\\Ya_Cc0.2795")
            self.ui.leOutFolder.setText("D:\\Agririsk\\Coamo_FAO_estimation")
    
