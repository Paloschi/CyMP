# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Paloschi\Desktop\Gafanhoto\Software\Gafanhoto_1.0\InterfacesQT\DlgFiltroSavitzGolay.ui'
#
# Created: Fri Jun 12 14:10:00 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controle import ConFiltroSavitzGolay

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

class Ui_DlgSavitzGolay(QtGui.QDialog):
    def setupUi(self, DlgSavitzGolay):
        
        self.controller = ConFiltroSavitzGolay.Controller(self);
        
        DlgSavitzGolay.setObjectName(_fromUtf8("DlgSavitzGolay"))
        DlgSavitzGolay.setWindowModality(QtCore.Qt.WindowModal)
        DlgSavitzGolay.resize(371, 278)
        DlgSavitzGolay.setMinimumSize(QtCore.QSize(50, 0))
        DlgSavitzGolay.setSizeIncrement(QtCore.QSize(1, 0))
        DlgSavitzGolay.setBaseSize(QtCore.QSize(50, 0))
        DlgSavitzGolay.setStyleSheet(_fromUtf8(""))
        self.tabWidget = QtGui.QTabWidget(DlgSavitzGolay)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 351, 201))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 51))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leInFolder = QtGui.QLineEdit(self.gridLayoutWidget)
        self.leInFolder.setObjectName(_fromUtf8("leInFolder"))
        self.gridLayout.addWidget(self.leInFolder, 0, 1, 1, 1)
        self.toolbFindInFolder = QtGui.QToolButton(self.gridLayoutWidget)
        self.toolbFindInFolder.setObjectName(_fromUtf8("toolbFindInFolder"))
        self.gridLayout.addWidget(self.toolbFindInFolder, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 161))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.leWindowSize = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.leWindowSize.setObjectName(_fromUtf8("leWindowSize"))
        self.gridLayout_2.addWidget(self.leWindowSize, 0, 1, 1, 1)
        self.leOrdem = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.leOrdem.setObjectName(_fromUtf8("leOrdem"))
        self.gridLayout_2.addWidget(self.leOrdem, 1, 1, 1, 1)
        self.leNullValue = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.leNullValue.setInputMask(_fromUtf8(""))
        self.leNullValue.setObjectName(_fromUtf8("leNullValue"))
        
        self.leNullValue.setEnabled(False)
        
        self.gridLayout_2.addWidget(self.leNullValue, 2, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_2.addWidget(self.checkBox, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 331, 100))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.toolbFindOutFolder = QtGui.QToolButton(self.gridLayoutWidget_4)
        self.toolbFindOutFolder.setObjectName(_fromUtf8("toolbFindOutFolder"))
        self.gridLayout_4.addWidget(self.toolbFindOutFolder, 0, 2, 1, 1)
        self.leOutFolder = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.leOutFolder.setObjectName(_fromUtf8("leOutFolder"))
        self.gridLayout_4.addWidget(self.leOutFolder, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayoutWidget = QtGui.QWidget(DlgSavitzGolay)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 351, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.bbOkCancel = QtGui.QDialogButtonBox(self.horizontalLayoutWidget)
        self.bbOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.bbOkCancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.bbOkCancel.setObjectName(_fromUtf8("bbOkCancel"))
        self.horizontalLayout.addWidget(self.bbOkCancel)

        self.retranslateUi(DlgSavitzGolay)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.bbOkCancel, QtCore.SIGNAL(_fromUtf8("accepted()")), self.controller.action_ok)
        QtCore.QObject.connect(self.bbOkCancel, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgSavitzGolay.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgSavitzGolay)

    def retranslateUi(self, DlgEstimativaDatasAgricolas):
        DlgEstimativaDatasAgricolas.setWindowTitle(_translate("DlgEstimativaDatasAgricolas", "Filtro Savitz Golay", None))
        self.toolbFindInFolder.setText(_translate("DlgEstimativaDatasAgricolas", "...", None))
        self.label.setText(_translate("DlgEstimativaDatasAgricolas", "Pasta de entrada das imagens:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DlgEstimativaDatasAgricolas", "Dados de pasta", None))
        self.label_2.setText(_translate("DlgEstimativaDatasAgricolas", "Ordem:", None))
        self.label_9.setText(_translate("DlgEstimativaDatasAgricolas", "Tamanho da janela:", None))
        self.leWindowSize.setText(_translate("DlgEstimativaDatasAgricolas", "5", None))
        self.leOrdem.setText(_translate("DlgEstimativaDatasAgricolas", "3", None))
        self.label_14.setText(_translate("DlgEstimativaDatasAgricolas", "Valor Nulo:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DlgEstimativaDatasAgricolas", "Configuração", None))
        self.label_8.setText(_translate("DlgEstimativaDatasAgricolas", "Pasta de saída das imagens:", None))
        self.toolbFindOutFolder.setText(_translate("DlgEstimativaDatasAgricolas", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DlgEstimativaDatasAgricolas", "Dados de saída", None))
        
        
        self.leInFolder.setText("C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\entrada_pesada")
        self.leOutFolder.setText("C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\saida")
        
        self.checkBox.clicked.connect(self.controller.actionCheckBox)
        self.toolbFindInFolder.clicked.connect(self.controller.findInFolder)
        self.toolbFindOutFolder.clicked.connect(self.controller.findOutFolder)