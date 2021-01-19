# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgPPB.ui'
#
# Created: Fri Nov 27 07:19:40 2015
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Controle.ConPPR import Controller

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)


def _translate(context, text, disambig):
    return text


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        
        self.controller = Controller(self)
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txCc = QtWidgets.QDoubleSpinBox(Dialog)
        self.txCc.setDecimals(8)
        self.txCc.setMaximum(999.99999999)
        self.txCc.setObjectName(_fromUtf8("txCc"))
        self.gridLayout.addWidget(self.txCc, 2, 1, 1, 1)
        self.chT = QtWidgets.QCheckBox(Dialog)
        self.chT.setEnabled(False)
        self.chT.setObjectName(_fromUtf8("chT"))
        self.gridLayout.addWidget(self.chT, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.chPPR = QtWidgets.QCheckBox(Dialog)
        self.chPPR.setEnabled(False)
        self.chPPR.setObjectName(_fromUtf8("chPPR"))
        self.gridLayout.addWidget(self.chPPR, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.btnConfPPR = QtWidgets.QPushButton(Dialog)
        self.btnConfPPR.setObjectName(_fromUtf8("btnConfPPR"))
        self.gridLayout.addWidget(self.btnConfPPR, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.btnConfTemp = QtWidgets.QPushButton(Dialog)
        self.btnConfTemp.setObjectName(_fromUtf8("btnConfTemp"))
        self.gridLayout.addWidget(self.btnConfTemp, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.controller.action_ok)
        self.buttonBox.rejected.connect(self.controller.action_cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btnConfTemp.clicked.connect(self.controller.setSerieT)
        self.btnConfPPR.clicked.connect(self.controller.setSeriePPR)
        
        self.controller.parametros_teste()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - Produtividade potencial bruta (PPB)", None))
        self.chT.setText(_translate("Dialog", "Configurado", None))
        self.label_2.setText(_translate("Dialog", "Série de imagens de PPB:", None))
        self.label_3.setText(_translate("Dialog", "Dados de entrada:", None))
        self.chPPR.setText(_translate("Dialog", "Configurado", None))
        self.label_4.setText(_translate("Dialog", "Configuração de saída:", None))
        self.btnConfPPR.setText(_translate("Dialog", "Configurar", None))
        self.label_5.setText(_translate("Dialog", "Indice de colheita (Cc):", None))
        self.label.setText(_translate("Dialog", "Série de imagens de Temperatura:", None))
        self.btnConfTemp.setText(_translate("Dialog", "Configurar", None))

