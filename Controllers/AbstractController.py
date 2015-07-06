# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2015

@author: Paloschi
'''

from numpy.distutils.environment import __metaclass__
from abc import ABCMeta, abstractmethod
import threading
from PyQt4 import QtCore, QtGui


import time
import sys
from py2exe.build_exe import Target
from types import NoneType

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    

class BatchProcesser(QtCore.QThread):
    __errorHappened = False
    
    def __init__(self, target, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False
        self.target = target
         
    def run(self):
         while self.target == None : pass
         while (  self.target.progresso < 100):
            QtCore.QThread.msleep(1)
            self.emit(QtCore.SIGNAL("progress(int)"), self.target.progresso)

class AddProgresWin(QtGui.QWidget):
    def __init__(self,target, parent=None):
        super(AddProgresWin, self).__init__(parent)

        self.nameLabel = QtGui.QLabel("0.0%")
        self.nameLine = QtGui.QLineEdit()

        self.progressbar = QtGui.QProgressBar()
        self.progressbar.setMinimum(1)
        self.progressbar.setMaximum(100)
        
        self.processThread = BatchProcesser(target)
        
        QtCore.QObject.connect(self.processThread, QtCore.SIGNAL("progress(int)"),self.progressbar, QtCore.SLOT("setValue(int)"), QtCore.Qt.QueuedConnection)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.progressbar, 0, 0)
        mainLayout.addWidget(self.nameLabel, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Processing")

        #self.processThread.partDone.connect(self.updatePBar)
        #self.processThread.procDone.connect(self.fin)

        self.processThread.start()
        
        def updatePBar(self, val):
            self.progressbar.setValue(val)   
            perct = "{0}%".format(val)
            self.nameLabel.setText(perct)

        def fin(self):
            sys.exit()
            ##self.hide()


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
        
        self.ui = userInterface # seta interface para que seja visivel aos outros m�todos

        
    def action_ok(self):
        """
            Esse método cria uma thread pra executar a função
        """
        
        if self.valida_form() :

            #self.verify_progress = AddProgresWin(target=self.function)
            #self.verify_progress.show()
            
            self.thread = StoppableThread(self.executa)
            self.thread.start()
            
    def action_cancel(self):
            if self.thread != NoneType :
                if self.thread != None :
                    if self.thread.stopped() == False :
                        self.message(u"Atividade ainda em execução \n feche o aplicativo para parar")
            self.ui.close()
    
    @abstractmethod
    def valida_form(self):
        '''
        Esse método temque existir nas classes controladoras
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
    
    def ajeitarPath(self, pathIn):
        """
            Essa função da uma arrumada no path por causa das barras invertidas que as vezes bugam
        """
        root = _fromUtf8(str(pathIn) + "\\")
        root = str(root).replace("\\", "/")    
        
        return root   
    
    def findPath(self, textToWrite, type="none"):
        if type == "folder" :
            fname = QtGui.QFileDialog.getExistingDirectory()
        else :
            fname = QtGui.QFileDialog.getOpenFileName()
        textToWrite.setText (fname)
        
    def message(self, text):
        QtGui.QMessageBox.about(self.ui, "Ops...", text)
        
