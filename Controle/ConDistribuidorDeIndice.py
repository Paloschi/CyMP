# -*- coding: utf-8 -*-

'''
Created on 19/10/2015

@author: Rennan
'''
from Controle.AbstractController import Controller
from Modelo.Funcoes.BalancoHidrico import DistribuidorKC
from Modelo.beans import TableData, RasterFile
from PyQt4 import QtCore, QtGui
import os
import threading
import time

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Controller(Controller):
    
    def addEstagio(self):
        numero_de_linhas = self.ui.tableWidget.rowCount()
        ultimo_dia = str(self.ui.tableWidget.item(numero_de_linhas-1, 1).text())
        dia_inicial = str(self.ui.tableWidget.item(numero_de_linhas-1, 0).text())
        valor = str(self.ui.tableWidget.item(numero_de_linhas-1, 2).text())
        
        ultimo_dia_int = 0
        
        try :
            ultimo_dia_int = int(ultimo_dia)
            float(valor)
        except:
            self.message(u"Preencha corretamente o Estádio anterior")
            return
            
        if(ultimo_dia_int<=int(dia_inicial)):
            self.message(u"O dia final do Estádio anterior precisa ser maior que o inicial")
            return
        else:
            i_nova_linha = numero_de_linhas
            self.ui.tableWidget.setRowCount(i_nova_linha + 1)
            
            item = QtGui.QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(i_nova_linha, item)
            
            item = self.ui.tableWidget.verticalHeaderItem(i_nova_linha)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            item.setText(_translate("Dialog", ("Estádio " + str(i_nova_linha+1)), None))
            
            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.tableWidget.setItem(i_nova_linha, 0, item)
            
            item = self.ui.tableWidget.item(i_nova_linha, 0)
            item.setText(_translate("Dialog", str(ultimo_dia), None)) 
            
            item = QtGui.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.tableWidget.setItem(i_nova_linha, 1, item)     

            item = QtGui.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.tableWidget.setItem(i_nova_linha, 2, item)   
            
            item = self.ui.tableWidget.item(i_nova_linha-1, 1)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            item = self.ui.tableWidget.item(i_nova_linha-1, 2)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            
    def remEstagio(self):
        numero_de_linhas = self.ui.tableWidget.rowCount()
        if numero_de_linhas > 1 :
            self.ui.tableWidget.setRowCount(numero_de_linhas - 1)
  
    def findImgColheita(self):
        self.findPath(self.ui.txImgColheita)
    
    def findImgSemeadura(self):
        self.findPath(self.ui.txImgSemeadura)
    
    def findOutFolder(self):
        self.findPath(self.ui.txOutFolder, "folder")
    
    def changeDefaultIndices(self):
        self.ui.tableWidget.setRowCount(1)
        
        op_selected = str(self.ui.comboBox.currentText())
        
        if (op_selected=="Kc FAO - Soja"):
        
            self.ui.tableWidget.item(0, 1).setText("10") 
            self.ui.tableWidget.item(0, 2).setText("0.4") 
            
            self.addEstagio()
            self.ui.tableWidget.item(1, 1).setText("50") 
            self.ui.tableWidget.item(1, 2).setText("0.8")      
    
            self.addEstagio()
            self.ui.tableWidget.item(2, 1).setText("85") 
            self.ui.tableWidget.item(2, 2).setText("1.15") 
    
            self.addEstagio()
            self.ui.tableWidget.item(3, 1).setText("125") 
            self.ui.tableWidget.item(3, 2).setText("0.8") 
    
            self.addEstagio()
            self.ui.tableWidget.item(4, 1).setText("140") 
            self.ui.tableWidget.item(4, 2).setText("0.5")  
        
        else :
            
            self.ui.tableWidget.item(0, 1).setText("10") 
            self.ui.tableWidget.item(0, 2).setText("0.1") 
            
            self.addEstagio()
            self.ui.tableWidget.item(1, 1).setText("50") 
            self.ui.tableWidget.item(1, 2).setText("0.25")      
    
            self.addEstagio()
            self.ui.tableWidget.item(2, 1).setText("140") 
            self.ui.tableWidget.item(2, 2).setText("0.6") 
            
    def valida_form(self):
        if not os.path.exists(self.ui.txImgSemeadura.text()):
            self.message(u"Imagem de semeadura não encontrada")
            return False        
        if not os.path.exists(self.ui.txImgColheita.text()):
            self.message(u"Imagem de colheita não encontrada")
            return False
        if not os.path.exists(self.ui.txOutFolder.text()):
            self.message(u"Pasta de saída não encontrada") 
            return False
            
        numero_de_linhas = self.ui.tableWidget.rowCount()
        ultimo_dia = str(self.ui.tableWidget.item(numero_de_linhas-1, 1).text())
        dia_inicial = str(self.ui.tableWidget.item(numero_de_linhas-1, 0).text())   
        valor = str(self.ui.tableWidget.item(numero_de_linhas-1, 2).text())
        
        ultimo_dia_int = 0
        try :
            ultimo_dia_int = int(ultimo_dia)
            float(valor) # testa se é possivel converter o ultimo valor pra float
        except:
            self.message(u"Preencha corretamente o último período")
            return False
            
        if(ultimo_dia_int<=int(dia_inicial)):
            self.message(_translate("O dia final do Estádio anterior precisa ser maior que o inicial"))
            return False
        if self.confirmar(_translate("MainWindow","Caso esteja disponível, "+
                            "essa função utilizará os multiplos nucleos deste processador. " +
                            "Não há controle de multiprocesso implementado nesta versão logo " +
                            "este processo não poderá ser encerrado até que seja terminado, "+
                            "ela poderá levar várias horas para ser concluída, deseja realmente continuar?", None), 
                            u"Aviso!") :
            
            self.message(_translate("MainWindow","Verifique na pasta de saída se as imagens estão sendo criadas, "+
                         "as imagens poderão demorar até 10 minutos para aparecerem (com 5 milhões de pixels por imagem).", None))
            return True
        return False
                 
    def executa(self):
        
        self.print_text(u"Configurando função")
        self.progress_bar.btnCancelar.setEnabled(False)
        self.progress_bar.progressBar.setMaximum(0)
        self.function = DistribuidorKC() #função utilizada por este contrlolador
        
        '''
            Organizando tabela de kc em tabela para passar para a funcao
        '''
        numero_de_linhas = self.ui.tableWidget.rowCount()
        Kc = TableData()
        for i in range(numero_de_linhas):
            dia_inicio = str(self.ui.tableWidget.item(numero_de_linhas-1, 0).text())
            dia_fim = str(self.ui.tableWidget.item(numero_de_linhas-1, 1).text())
            valor =  float(str(self.ui.tableWidget.item(numero_de_linhas-1, 2).text()))
            Kc[dia_inicio+"-"+dia_fim] = valor
        '''
            Montando objetos raster referentes as imagens de semeadura e colheita para passar para a funcao
        '''
        semeadura = RasterFile(file_full_path = str(self.ui.txImgSemeadura.text()))
        colheita = RasterFile(file_full_path = str(self.ui.txImgColheita.text()))
        OutFolder = str(self.ui.txOutFolder.text())
        multply_factor = self.ui.txMultiplyFactor.value()
        
        '''
            Montando tabela com os parametros para a funcao
        '''
        paramIN = TableData()
        paramIN["Kc"] = Kc
        paramIN["semeadura"] = semeadura
        paramIN["colheita"] = colheita
        paramIN["path_out"] = OutFolder
        paramIN["multply_factor"] = multply_factor
        
        '''
            Executa a função
        '''
        self.print_text(u"Distribuindo índice")
        resultado = self.function.executar(paramIN)
        '''
            Verifica o que aconteceu com o processo
        '''
        if self.funcao_cancelada() : return None
        elif resultado == None :
            self.print_text(u"erro deconhecido, função interrompida")
            threading.currentThread().stop()
            self.finalizar()
        else : 
            self.print_text(u"função concluída")
            self.progress_bar.progressBar.setMaximum(100)
            threading.currentThread().stop()
            self.finalizar()
        
        
        