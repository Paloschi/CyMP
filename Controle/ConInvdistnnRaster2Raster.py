# -*- coding: utf-8 -*-
'''
Created on 13/10/2015

@author: Rennan
'''
from Modelo.Funcoes.RasterTools import RasterToCSVeVRT
from Modelo.Funcoes.Interpoladores import IDW
from Modelo.beans import SerialFile, TableData
from PyQt4 import QtCore
from Controle import AbstractController
import os.path
from Modelo.beans.RasterData import RasterFile

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Controller(AbstractController.Controller):
    '''
    classdocs
    
    '''
    def findInFolder(self):
        self.findPath(self.ui.txInFolder, "folder")
        
    def findOutFolder(self):
        self.findPath(self.ui.txOutFolder, "folder")
  
    def findImgRef(self):
        self.findPath(self.ui.txImgReference)

    def valida_form(self):
        try :
            if not os.path.exists(self.ui.txInFolder.text()):
                self.message(u"Pasta de entrada das imagens não encontrada, verifique o endereço.")
                return False 
            if not os.path.exists(self.ui.txOutFolder.text()):
                self.message(u"Pasta de saida das imagens não encontrada, verifique o endereço.")
                return False
            if not os.path.exists(self.ui.txImgReference.text()):
                self.message(u"Imagem de referencia das imagens não encontrada, verifique o endereço.")
                return False     
            return True
        except :
            self.message(u"Não foi possível ler o caminho das imagens informadas (caracteres com acentos não podem ser lidos).")
            return False
    def executa(self):
        
        '''
            Criando arquivos CSVs e VRTs para submeter a interpolação
        '''
        
        self.console(u"Recolhendo informações")
        
        self.function = RasterToCSVeVRT()
        paramIn = TableData()
        paramIn["images"] = SerialFile(root_path=str(self.ui.txInFolder.text()))
        paramIn["out_folder"] = str(self.ui.txOutFolder.text())
        
        self.print_text(u'Interpolando imagens...')

        resultado = self.interpolar_todas_as_imagens(paramIn)
            
        if self.funcao_cancelada():
            #self.console(u"Função interrompida")
            self.finalizar()
        elif resultado is not None:
            self.console(u"Função concluída")
            self.finalizar()
    
    def interpolar_todas_as_imagens(self, paramIn):
        
        self.print_text(u"Lendo imagens e criando arquivos para a interpolação")
    
        resposta = self.function.executar(paramIn)
        if self.funcao_cancelada() : return
        
        CSVs = resposta["CSVs"]
        VRTs = resposta["VRTs"]
        
        self.print_text(u"Número de imagens identificadas para interpolar: " + str(len(CSVs)))
        self.function.progresso = 0.0
        
        conf_algoritimo = TableData()
        conf_algoritimo["power"] = str(self.ui.txPower.value())
        conf_algoritimo["radius"] = str(self.ui.txRadius.value())
        conf_algoritimo["max_points"] = str(self.ui.txMaxPoint.value())
        conf_algoritimo["min_points"] = str(self.ui.txMinPoint.value())
        
        conf_img_out = RasterFile(file_full_path=str(self.ui.txImgReference.text())).getRasterInformation()
        
        self.console(u"Interpolando imagens...")
        
        for i in range(len(CSVs)):
            
            img_out = RasterFile(file_full_path=VRTs[i].file_full_path)
            img_out.file_ext = "tif"           
            
            paramIn = TableData()
            paramIn["csv"] = CSVs[i]
            paramIn["vrt"] = VRTs[i]
            paramIn["img_out_config"] = conf_img_out
            paramIn["conf_algoritimo"] = conf_algoritimo
            paramIn["img_out"] = img_out
            
            self.function = IDW()
            self.function.setProgresso(i, len(CSVs))
            self.function.data = paramIn
            imagem_interpolada = self.function.data
            self.print_text("Imagem interpolada: " + imagem_interpolada.file_name)
            
            if self.funcao_cancelada(): return
        
        return "tudo certo!"
        

    def set_param(self):
            
        self.ui.txInFolder.setText("C:\\Users\\Paloschi\\Desktop\\TesteInterpolacao")
        self.ui.txOutFolder.setText("C:\\Users\\Paloschi\\Desktop\\TesteSaidaInterpolacao")
        self.ui.txImgReference.setText("C:\\Users\\Paloschi\\Desktop\\Imagem de referencia 2011_01_01.tif")
            
            
            
            
            
            
            
            
            
