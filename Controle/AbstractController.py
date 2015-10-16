# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2015

@author: Paloschi
'''

from numpy.distutils.environment import __metaclass__
from abc import ABCMeta, abstractmethod
import threading
from PyQt4 import QtCore, QtGui
import ConfigParser
from types import NoneType
from Visao.Box_Progress_Bar import Ui_DlgProgressBar
from PyQt4.Qt import QString
import time

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
    Essa classe � um controlador abstrato, criado para padronizar os controladores.
    '''
    
    __metaclass__ = ABCMeta
    function = None
    thread = None

    def __init__(self, userInterface):
        '''
        Este contrutor é padrão para os controladores, ele recebe uma user interface que permite o controle
        as classes controladoras finais não deverão ter construtores
        '''
        self.config = ConfigParser.RawConfigParser()
        self.config.read('workspace.properties')
        self.ui = userInterface # seta interface para que seja visivel aos outros m�todos

    def print_text(self, text):
        self.progress_bar.print_text(text)
        
    def action_ok(self):
        """
            Esse método cria uma thread pra executar a função
        """
        if self.valida_form() :
         
            self.thread = StoppableThread(self.executa)
            
            self.progress_bar = Ui_DlgProgressBar(self.ui)
            self.progress_bar.setupUi(self.progress_bar)    
            self.progress_bar.show()
            
            self.thread.start()
                
            
            while(self.function==None) : 
                time.sleep(0.05)
                
            self.progress_bar.iniciar(self.function, self.thread)
            
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
        if type == "folder" :
            fname = QtGui.QFileDialog.getExistingDirectory()
        else :
            fname = QtGui.QFileDialog.getOpenFileName()
        textToWrite.setText (fname)
        
    def message(self, text):
        text = QString(text)
        QtGui.QMessageBox.about(self.ui, "Ops...", text)

    def confirmation(self, text):
        text = QString(text)

        quit_msg = "Are you sure you want to exit the program?"
        
        reply = QtGui.QMessageBox.question(self.progress_bar, 'Message', 
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            return True
        else:
            return False

        
    def funcao_cancelada(self):
        if threading.currentThread().stopped():
            if self.confirmation("Deseja realmente interromper o processo?"):
                self.progress_bar.finalizar()
                self.progress_bar.funcao_finalizada = True
                return True
            return False
        return False
