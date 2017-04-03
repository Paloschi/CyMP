# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgETc.ui'
#
# Created: Wed Nov 11 00:58:52 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controle.ConEtc import Controller

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
        

        Dialog.resize(371, 290)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)      
        self.gridLayout = QtGui.QGridLayout()
        self.verticalLayout.addLayout(self.gridLayout)
        
        self.rbEtc = QtGui.QRadioButton(Dialog)
        self.gridLayout.addWidget(self.rbEtc, 0,0,1,1)
        self.rbEtc.setChecked(True)

        self.rbEta = QtGui.QRadioButton(Dialog)
        self.gridLayout.addWidget(self.rbEta, 0,1,1,1)        
        
        self.label = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        
        self.label_2 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        
        self.btnConfET0 = QtGui.QPushButton(Dialog)
        self.gridLayout.addWidget(self.btnConfET0, 2, 1, 1, 1)
        
        self.chET0 = QtGui.QCheckBox(Dialog)
        self.chET0.setEnabled(False)
        self.gridLayout.addWidget(self.chET0, 2, 2, 1, 1)
        
        self.label_3 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        
        self.btnConfKc = QtGui.QPushButton(Dialog)
        self.gridLayout.addWidget(self.btnConfKc, 3, 1, 1, 1)
        
        self.chKc = QtGui.QCheckBox(Dialog)
        self.chKc.setEnabled(False)
        self.gridLayout.addWidget(self.chKc, 3, 2, 1, 1)
        
        self.label_4 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        
        self.label_5 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        
        self.btnConfETc = QtGui.QPushButton(Dialog)
        self.gridLayout.addWidget(self.btnConfETc, 5, 1, 1, 1)
        
        self.chETc = QtGui.QCheckBox(Dialog)
        self.chETc.setEnabled(False)
        self.gridLayout.addWidget(self.chETc, 5, 2, 1, 1)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        

        
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.controller.action_ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.controller.action_cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.btnConfET0.clicked.connect(self.controller.setSerieET0)
        self.btnConfKc.clicked.connect(self.controller.setSerie_Kc)
        self.btnConfETc.clicked.connect(self.controller.setSerie_ETc)
        
        self.rbEta.clicked.connect(self.controller.MudaPraETa)
        self.rbEtc.clicked.connect(self.controller.MudaPraETc)
        
        #self.controller.parametros_teste()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - Evapotranspiração", None))
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
        
        self.rbEta.setText(_translate("Dialog", "ETa (FAO)", None))
        self.rbEtc.setText(_translate("Dialog", "ETc", None))

