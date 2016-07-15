# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Box_Progress_Bar.ui'
#
# Created: Tue Oct 13 04:35:05 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
from PyQt4.Qt import QDialog
import time
#from matplotlib.textpath import text_to_path

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DlgProgressBar(QDialog):
    
    
    text_to_append = ""
    funcao_finalizada = False
    
    def print_text(self, text):
        while self.text_to_append != "" : pass
        self.text_to_append = text
        
    
    def iniciar(self, controller, thread_executando):
        self.thread_executando = thread_executando
        print "iniciando"
        self._active = True
        while True:
            time.sleep(0.05)
            if self.text_to_append != "" : 
                self.console.appendPlainText(self.text_to_append)
                self.text_to_append = ""
            value = controller.function.progresso
            self.progressBar.setValue(value)
            #print value
            QtGui.qApp.processEvents()
            if (not self._active):
                self.funcao_terminada()
                break
            if self.funcao_finalizada : self.funcao_terminada()

        QtGui.qApp.processEvents()
        
    def cancelar(self):
        if self.confirmar_cancelamento() :
            self.console.appendPlainText("cancelando..")
            self.thread_executando.stop() 
            QtGui.qApp.processEvents()
            while not self.funcao_finalizada : pass
            self.console.appendPlainText(U"Função cancelada!")
            self.btnCancelar.setEnabled(False)
            self.btnOk.setEnabled(True)            
            self._active = False
            self.progressBar.setValue(100)

        
    def confirmar_cancelamento(self):
        quit_msg = "Deseja realmente cancelar o processo?"
        reply = QtGui.QMessageBox.question(self, 'Cancelamento', 
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            return True
        else:
            return False
        
    def setupUi(self, DlgProgressBar):
        DlgProgressBar.setObjectName(_fromUtf8("DlgProgressBar"))
        DlgProgressBar.resize(388, 247)
        self.verticalLayout = QtGui.QVBoxLayout(DlgProgressBar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.label = QtGui.QLabel(DlgProgressBar)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        
        self.console = QtGui.QPlainTextEdit(DlgProgressBar)
        self.console.setReadOnly(True)
        self.console.setPlainText(_fromUtf8(""))
        self.console.setObjectName(_fromUtf8("console"))
        self.verticalLayout.addWidget(self.console)
        
        self.progressBar = QtGui.QProgressBar(DlgProgressBar)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        
        self.btnCancelar = QtGui.QPushButton(DlgProgressBar)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.verticalLayout.addWidget(self.btnCancelar)
        
        self.btnOk = QtGui.QPushButton(DlgProgressBar)
        self.btnOk.setEnabled(False)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.verticalLayout.addWidget(self.btnOk)

        self.retranslateUi(DlgProgressBar)
        QtCore.QMetaObject.connectSlotsByName(DlgProgressBar)

    def retranslateUi(self, DlgProgressBar):
        DlgProgressBar.setWindowTitle(_translate("DlgProgressBar", "CyMP - Execução da função", None))
        self.label.setText(_translate("DlgProgressBar", "Status:", None))
        self.btnCancelar.setText(_translate("DlgProgressBar", "Cancelar", None))
        self.btnOk.setText(_translate("DlgProgressBar", "OK", None))
        
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnOk.clicked.connect(self.reject)

    def finalizar(self):
        self.funcao_finalizada = True
        
        
    def funcao_terminada(self):
        self.funcao_finalizada = True
        self.btnCancelar.setEnabled(False)
        self.btnOk.setEnabled(True)            
        self._active = False
        self.progressBar.setValue(100)