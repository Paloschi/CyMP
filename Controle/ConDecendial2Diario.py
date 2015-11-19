# -*- coding: utf-8 -*-
'''
Created on 09/11/2015

@author: Rennan
'''
from Controle import AbstractController
from Modelo.Funcoes.RasterTools import Decendial2Diario
from Modelo.beans.TableData import TableData
from Modelo.beans.SerialFileData import SerialTemporalFiles

class Controller(AbstractController.Controller):
    '''
    classdocs
    '''
    
    serie_entrada_decendial = None
    serie_saida_diaria = None
    
    def setSerieEntrada(self):
        imagens = self.getSerieTemporal(self.serie_entrada_decendial)
        if imagens is not None:
            self.serie_entrada_decendial = imagens
            self.ui.chDiario.setCheckState(True)
    
    def setSerieSaida(self):
        imagens = self.getSerieTemporal(self.serie_saida_diaria)
        if imagens is not None:
            self.serie_saida_diaria = imagens
            self.ui.chDecendial.setCheckState(True)

    def executa(self):
        
        #self.serie_entrada_decendial = SerialTemporalFiles()
        #self.serie_entrada_decendial.root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\7-Cortado_tamanho_Modis\\PPP"
        #self.serie_entrada_decendial.prefixo = "rain_"
        #self.serie_entrada_decendial.date_mask = "%Y%m%d"
        #self.serie_entrada_decendial.mutiply_factor = 0.01

        #self.serie_saida_diaria = SerialTemporalFiles()
        #self.serie_saida_diaria.root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\8-Diario\\PPP"
        #self.serie_saida_diaria.prefixo = "rain_"
        #self.serie_saida_diaria.date_mask = "%Y%m%d"
        #self.serie_saida_diaria.mutiply_factor = 1
                
        self.function = Decendial2Diario.Funcao()
        
        param = TableData()
        param["In"] = self.serie_entrada_decendial
        param["Out_config"] = self.serie_saida_diaria
        param["Operation"] = str(self.ui.cbOperacao.currentText())
        
        print "executar"
        resultado = self.function.executar(param)
        
        if self.funcao_cancelada():
            print "controller cancelando"
            self.console(u"Função interrompida.")
            self.finalizar()
        else :
            self.console(u"Função terminada")
            self.finalizar()
        
        return resultado
        
 
    def valida_form(self):
        
        return True
        
        if self.serie_entrada_decendial is None:
            return False
        if self.serie_saida_diaria is None:
            return False
        
        return True    
    
    
    def parametros_teste(self):
        root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\7.1-MultiplicadasPelaMascaraSoja11-12\\evpt"
        self.serie_entrada_decendial = SerialTemporalFiles()
        self.serie_entrada_decendial.root_path = root_path
        self.serie_entrada_decendial.prefixo = "evpt_"
        self.serie_entrada_decendial.mutiply_factor = 1
        self.serie_entrada_decendial.date_mask = "%Y%m%d"
        
        root_path = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\8-Diario\\EVPT\\novo"
        self.serie_saida_diaria = SerialTemporalFiles()
        self.serie_saida_diaria.root_path = root_path
        self.serie_saida_diaria.prefixo = "evpt_diario_"
        self.serie_saida_diaria.mutiply_factor = 100

        self.serie_saida_diaria.date_mask = "%Y-%m-%d"
        
 