# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgPPB.ui'
#
# Created: Fri Nov 27 07:19:40 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txCc = QtGui.QDoubleSpinBox(Dialog)
        self.txCc.setDecimals(4)
        self.txCc.setMaximum(9999.9999)
        self.txCc.setObjectName(_fromUtf8("txCc"))
        self.gridLayout.addWidget(self.txCc, 2, 1, 1, 1)
        self.chTemp = QtGui.QCheckBox(Dialog)
        self.chTemp.setEnabled(False)
        self.chTemp.setObjectName(_fromUtf8("chTemp"))
        self.gridLayout.addWidget(self.chTemp, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.chPPB = QtGui.QCheckBox(Dialog)
        self.chPPB.setEnabled(False)
        self.chPPB.setObjectName(_fromUtf8("chPPB"))
        self.gridLayout.addWidget(self.chPPB, 4, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.btnConfPPB = QtGui.QPushButton(Dialog)
        self.btnConfPPB.setObjectName(_fromUtf8("btnConfPPB"))
        self.gridLayout.addWidget(self.btnConfPPB, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.btnConfTemp = QtGui.QPushButton(Dialog)
        self.btnConfTemp.setObjectName(_fromUtf8("btnConfTemp"))
        self.gridLayout.addWidget(self.btnConfTemp, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Produtividade potencial bruta (PPB)", None))
        self.chTemp.setText(_translate("Dialog", "Configurado", None))
        self.label_2.setText(_translate("Dialog", "Série de imagens de PPB", None))
        self.label_3.setText(_translate("Dialog", "Dados de entrada:", None))
        self.chPPB.setText(_translate("Dialog", "Configurado", None))
        self.label_4.setText(_translate("Dialog", "Configuração de saída", None))
        self.btnConfPPB.setText(_translate("Dialog", "Configurar", None))
        self.label_5.setText(_translate("Dialog", "Indice de colheita", None))
        self.label.setText(_translate("Dialog", "Série de imagens de Temperatura", None))
        self.btnConfTemp.setText(_translate("Dialog", "Configurar", None))

