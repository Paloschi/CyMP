# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgKs.ui'
#
# Created: Wed Nov 18 11:12:14 2015
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Controle.ConKs import Controller

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

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        
        self.controller = Controller(self)
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(451, 273)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chTAW = QtWidgets.QCheckBox(Dialog)
        self.chTAW.setEnabled(False)
        self.chTAW.setObjectName(_fromUtf8("chTAW"))
        self.gridLayout.addWidget(self.chTAW, 3, 2, 1, 1)
        self.btnConfRAW = QtWidgets.QPushButton(Dialog)
        self.btnConfRAW.setObjectName(_fromUtf8("btnConfRAW"))
        self.gridLayout.addWidget(self.btnConfRAW, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.chKs = QtWidgets.QCheckBox(Dialog)
        self.chKs.setEnabled(False)
        self.chKs.setObjectName(_fromUtf8("chKs"))
        self.gridLayout.addWidget(self.chKs, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.btnConfTAW = QtWidgets.QPushButton(Dialog)
        self.btnConfTAW.setObjectName(_fromUtf8("btnConfTAW"))
        self.gridLayout.addWidget(self.btnConfTAW, 3, 1, 1, 1)
        self.btnConfDr = QtWidgets.QPushButton(Dialog)
        self.btnConfDr.setObjectName(_fromUtf8("btnConfDr"))
        self.gridLayout.addWidget(self.btnConfDr, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.chRAW = QtWidgets.QCheckBox(Dialog)
        self.chRAW.setEnabled(False)
        self.chRAW.setObjectName(_fromUtf8("chRAW"))
        self.gridLayout.addWidget(self.chRAW, 2, 2, 1, 1)
        self.btnConfKs = QtWidgets.QPushButton(Dialog)
        self.btnConfKs.setObjectName(_fromUtf8("btnConfKs"))
        self.gridLayout.addWidget(self.btnConfKs, 5, 1, 1, 1)
        self.chDr = QtWidgets.QCheckBox(Dialog)
        self.chDr.setEnabled(False)
        self.chDr.setObjectName(_fromUtf8("chDr"))
        self.gridLayout.addWidget(self.chDr, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.controller.action_ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.controller.action_cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.btnConfTAW.clicked.connect(self.controller.setSerie_TAW)
        self.btnConfDr.clicked.connect(self.controller.setSerie_Dr)
        self.btnConfKs.clicked.connect(self.controller.setSerie_Ks)
        self.btnConfRAW.clicked.connect(self.controller.setSerieRAW)
        
        self.controller.parametros_teste()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - Fator de estresse hídrico da cultura (Ks)", None))
        self.chTAW.setText(_translate("Dialog", "configurado", None))
        self.btnConfRAW.setText(_translate("Dialog", "configurar", None))
        self.label.setText(_translate("Dialog", "Configuração de entrada:", None))
        self.chKs.setText(_translate("Dialog", "configurado", None))
        self.label_2.setText(_translate("Dialog", "Série de imagens Dr:", None))
        self.label_3.setText(_translate("Dialog", "Série de imagens RAW:", None))
        self.label_4.setText(_translate("Dialog", "Série de imagens TAW:", None))
        self.label_5.setText(_translate("Dialog", "Configuração de saída:", None))
        self.btnConfTAW.setText(_translate("Dialog", "configurar", None))
        self.btnConfDr.setText(_translate("Dialog", "configurar", None))
        self.label_6.setText(_translate("Dialog", "Série de Imagens de Ks:", None))
        self.chRAW.setText(_translate("Dialog", "configurado", None))
        self.btnConfKs.setText(_translate("Dialog", "configurar", None))
        self.chDr.setText(_translate("Dialog", "configurado", None))

