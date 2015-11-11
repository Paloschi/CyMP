# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgDr.ui'
#
# Created: Wed Nov 11 04:59:35 2015
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
        Dialog.resize(451, 273)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chTAW = QtGui.QCheckBox(Dialog)
        self.chTAW.setEnabled(False)
        self.chTAW.setObjectName(_fromUtf8("chTAW"))
        self.gridLayout.addWidget(self.chTAW, 3, 2, 1, 1)
        self.btnConfPPP = QtGui.QPushButton(Dialog)
        self.btnConfPPP.setObjectName(_fromUtf8("btnConfPPP"))
        self.gridLayout.addWidget(self.btnConfPPP, 2, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.chDr = QtGui.QCheckBox(Dialog)
        self.chDr.setEnabled(False)
        self.chDr.setObjectName(_fromUtf8("chDr"))
        self.gridLayout.addWidget(self.chDr, 5, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.btnConfTAW = QtGui.QPushButton(Dialog)
        self.btnConfTAW.setObjectName(_fromUtf8("btnConfTAW"))
        self.gridLayout.addWidget(self.btnConfTAW, 3, 1, 1, 1)
        self.btnConfETc = QtGui.QPushButton(Dialog)
        self.btnConfETc.setObjectName(_fromUtf8("btnConfETc"))
        self.gridLayout.addWidget(self.btnConfETc, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.chPPP = QtGui.QCheckBox(Dialog)
        self.chPPP.setEnabled(False)
        self.chPPP.setObjectName(_fromUtf8("chPPP"))
        self.gridLayout.addWidget(self.chPPP, 2, 2, 1, 1)
        self.BtnConfDr = QtGui.QPushButton(Dialog)
        self.BtnConfDr.setObjectName(_fromUtf8("BtnConfDr"))
        self.gridLayout.addWidget(self.BtnConfDr, 5, 1, 1, 1)
        self.chEtc = QtGui.QCheckBox(Dialog)
        self.chEtc.setEnabled(False)
        self.chEtc.setObjectName(_fromUtf8("chEtc"))
        self.gridLayout.addWidget(self.chEtc, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
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
        Dialog.setWindowTitle(_translate("Dialog", "Valor de esgotamento (Dr)", None))
        self.chTAW.setText(_translate("Dialog", "configurado", None))
        self.btnConfPPP.setText(_translate("Dialog", "configurar", None))
        self.label.setText(_translate("Dialog", "Configuração de entrada:", None))
        self.chDr.setText(_translate("Dialog", "configurado", None))
        self.label_2.setText(_translate("Dialog", "Série de imagens de Etc:", None))
        self.label_3.setText(_translate("Dialog", "Série de imagens de Precipitção:", None))
        self.label_4.setText(_translate("Dialog", "Série de imagens TAW:", None))
        self.label_5.setText(_translate("Dialog", "Configuração de saída:", None))
        self.btnConfTAW.setText(_translate("Dialog", "configurar", None))
        self.btnConfETc.setText(_translate("Dialog", "configurar", None))
        self.label_6.setText(_translate("Dialog", "Série de Imagens de esgotamento:", None))
        self.chPPP.setText(_translate("Dialog", "configurado", None))
        self.BtnConfDr.setText(_translate("Dialog", "configurar", None))
        self.chEtc.setText(_translate("Dialog", "configurado", None))

