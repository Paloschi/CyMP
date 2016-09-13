# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgDistribuidorDeIndice.ui'
#
# Created: Mon Oct 19 07:14:46 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controle.ConDistribuidorDeIndice import Controller

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

class Ui_DistribuidorDeIndice(QtGui.QDialog):
    def setupUi(self, Dialog):
        
        self.controller = Controller(self)
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(437, 332)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(26, 44, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.btFindImgSemeadura = QtGui.QToolButton(Dialog)
        self.btFindImgSemeadura.setGeometry(QtCore.QRect(370, 40, 25, 19))
        self.btFindImgSemeadura.setObjectName(_fromUtf8("btFindImgSemeadura"))
        self.btFindOutFolder = QtGui.QToolButton(Dialog)
        self.btFindOutFolder.setGeometry(QtCore.QRect(370, 130, 25, 19))
        self.btFindOutFolder.setObjectName(_fromUtf8("btFindOutFolder"))
        self.txOutFolder = QtGui.QLineEdit(Dialog)
        self.txOutFolder.setGeometry(QtCore.QRect(146, 130, 211, 20))
        self.txOutFolder.setObjectName(_fromUtf8("txOutFolder"))
        self.txImgSemeadura = QtGui.QLineEdit(Dialog)
        self.txImgSemeadura.setGeometry(QtCore.QRect(146, 40, 211, 20))
        self.txImgSemeadura.setObjectName(_fromUtf8("txImgSemeadura"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(26, 134, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btOkCancel = QtGui.QDialogButtonBox(Dialog)
        self.btOkCancel.setGeometry(QtCore.QRect(30, 300, 401, 23))
        self.btOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.btOkCancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btOkCancel.setObjectName(_fromUtf8("btOkCancel"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 170, 261, 111))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        self.tableWidget.rowCount()
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        self.btRemover = QtGui.QPushButton(Dialog)
        self.btRemover.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.btRemover.setObjectName(_fromUtf8("btRemover"))
        self.btAdicionar = QtGui.QPushButton(Dialog)
        self.btAdicionar.setGeometry(QtCore.QRect(300, 230, 75, 23))
        self.btAdicionar.setObjectName(_fromUtf8("btAdicionar"))
                                                  
        self.txMultiplyFactor = QtGui.QSpinBox(Dialog)
        self.txMultiplyFactor.setMaximum(10000)
        self.txMultiplyFactor.setGeometry(QtCore.QRect(146, 100, 211, 20))
        self.txMultiplyFactor.setObjectName(_fromUtf8("txMultiplyFactor"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(26, 100, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        #self.btFindImgPico = QtGui.QToolButton(Dialog)
        #self.btFindImgPico.setGeometry(QtCore.QRect(370, 70, 25, 19))
        #self.btFindImgPico.setObjectName(_fromUtf8("btFindImgPico"))
        self.txImgColheita = QtGui.QLineEdit(Dialog)
        self.txImgColheita.setGeometry(QtCore.QRect(146, 70, 211, 20))
        self.txImgColheita.setObjectName(_fromUtf8("txImgColheita"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(26, 70, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btFindImgColheita = QtGui.QToolButton(Dialog)
        self.btFindImgColheita.setGeometry(QtCore.QRect(370, 70, 25, 19))
        self.btFindImgColheita.setObjectName(_fromUtf8("btFindImgColheita"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(300, 170, 121, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 10, 208, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btOkCancel, QtCore.SIGNAL(_fromUtf8("accepted()")), self.controller.action_ok)
        QtCore.QObject.connect(self.btOkCancel, QtCore.SIGNAL(_fromUtf8("rejected()")), self.controller.action_cancel)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - Distribuidor de índice.", None))
        self.label.setText(_translate("Dialog", "Imagem de semeadura", None))
        self.btFindImgSemeadura.setText(_translate("Dialog", "...", None))
        self.btFindOutFolder.setText(_translate("Dialog", "...", None))
        self.label_2.setText(_translate("Dialog", "Pasta de saída:", None))
        
        
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Estádio 1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        self.tableWidget.setColumnWidth(0, 60)
        item.setText(_translate("Dialog", "Dia inicial", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        self.tableWidget.setColumnWidth(1, 60)
        item.setText(_translate("Dialog", "Dia final", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        self.tableWidget.setColumnWidth(2, 60)
        item.setText(_translate("Dialog", "Valor", None))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "1", None))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "1", None))
        #self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.btRemover.setText(_translate("Dialog", "Remover", None))
        self.btAdicionar.setText(_translate("Dialog", "Adicionar", None))
        self.label_3.setText(_translate("Dialog", "Fator multiplicador:", None))
        #self.btFindImgPico.setText(_translate("Dialog", "...", None))
        self.label_4.setText(_translate("Dialog", "Imagem de colheita:", None))
        self.btFindImgColheita.setText(_translate("Dialog", "...", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Kc FAO - Soja", None))
        self.comboBox.setItemText(2, _translate("Dialog", "Zr FAO - Soja", None))
        self.label_5.setText(_translate("Dialog", "Distribuidor de índice por Estádio fenológico", None))
        self.txMultiplyFactor.setValue(100)
        
        self.btFindImgSemeadura.clicked.connect(self.controller.findImgSemeadura)
        self.btFindOutFolder.clicked.connect(self.controller.findOutFolder)
        #self.btFindImgPico.clicked.connect(self.controller.findImgPico)
        self.btFindImgColheita.clicked.connect(self.controller.findImgColheita)
        
        self.comboBox.currentIndexChanged.connect(self.controller.changeDefaultIndices)
        
        self.btAdicionar.clicked.connect(self.controller.addEstagio)
        self.btRemover.clicked.connect(self.controller.remEstagio)
        
        self.txImgColheita.setText("C:\\Users\\PGSERE16\\Desktop\\2013-2014\\colheita.tif")
        self.txImgSemeadura.setText("C:\\Users\\PGSERE16\\Desktop\\2013-2014\\semeadura.tif")
        self.txOutFolder.setText("C:\\Users\\PGSERE16\\Desktop\\Indices_distribuidos_teste\\")

