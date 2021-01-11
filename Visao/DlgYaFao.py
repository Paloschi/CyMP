# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgYa.ui'
#
# Created: Thu Dec 03 17:49:02 2015
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Controle.ConYaFao import Controller

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
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.btnConfYa = QtWidgets.QPushButton(Dialog)
        self.btnConfYa.setObjectName(_fromUtf8("btnConfYa"))
        self.gridLayout.addWidget(self.btnConfYa, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btnConfEta = QtWidgets.QPushButton(Dialog)
        self.btnConfEta.setObjectName(_fromUtf8("btnConfEta"))
        self.gridLayout.addWidget(self.btnConfEta, 1, 1, 1, 1)
        self.btnConfYx = QtWidgets.QPushButton(Dialog)
        self.btnConfYx.setObjectName(_fromUtf8("btnConfYx"))
        self.gridLayout.addWidget(self.btnConfYx, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.chETa = QtWidgets.QCheckBox(Dialog)
        self.chETa.setEnabled(False)
        self.chETa.setObjectName(_fromUtf8("chETa"))
        self.gridLayout.addWidget(self.chETa, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.BtnConfETc = QtWidgets.QPushButton(Dialog)
        self.BtnConfETc.setObjectName(_fromUtf8("BtnConfETc"))
        self.gridLayout.addWidget(self.BtnConfETc, 2, 1, 1, 1)
        self.txKy = QtWidgets.QDoubleSpinBox(Dialog)
        self.txKy.setObjectName(_fromUtf8("txKy"))
        self.gridLayout.addWidget(self.txKy, 3, 1, 1, 1)
        self.chETc = QtWidgets.QCheckBox(Dialog)
        self.chETc.setEnabled(False)
        self.chETc.setObjectName(_fromUtf8("chETc"))
        self.gridLayout.addWidget(self.chETc, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.chYx = QtWidgets.QCheckBox(Dialog)
        self.chYx.setEnabled(False)
        self.chYx.setObjectName(_fromUtf8("chYx"))
        self.gridLayout.addWidget(self.chYx, 4, 2, 1, 1)
        self.chYa = QtWidgets.QCheckBox(Dialog)
        self.chYa.setEnabled(False)
        self.chYa.setObjectName(_fromUtf8("chYa"))
        self.gridLayout.addWidget(self.chYa, 7, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.btnConfKc = QtWidgets.QPushButton(Dialog)
        self.btnConfKc.setObjectName(_fromUtf8("btnConfKc"))
        self.gridLayout.addWidget(self.btnConfKc, 5, 1, 1, 1)
        self.chKc = QtWidgets.QCheckBox(Dialog)
        self.chKc.setEnabled(False)
        self.chKc.setObjectName(_fromUtf8("chKc"))
        self.gridLayout.addWidget(self.chKc, 5, 2, 1, 1)
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
        
        self.txKy.setValue(0.8)
        
        self.btnConfEta.clicked.connect(self.controller.setSerie_ETa)
        self.BtnConfETc.clicked.connect(self.controller.setSerie_ETc)
        self.btnConfYa.clicked.connect(self.controller.setSerie_Ya)
        self.btnConfYx.clicked.connect(self.controller.setSerie_Yx)
        self.btnConfKc.clicked.connect(self.controller.setSerie_Kc)
        
        #self.controller.parametros_teste()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - Produtividade Atingível (Ya)", None))
        self.label_7.setText(_translate("Dialog", "Produtividade atingível (Ya):", None))
        self.btnConfYa.setText(_translate("Dialog", "Configurar", None))
        self.label.setText(_translate("Dialog", "Dados de entrada:", None))
        self.label_2.setText(_translate("Dialog", "Evapotranspiração real (ETa)", None))
        self.btnConfEta.setText(_translate("Dialog", "Configurar", None))
        self.btnConfYx.setText(_translate("Dialog", "Configurar", None))
        self.label_5.setText(_translate("Dialog", "Produtividade Potencial Bruta (PPB-Yx):", None))
        self.label_6.setText(_translate("Dialog", "Dados de saída:", None))
        self.chETa.setText(_translate("Dialog", "configurado", None))
        self.label_3.setText(_translate("Dialog", "Evapotranspiração da cultura (ETc):", None))
        self.BtnConfETc.setText(_translate("Dialog", "Configurar", None))
        self.chETc.setText(_translate("Dialog", "configurado", None))
        self.label_4.setText(_translate("Dialog", "Fator de produtividade (Ky):", None))
        self.chYx.setText(_translate("Dialog", "configurado", None))
        self.chYa.setText(_translate("Dialog", "configurado", None))
        self.label_8.setText(_translate("Dialog", "Imagens de Kc", None))
        self.btnConfKc.setText(_translate("Dialog", "Configurar", None))
        self.chKc.setText(_translate("Dialog", "configurado", None))

