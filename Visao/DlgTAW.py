# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgTAW.ui'
#
# Created: Wed Nov 11 04:59:25 2015
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Controle.ConTAW import Controller

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

        try:
            self.controller = Controller(self)

            Dialog.setObjectName(_fromUtf8("Dialog"))
            Dialog.resize(460, 243)
            self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
            self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
            self.gridLayout = QtWidgets.QGridLayout()
            self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
            self.label_2 = QtWidgets.QLabel(Dialog)
            self.label_2.setObjectName(_fromUtf8("label_2"))
            self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
            self.label = QtWidgets.QLabel(Dialog)
            self.label.setObjectName(_fromUtf8("label"))
            self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
            self.chZr = QtWidgets.QCheckBox(Dialog)
            self.chZr.setEnabled(False)
            self.chZr.setObjectName(_fromUtf8("chZr"))
            self.gridLayout.addWidget(self.chZr, 2, 2, 1, 1)
            self.label_4 = QtWidgets.QLabel(Dialog)
            self.label_4.setObjectName(_fromUtf8("label_4"))
            self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
            self.btnConfTAW = QtWidgets.QPushButton(Dialog)
            self.btnConfTAW.setObjectName(_fromUtf8("btnConfTAW"))
            self.gridLayout.addWidget(self.btnConfTAW, 5, 1, 1, 1)
            self.label_5 = QtWidgets.QLabel(Dialog)
            self.label_5.setObjectName(_fromUtf8("label_5"))
            self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
            self.chTAW = QtWidgets.QCheckBox(Dialog)
            self.chTAW.setEnabled(False)
            self.chTAW.setObjectName(_fromUtf8("chTAW"))
            self.gridLayout.addWidget(self.chTAW, 5, 2, 1, 1)
            self.label_3 = QtWidgets.QLabel(Dialog)
            self.label_3.setObjectName(_fromUtf8("label_3"))
            self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
            self.txImgCAD = QtWidgets.QLineEdit(Dialog)
            self.txImgCAD.setObjectName(_fromUtf8("txImgCAD"))
            self.gridLayout.addWidget(self.txImgCAD, 1, 1, 1, 1)
            self.btnConfZr = QtWidgets.QPushButton(Dialog)
            self.btnConfZr.setObjectName(_fromUtf8("btnConfZr"))
            self.gridLayout.addWidget(self.btnConfZr, 2, 1, 1, 1)
            self.btnFindImgCAD = QtWidgets.QToolButton(Dialog)
            self.btnFindImgCAD.setObjectName(_fromUtf8("btnFindImgCAD"))
            self.gridLayout.addWidget(self.btnFindImgCAD, 1, 2, 1, 1)

            self.lblPValor = QtWidgets.QLabel(Dialog)
            self.lblPValor.setObjectName(_fromUtf8("lblPValor"))
            self.gridLayout.addWidget(self.lblPValor, 3, 0, 1, 1)
            self.txPvalor = QtWidgets.QDoubleSpinBox(Dialog)
            self.txPvalor.setDecimals(4)
            self.txPvalor.setMaximum(1.0)
            self.txPvalor.setEnabled(False)
            self.txPvalor.setObjectName(_fromUtf8("txPvalor"))
            self.gridLayout.addWidget(self.txPvalor, 3, 1, 1, 1)
            self.chPValor = QtWidgets.QCheckBox(Dialog)
            self.chPValor.setObjectName(_fromUtf8("chPValor"))
            self.gridLayout.addWidget(self.chPValor, 3, 2, 1, 1)

            self.label_desc = QtWidgets.QLabel(Dialog)
            self.label_desc.setObjectName(_fromUtf8("label_3"))
            self.gridLayout.addWidget(self.label_desc, 6, 0, 1, 1)

            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

            self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
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

            self.btnConfTAW.clicked.connect(self.controller.setSerie_TAW)
            self.btnConfZr.clicked.connect(self.controller.setSerieZr)
            self.btnFindImgCAD.clicked.connect(self.controller.findImgCAD)

            self.chPValor.clicked.connect(self.controller.habilitaPValue)

            self.controller.parametros_teste()

        except Exception as e:
            print(e)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - TAW/RAW", None))
        self.label_2.setText(_translate("Dialog", "Série de imagens de Zr:", None))
        self.label.setText(_translate("Dialog", "Imagem de CAD:", None))
        self.chZr.setText(_translate("Dialog", "configurado", None))
        self.label_4.setText(_translate("Dialog", "Configuração de saída:", None))
        self.btnConfTAW.setText(_translate("Dialog", "configurar", None))
        self.label_5.setText(_translate("Dialog", "Série de imagens TAW/RAW", None))
        self.chTAW.setText(_translate("Dialog", "configurado", None))
        self.label_3.setText(_translate("Dialog", "Configuração de entrada:", None))
        self.btnConfZr.setText(_translate("Dialog", "configurar", None))
        self.btnFindImgCAD.setText(_translate("Dialog", "...", None))
        
        self.chPValor.setText(_translate("Dialog", "Habilitado", None))
        self.lblPValor.setText(_translate("Dialog", "Coeficiente p (RAW)", None))
        
        self.label_desc.setText(_translate("Dialog", "Use o valor p para a RAW!", None))
        
        

