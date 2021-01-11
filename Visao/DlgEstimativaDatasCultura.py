# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgEstimativaDatasCultura.ui'
#
# Created: Thu Jun 11 16:55:09 2015
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Controle.ConEstimativaDatasCultura import Controller
#import ConfigParser

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

class Ui_DlgEstimativaDatasAgricolas(QtWidgets.QDialog):

    
    def setupUi(self, DlgEstimativaDatasAgricolas):
        
        self.controller = Controller(self);
        
        DlgEstimativaDatasAgricolas.setObjectName(_fromUtf8("DlgEstimativaDatasAgricolas"))
        DlgEstimativaDatasAgricolas.setWindowModality(QtCore.Qt.WindowModal)
        DlgEstimativaDatasAgricolas.resize(371, 278)
        DlgEstimativaDatasAgricolas.setMinimumSize(QtCore.QSize(50, 0))
        DlgEstimativaDatasAgricolas.setSizeIncrement(QtCore.QSize(1, 0))
        DlgEstimativaDatasAgricolas.setBaseSize(QtCore.QSize(50, 0))
        DlgEstimativaDatasAgricolas.setStyleSheet(_fromUtf8(""))
        
        self.tabWidget = QtWidgets.QTabWidget(DlgEstimativaDatasAgricolas)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 351, 201))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 51))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.leInFolder = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.leInFolder.setObjectName(_fromUtf8("leInFolder"))
        self.gridLayout.addWidget(self.leInFolder, 0, 1, 1, 1)
        

        self.toolbFindInFolder = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolbFindInFolder.setObjectName(_fromUtf8("toolbFindInFolder"))
        self.gridLayout.addWidget(self.toolbFindInFolder, 0, 2, 1, 1)
        
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 311, 71))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        
        self.leSufixo = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.leSufixo.setObjectName(_fromUtf8("leSufixo"))
        self.gridLayout_3.addWidget(self.leSufixo, 1, 1, 1, 1)
        
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        
        self.lePrefixo = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lePrefixo.setObjectName(_fromUtf8("lePrefixo"))
        self.gridLayout_3.addWidget(self.lePrefixo, 0, 1, 1, 1)
        
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        
        self.leMascara = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.leMascara.setAutoFillBackground(False)
        self.leMascara.setObjectName(_fromUtf8("leMascara"))
        self.gridLayout_3.addWidget(self.leMascara, 0, 3, 1, 1)
        
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 161))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.dspASemeadura = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.dspASemeadura.setMinimum(-99.99)
        self.dspASemeadura.setObjectName(_fromUtf8("dspASemeadura"))
        self.gridLayout_2.addWidget(self.dspASemeadura, 3, 1, 1, 1)
        
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        
        self.dsbAColheita = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.dsbAColheita.setMinimum(-99.99)
        self.dsbAColheita.setObjectName(_fromUtf8("dsbAColheita"))
        self.gridLayout_2.addWidget(self.dsbAColheita, 4, 1, 1, 1)
        
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        
        self.lePSemeadura = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lePSemeadura.setObjectName(_fromUtf8("lePSemeadura"))
        self.gridLayout_2.addWidget(self.lePSemeadura, 0, 1, 1, 1)
        
        self.lePPico = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lePPico.setObjectName(_fromUtf8("lePPico"))
        self.gridLayout_2.addWidget(self.lePPico, 1, 1, 1, 1)
        
        self.lePColheita = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lePColheita.setObjectName(_fromUtf8("lePColheita"))
        self.gridLayout_2.addWidget(self.lePColheita, 2, 1, 1, 1)
        
        self.leNullValue = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.leNullValue.setInputMask(_fromUtf8(""))
        self.leNullValue.setObjectName(_fromUtf8("leNullValue"))
        
        regexp = QtCore.QRegExp("[0-9]\\d{0,5}")
        validator = QtGui.QRegExpValidator(regexp)
        self.leNullValue.setValidator(validator)
        
        self.gridLayout_2.addWidget(self.leNullValue, 5, 1, 1, 1)
        
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 5, 0, 1, 1)
        
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 331, 100))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        
        self.toolbFindOutFolder = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.toolbFindOutFolder.setObjectName(_fromUtf8("toolbFindOutFolder"))
        self.gridLayout_4.addWidget(self.toolbFindOutFolder, 0, 2, 1, 1)
        
        self.leOutFolder = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.leOutFolder.setObjectName(_fromUtf8("leOutFolder"))
        self.gridLayout_4.addWidget(self.leOutFolder, 0, 1, 1, 1)
        
        self.leImgPico = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.leImgPico.setObjectName(_fromUtf8("leImgPico"))
        self.gridLayout_4.addWidget(self.leImgPico, 2, 1, 1, 1)
        
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        
        self.leImgSemeadura = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.leImgSemeadura.setObjectName(_fromUtf8("leImgSemeadura"))
        self.gridLayout_4.addWidget(self.leImgSemeadura, 1, 1, 1, 1)
        
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_4.addWidget(self.label_13, 3, 0, 1, 1)
        
        self.leImgColheita = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.leImgColheita.setObjectName(_fromUtf8("leImgColheita"))
        self.gridLayout_4.addWidget(self.leImgColheita, 3, 1, 1, 1)
        
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayoutWidget = QtWidgets.QWidget(DlgEstimativaDatasAgricolas)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 351, 41))
        
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        #self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        #self.progressBar.setProperty("value", 0)
        #self.progressBar.setMinimum(1)
        #self.progressBar.setMaximum(100)
        #self.progressBar.setObjectName(_fromUtf8("progressBar"))
        #self.horizontalLayout.addWidget(self.progressBar)
        
        self.bbOkCancel = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        self.bbOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.bbOkCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bbOkCancel.setObjectName(_fromUtf8("bbOkCancel"))
        self.horizontalLayout.addWidget(self.bbOkCancel)
        
        self.retranslateUi(DlgEstimativaDatasAgricolas)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.bbOkCancel, QtCore.SIGNAL(_fromUtf8("accepted()")), self.controller.action_ok)
        QtCore.QObject.connect(self.bbOkCancel, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgEstimativaDatasAgricolas.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgEstimativaDatasAgricolas)
        
        self.dsbAColheita.value()
        
        self.controller.parametros_teste()

    def retranslateUi(self, DlgEstimativaDatasAgricolas):
        
        DlgEstimativaDatasAgricolas.setWindowTitle(_translate("DlgEstimativaDatasAgricolas", "CyMP - Estimativa de datas da cultura", None))
        self.toolbFindInFolder.setText(_translate("DlgEstimativaDatasAgricolas", "...", None))
        self.label.setText(_translate("DlgEstimativaDatasAgricolas", "Pasta de entrada das imagens:", None))
        self.label_6.setText(_translate("DlgEstimativaDatasAgricolas", "Sufixo:", None))
        self.label_7.setText(_translate("DlgEstimativaDatasAgricolas", "Máscara:", None))
        self.label_5.setText(_translate("DlgEstimativaDatasAgricolas", "Prefixo:", None))
        self.leMascara.setText(_translate("DlgEstimativaDatasAgricolas", "%Y%m%d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DlgEstimativaDatasAgricolas", "Dados de pasta", None))
        self.label_4.setText(_translate("DlgEstimativaDatasAgricolas", "Avanço colheita:", None))
        self.label_2.setText(_translate("DlgEstimativaDatasAgricolas", "Posição DMDV:", None))
        self.label_10.setText(_translate("DlgEstimativaDatasAgricolas", "Posição Colheita:", None))
        self.label_3.setText(_translate("DlgEstimativaDatasAgricolas", "Avanço semeadura:", None))
        self.label_9.setText(_translate("DlgEstimativaDatasAgricolas", "Posição Semeadura:", None))
        self.lePSemeadura.setText(_translate("DlgEstimativaDatasAgricolas", "29-45", None))
        self.lePPico.setText(_translate("DlgEstimativaDatasAgricolas", "34-54", None))
        self.lePColheita.setText(_translate("DlgEstimativaDatasAgricolas", "45-59", None))
        self.label_14.setText(_translate("DlgEstimativaDatasAgricolas", "Valor Nulo:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DlgEstimativaDatasAgricolas", "Configuração", None))
        self.label_12.setText(_translate("DlgEstimativaDatasAgricolas", "Nome imagem de DMDV:", None))
        self.label_8.setText(_translate("DlgEstimativaDatasAgricolas", "Pasta de saída das imagens:", None))
        self.toolbFindOutFolder.setText(_translate("DlgEstimativaDatasAgricolas", "...", None))
        self.label_11.setText(_translate("DlgEstimativaDatasAgricolas", "Nome imagem de Semeadura", None))
        self.label_13.setText(_translate("DlgEstimativaDatasAgricolas", "Nome imagem de colheita:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DlgEstimativaDatasAgricolas", "Dados de saída", None))
        
        self.leImgSemeadura.setText("semeadura")
        self.leImgPico.setText("DMDV")
        self.leImgColheita.setText("colheita")
        self.lePrefixo.setText("")
        self.leSufixo.setText("")
        self.leNullValue.setText("0")
        
                
        #self.config = ConfigParser.RawConfigParser()
        #self.config.read('workspace.properties')
        
        #workspace = self.config.get('WorkSpace', 'space.default')
        #raster = workspace + self.config.get('WorkSpace', 'space.raster')
        #out = workspace + self.config.get('WorkSpace', 'space.out')
        
        #self.leInFolder.setText(raster)
        #self.leOutFolder.setText(out)
        
        self.toolbFindInFolder.clicked.connect(self.controller.findInFolder)
        self.toolbFindOutFolder.clicked.connect(self.controller.findOutFolder)
        