# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgETc.ui'
#
# Created: Wed Nov 11 00:58:52 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controle.ConBH import Controller

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
        Dialog.resize(371, 290)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.btnConfETc = QtGui.QPushButton(Dialog)
        self.btnConfETc.setObjectName(_fromUtf8("btnConfETc"))
        self.gridLayout.addWidget(self.btnConfETc, 4, 1, 1, 1)
        self.chETc = QtGui.QCheckBox(Dialog)
        self.chETc.setEnabled(False)
        self.chETc.setObjectName(_fromUtf8("chETc"))
        self.gridLayout.addWidget(self.chETc, 4, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btnConfET0 = QtGui.QPushButton(Dialog)
        self.btnConfET0.setObjectName(_fromUtf8("btnConfET0"))
        self.gridLayout.addWidget(self.btnConfET0, 1, 1, 1, 1)
        self.chET0 = QtGui.QCheckBox(Dialog)
        self.chET0.setEnabled(False)
        self.chET0.setObjectName(_fromUtf8("chET0"))
        self.gridLayout.addWidget(self.chET0, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.btnConfKc = QtGui.QPushButton(Dialog)
        self.btnConfKc.setObjectName(_fromUtf8("btnConfKc"))
        self.gridLayout.addWidget(self.btnConfKc, 2, 1, 1, 1)
        self.chKc = QtGui.QCheckBox(Dialog)
        self.chKc.setEnabled(False)
        self.chKc.setObjectName(_fromUtf8("chKc"))
        self.gridLayout.addWidget(self.chKc, 2, 2, 1, 1)
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
        
        self.btnConfET0.clicked.connect(self.controller.setSerieET0)
        self.btnConfKc.clicked.connect(self.controller.setSerie_Kc)
        self.btnConfETc.clicked.connect(self.controller.setSerie_ETc)
        
        #self.controller.parametros_teste()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Evapotranspiração da cultura", None))
        self.label_4.setText(_translate("Dialog", "Configuração de saída:", None))
        self.label_5.setText(_translate("Dialog", "Imagens diárias de ETc", None))
        self.btnConfETc.setText(_translate("Dialog", "Configurar", None))
        self.chETc.setText(_translate("Dialog", "Configurado", None))
        self.label.setText(_translate("Dialog", "Configuração de entrada", None))
        self.label_2.setText(_translate("Dialog", "Imagens diárias de ET0", None))
        self.btnConfET0.setText(_translate("Dialog", "Configurar", None))
        self.chET0.setText(_translate("Dialog", "Configurado", None))
        self.label_3.setText(_translate("Dialog", "Imagens diárias de Kc", None))
        self.btnConfKc.setText(_translate("Dialog", "Configurar", None))
        self.chKc.setText(_translate("Dialog", "Configurado", None))

