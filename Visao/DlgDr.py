# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgDr.ui'
#
# Created: Wed Nov 11 04:59:35 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controle.ConDr import Controller

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

class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, Dialog):
        
        self.controller = Controller(self)
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(451, 273)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)

        self.gridLayout = QtGui.QGridLayout()
      
        self.label = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        self.label_2 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btnConfETc = QtGui.QPushButton(Dialog)
        self.gridLayout.addWidget(self.btnConfETc, 1, 1, 1, 1)
        self.chEtc = QtGui.QCheckBox(Dialog)
        self.chEtc.setEnabled(False)
        self.gridLayout.addWidget(self.chEtc, 1, 2, 1, 1)
        
        self.label_3 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.btnConfPPP = QtGui.QPushButton(Dialog)
        self.gridLayout.addWidget(self.btnConfPPP, 2, 1, 1, 1)
        self.chPPP = QtGui.QCheckBox(Dialog)
        self.chPPP.setEnabled(False)
        self.gridLayout.addWidget(self.chPPP, 2, 2, 1, 1)
        
        self.label_4 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.btnConfTAW = QtGui.QPushButton(Dialog)
        self.gridLayout.addWidget(self.btnConfTAW, 3, 1, 1, 1)
        self.chTAW = QtGui.QCheckBox(Dialog)
        self.chTAW.setEnabled(False)
        self.gridLayout.addWidget(self.chTAW, 3, 2, 1, 1)
        
        self.label_7 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.txImgCAD = QtGui.QLineEdit(Dialog)
        self.gridLayout.addWidget(self.txImgCAD, 4, 1, 1, 1)
        self.btnFindImgCAD = QtGui.QToolButton(Dialog)
        self.gridLayout.addWidget(self.btnFindImgCAD, 4, 2, 1, 1)        
        
        self.label_5 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)       

        self.label_6 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1) 
        self.BtnConfDr = QtGui.QPushButton(Dialog)
        self.gridLayout.addWidget(self.BtnConfDr, 6, 1, 1, 1)               
        self.chDr = QtGui.QCheckBox(Dialog)
        self.chDr.setEnabled(False)
        self.gridLayout.addWidget(self.chDr, 6, 2, 1, 1)
        
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.controller.action_ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.controller.action_cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.BtnConfDr.clicked.connect(self.controller.setSerie_Dr)
        self.btnConfETc.clicked.connect(self.controller.setSerie_ETc)
        self.btnConfPPP.clicked.connect(self.controller.setSeriePPP)
        self.btnConfTAW.clicked.connect(self.controller.setSerie_TAW)
        self.btnFindImgCAD.clicked.connect(self.controller.findImgCAD)
        
        self.controller.parametros_teste()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - Valor de esgotamento (Dr)", None))
        self.chTAW.setText(_translate("Dialog", "configurado", None))
        self.btnConfPPP.setText(_translate("Dialog", "configurar", None))
        self.label.setText(_translate("Dialog", "Configuração de entrada:", None))
        self.chDr.setText(_translate("Dialog", "configurado", None))
        self.label_2.setText(_translate("Dialog", "Série de imagens de Etc:", None))
        self.label_3.setText(_translate("Dialog", "Série de imagens de Precipitação:", None))
        self.label_4.setText(_translate("Dialog", "Série de imagens TAW:", None))
        self.label_5.setText(_translate("Dialog", "Configuração de saída:", None))
        self.label_5.setText(_translate("Dialog", "Configuração de saída:", None))
        self.btnConfTAW.setText(_translate("Dialog", "configurar", None))
        self.btnConfETc.setText(_translate("Dialog", "configurar", None))
        self.label_6.setText(_translate("Dialog", "Série de Imagens de esgotamento:", None))
        self.chPPP.setText(_translate("Dialog", "configurado", None))
        self.BtnConfDr.setText(_translate("Dialog", "configurar", None))
        self.chEtc.setText(_translate("Dialog", "configurado", None))
        self.label_7.setText(_translate("Dialog", "Imagem de CAD:", None))
        self.btnFindImgCAD.setText(_translate("Dialog", "...", None))

