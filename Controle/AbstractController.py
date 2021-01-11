# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2015

@author: Paloschi
'''

#from numpy.distutils.environment import __metaclass__
from abc import ABCMeta, abstractmethod
import threading
from PyQt5 import QtCore, QtWidgets
import configparser as ConfigParser
NoneType = type(None)
from Visao.Box_Progress_Bar import Ui_DlgProgressBar
import time
from Visao import DlgNovaSerieTemporal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, funcao):
        super(StoppableThread, self).__init__(target=funcao)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

class Controller(object):
    '''
    Essa classe é um controlador abstrato, criado para padronizar os controladores.
    '''
    
    __metaclass__ = ABCMeta # define a classe como abstrata
    function = None
    thread = None

    def __init__(self, userInterface):
        '''
        Este contrutor é padrão para os controladores, ele recebe uma user interface que permite o controle
        as classes controladoras finais não deverão ter construtores
        '''
        try:
            self.config = ConfigParser.RawConfigParser()
            self.config.read('workspace.properties')
            self.ui = userInterface # seta interface para que seja visivel aos outros m�todos
        except Exception as e:
            print(e)

    def print_text(self, text):
        self.progress_bar.print_text(text)
        
    def console(self, text):
        self.progress_bar.print_text(text)
        
    def action_ok(self):
        """
            Esse método cria uma thread pra executar a função
        """
        try:
            if self.valida_form() :
                print("Form validated")
                self.function = None
                self.thread = StoppableThread(self.executa)
                self.progress_bar = Ui_DlgProgressBar(self.ui)
                self.progress_bar.setupUi(self.progress_bar)
                print("Progress dialog shown")
                self.progress_bar.show()
                print("Progress dialog shown")
                self.thread.start()
                print("Thread running")
                while(self.function==None) :
                    time.sleep(0.005)
                self.function.print_text = self.progress_bar.print_text
                self.function.console = self.progress_bar.print_text
                self.progress_bar.iniciar(self, self.thread)
                print("Action ok finished")
        except Exception as e:
            print (e)
            
    def action_cancel(self):
            if self.thread != NoneType :
                if self.thread != None :
                    if self.thread.stopped() == False :
                        self.message(u"Atividade ainda em execução \n feche o aplicativo para parar")
            self.ui.close()
    
    @abstractmethod
    def valida_form(self):
        '''
        Esse método tem que existir nas classes controladoras
        aqui serão feitas todas as validações do form    
        '''
   
    @abstractmethod
    def executa(self):
        '''
        Esse método temque existir nas classes controladoras
        aqui serão executadas as funções quando for apertado OK na tela
        '''
    
    """
        Aqui a baixo estão alguns recursos para facilitar a vida dos controladores
    """
    
    def findPath(self, textToWrite, type="none"):
        
        config = ConfigParser.RawConfigParser()
        config.read('workspace.properties')
        workspace=config.get('WorkSpace', 'space.default')
        
        if type == "folder" :
            fname = QtWidgets.QFileDialog.getExistingDirectory(self.ui, "Selecione uma pasta", workspace)
        else :
            print ("here")
            fname = QtWidgets.QFileDialog.getOpenFileName(self.ui, "Selecione o arquivo", workspace)
        if fname!="" :
            print(fname)
            textToWrite.setText (str(fname[0]))
    
    def getSerieTemporal(self, serieTemporal=None):
        
        dlgSerieTemporal = DlgNovaSerieTemporal.Ui_Dialog(self.ui)
        dlgSerieTemporal.setupUi(dlgSerieTemporal) 
        dlgSerieTemporal.setWindowModality(QtCore.Qt.WindowModal)   
        
        dlgSerieTemporal.setForm(serieTemporal)
        
        dlgSerieTemporal.exec_()
         
        serie_temporal = dlgSerieTemporal.SerieTemporal
        return serie_temporal       
        
    def message(self, text):
        text = text
        QtWidgets.QMessageBox.about(self.ui, "Ops...", text)
        
    def funcao_cancelada(self):
        if threading.currentThread().stopped():
                self.progress_bar.finalizar()
                return True
        return False
    
    def confirmar(self, text, title):
        quit_msg = text
        reply = QtWidgets.QMessageBox.question(self.ui, title,
                     quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False
    
    def finalizar(self):
        self.function.progresso = 100
        self.thread.stop()
        time.sleep(0.2)
        self.progress_bar.finalizar()