# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgDecendial2Diario.ui'
#
# Created: Mon Nov 09 13:44:39 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controle import ConDecendial2Diario

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

class Ui_Decendial2Diario(QtGui.QDialog):
    def setupUi(self, Dialog):
        
        self.controller = ConDecendial2Diario.Controller(self)
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(283, 166)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.chDecendial = QtGui.QCheckBox(Dialog)
        self.chDecendial.setText(_fromUtf8(""))
        #self.chDecendial.setCheckState()
        self.chDecendial.setCheckable(False)
        self.chDecendial.setEnabled(False)
        
        self.chDecendial.setObjectName(_fromUtf8("chDecendial"))
        self.gridLayout.addWidget(self.chDecendial, 2, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.chDiario = QtGui.QCheckBox(Dialog)
        self.chDiario.setText(_fromUtf8(""))
        self.chDiario.setCheckable(False)
        self.chDiario.setObjectName(_fromUtf8("chDiario"))
        self.chDiario.setEnabled(False)
        self.gridLayout.addWidget(self.chDiario, 1, 2, 1, 1)

        self.label_3 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_3, 3, 1, 2, 1)
        
        self.cbOperacao = QtGui.QComboBox(Dialog)
        self.cbOperacao.setEditable(True)
        self.cbOperacao.setObjectName(_fromUtf8("cbOperacao"))
        self.cbOperacao.addItem(_fromUtf8("manter valores"))
        self.cbOperacao.addItem(_fromUtf8("dividir valores"))
        self.gridLayout.addWidget(self.cbOperacao, 3, 1, 2, 1)
        
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.controller.action_ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.controller.action_cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.controller.setSerieEntrada)
        self.pushButton_2.clicked.connect(self.controller.setSerieSaida)
        
        self.controller.parametros_teste()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - Decendial para diário", None))
        self.label_2.setText(_translate("Dialog", "Entrada de imagens decendiais", None))
        self.label_3.setText(_translate("MainWindow", "", None))
        self.label.setText(_translate("Dialog", "Saída de imagens diárias", None))
        self.pushButton_2.setText(_translate("Dialog", "configurar", None))
        self.pushButton.setText(_translate("Dialog", "configurar", None))

