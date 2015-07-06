# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgEstatisticasEspectrais.ui'
#
# Created: Wed Jul 01 11:12:16 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controllers import ConEstatisticasEspectrais

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

class Ui_DlgEstatisticasEspectrais(QtGui.QDialog):
    def setupUi(self, DlgEstatisticasEspectrais):
        
        self.controller = ConEstatisticasEspectrais.Controller(self)
        
        DlgEstatisticasEspectrais.setObjectName(_fromUtf8("DlgEstatisticasEspectrais"))
        DlgEstatisticasEspectrais.setWindowModality(QtCore.Qt.WindowModal)
        DlgEstatisticasEspectrais.resize(359, 272)
        DlgEstatisticasEspectrais.setMinimumSize(QtCore.QSize(50, 0))
        DlgEstatisticasEspectrais.setSizeIncrement(QtCore.QSize(1, 0))
        DlgEstatisticasEspectrais.setBaseSize(QtCore.QSize(50, 0))
        DlgEstatisticasEspectrais.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(DlgEstatisticasEspectrais)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(DlgEstatisticasEspectrais)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leInFolder = QtGui.QLineEdit(self.tab_3)
        self.leInFolder.setObjectName(_fromUtf8("leInFolder"))
        self.gridLayout.addWidget(self.leInFolder, 0, 1, 1, 1)
        self.toolbFindInFolder = QtGui.QToolButton(self.tab_3)
        self.toolbFindInFolder.setObjectName(_fromUtf8("toolbFindInFolder"))
        self.gridLayout.addWidget(self.toolbFindInFolder, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.toolbFindOutFolder = QtGui.QToolButton(self.tab_2)
        self.toolbFindOutFolder.setObjectName(_fromUtf8("toolbFindOutFolder"))
        self.gridLayout_4.addWidget(self.toolbFindOutFolder, 0, 2, 1, 1)
        self.leOutFolder = QtGui.QLineEdit(self.tab_2)
        self.leOutFolder.setObjectName(_fromUtf8("leOutFolder"))
        self.gridLayout_4.addWidget(self.leOutFolder, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbSD = QtGui.QCheckBox(self.tab)
        self.cbSD.setObjectName(_fromUtf8("cbSD"))
        self.gridLayout_2.addWidget(self.cbSD, 1, 0, 1, 1)
        self.cbMedia = QtGui.QCheckBox(self.tab)
        self.cbMedia.setObjectName(_fromUtf8("cbMedia"))
        self.gridLayout_2.addWidget(self.cbMedia, 0, 0, 1, 1)
        self.cbModa = QtGui.QCheckBox(self.tab)
        self.cbModa.setObjectName(_fromUtf8("cbModa"))
        self.gridLayout_2.addWidget(self.cbModa, 3, 0, 1, 1)
        self.cbMin = QtGui.QCheckBox(self.tab)
        self.cbMin.setObjectName(_fromUtf8("cbMin"))
        self.gridLayout_2.addWidget(self.cbMin, 0, 1, 1, 1)
        self.cbCV = QtGui.QCheckBox(self.tab)
        self.cbCV.setObjectName(_fromUtf8("cbCV"))
        self.gridLayout_2.addWidget(self.cbCV, 2, 0, 1, 1)
        self.cbMax = QtGui.QCheckBox(self.tab)
        self.cbMax.setObjectName(_fromUtf8("cbMax"))
        self.gridLayout_2.addWidget(self.cbMax, 1, 1, 1, 1)
        self.cbSoma = QtGui.QCheckBox(self.tab)
        self.cbSoma.setObjectName(_fromUtf8("cbSoma"))
        self.gridLayout_2.addWidget(self.cbSoma, 2, 1, 1, 1)
        self.cbMediana = QtGui.QCheckBox(self.tab)
        self.cbMediana.setObjectName(_fromUtf8("cbMediana"))
        self.gridLayout_2.addWidget(self.cbMediana, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bbOkCancel = QtGui.QDialogButtonBox(DlgEstatisticasEspectrais)
        self.bbOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.bbOkCancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.bbOkCancel.setObjectName(_fromUtf8("bbOkCancel"))
        self.horizontalLayout.addWidget(self.bbOkCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DlgEstatisticasEspectrais)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.bbOkCancel, QtCore.SIGNAL(_fromUtf8("accepted()")), self.controller.action_ok)
        QtCore.QObject.connect(self.bbOkCancel, QtCore.SIGNAL(_fromUtf8("rejected()")), self.controller.action_cancel)
        QtCore.QMetaObject.connectSlotsByName(DlgEstatisticasEspectrais)

    def retranslateUi(self, DlgEstatisticasEspectrais):
        DlgEstatisticasEspectrais.setWindowTitle(_translate("DlgEstatisticasEspectrais", "Estatisticas espectrais", None))
        self.toolbFindInFolder.setText(_translate("DlgEstatisticasEspectrais", "...", None))
        self.label.setText(_translate("DlgEstatisticasEspectrais", "Pasta de entrada das imagens:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DlgEstatisticasEspectrais", "Dados de pasta", None))
        self.label_8.setText(_translate("DlgEstatisticasEspectrais", "Pasta de saída das imagens:", None))
        self.toolbFindOutFolder.setText(_translate("DlgEstatisticasEspectrais", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DlgEstatisticasEspectrais", "Dados de saída", None))
        self.cbSD.setText(_translate("DlgEstatisticasEspectrais", "Desvio padrão", None))
        self.cbMedia.setText(_translate("DlgEstatisticasEspectrais", "Media", None))
        self.cbModa.setText(_translate("DlgEstatisticasEspectrais", "Moda", None))
        self.cbMin.setText(_translate("DlgEstatisticasEspectrais", "Mínimo", None))
        self.cbCV.setText(_translate("DlgEstatisticasEspectrais", "Coeficiente de variação", None))
        self.cbMax.setText(_translate("DlgEstatisticasEspectrais", "Máximo", None))
        self.cbSoma.setText(_translate("DlgEstatisticasEspectrais", "Soma", None))
        self.cbMediana.setText(_translate("DlgEstatisticasEspectrais", "Mediana", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DlgEstatisticasEspectrais", "Configuração", None))
        
        self.cbModa.setEnabled(False)
        
        self.leInFolder.setText("C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\entrada")
        self.leOutFolder.setText("C:\\Users\\Paloschi\\Desktop\\data\\Ajuste extrator de estatisticas\\saida_teste")
        

        self.toolbFindInFolder.clicked.connect(self.controller.findInFolder)
        self.toolbFindOutFolder.clicked.connect(self.controller.findOutFolder)
