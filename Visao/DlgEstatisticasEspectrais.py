# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgEstatisticasEspectrais.ui'
#
# Created: Wed Jul 01 11:12:16 2015
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Controle import ConEstatisticasEspectrais

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

class Ui_DlgEstatisticasEspectrais(QtWidgets.QDialog):
    def setupUi(self, DlgEstatisticasEspectrais):
        
        self.controller = ConEstatisticasEspectrais.Controller(self)
        
        self.setObjectName(_fromUtf8("DlgEstatisticasEspectrais"))
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(359, 272)
        self.setMinimumSize(QtCore.QSize(50, 0))
        self.setSizeIncrement(QtCore.QSize(1, 0))
        self.setBaseSize(QtCore.QSize(50, 0))
        self.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtWidgets.QVBoxLayout(DlgEstatisticasEspectrais)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtWidgets.QTabWidget(DlgEstatisticasEspectrais)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leInFolder = QtWidgets.QLineEdit(self.tab_3)
        self.leInFolder.setObjectName(_fromUtf8("leInFolder"))
        self.gridLayout.addWidget(self.leInFolder, 0, 1, 1, 1)
        self.toolbFindInFolder = QtWidgets.QToolButton(self.tab_3)
        self.toolbFindInFolder.setObjectName(_fromUtf8("toolbFindInFolder"))
        self.gridLayout.addWidget(self.toolbFindInFolder, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.toolbFindOutFolder = QtWidgets.QToolButton(self.tab_2)
        self.toolbFindOutFolder.setObjectName(_fromUtf8("toolbFindOutFolder"))
        self.gridLayout_4.addWidget(self.toolbFindOutFolder, 0, 2, 1, 1)
        self.leOutFolder = QtWidgets.QLineEdit(self.tab_2)
        self.leOutFolder.setObjectName(_fromUtf8("leOutFolder"))
        self.gridLayout_4.addWidget(self.leOutFolder, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbSD = QtWidgets.QCheckBox(self.tab)
        self.cbSD.setObjectName(_fromUtf8("cbSD"))
        self.gridLayout_2.addWidget(self.cbSD, 1, 0, 1, 1)
        self.cbMedia = QtWidgets.QCheckBox(self.tab)
        self.cbMedia.setObjectName(_fromUtf8("cbMedia"))
        self.gridLayout_2.addWidget(self.cbMedia, 0, 0, 1, 1)
        self.cbAmplitude = QtWidgets.QCheckBox(self.tab)
        self.cbAmplitude.setObjectName(_fromUtf8("cbAmplitude"))
        self.gridLayout_2.addWidget(self.cbAmplitude, 3, 0, 1, 1)
        self.cbMin = QtWidgets.QCheckBox(self.tab)
        self.cbMin.setObjectName(_fromUtf8("cbMin"))
        self.gridLayout_2.addWidget(self.cbMin, 0, 1, 1, 1)
        self.cbCV = QtWidgets.QCheckBox(self.tab)
        self.cbCV.setObjectName(_fromUtf8("cbCV"))
        self.gridLayout_2.addWidget(self.cbCV, 2, 0, 1, 1)
        self.cbMax = QtWidgets.QCheckBox(self.tab)
        self.cbMax.setObjectName(_fromUtf8("cbMax"))
        self.gridLayout_2.addWidget(self.cbMax, 1, 1, 1, 1)
        self.cbSoma = QtWidgets.QCheckBox(self.tab)
        self.cbSoma.setObjectName(_fromUtf8("cbSoma"))
        self.gridLayout_2.addWidget(self.cbSoma, 2, 1, 1, 1)
        self.cbMediana = QtWidgets.QCheckBox(self.tab)
        self.cbMediana.setObjectName(_fromUtf8("cbMediana"))
        self.gridLayout_2.addWidget(self.cbMediana, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bbOkCancel = QtWidgets.QDialogButtonBox(self)
        self.bbOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.bbOkCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bbOkCancel.setObjectName(_fromUtf8("bbOkCancel"))
        self.horizontalLayout.addWidget(self.bbOkCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)

        self.bbOkCancel.accepted.connect(self.controller.action_ok)
        self.bbOkCancel.rejected.connect(self.controller.action_cancel)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.controller.parametros_teste()

    def retranslateUi(self, DlgEstatisticasEspectrais):
        print("teste retranslate")
        DlgEstatisticasEspectrais.setWindowTitle(_translate("DlgEstatisticasEspectrais", "CyMP - Estatísticas Descritivas (Perfil)", None))
        self.toolbFindInFolder.setText(_translate("DlgEstatisticasEspectrais", "...", None))
        self.label.setText(_translate("DlgEstatisticasEspectrais", "Pasta de entrada das imagens:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DlgEstatisticasEspectrais", "Dados de entrada", None))
        self.label_8.setText(_translate("DlgEstatisticasEspectrais", "Pasta de saída das imagens:", None))
        self.toolbFindOutFolder.setText(_translate("DlgEstatisticasEspectrais", "...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DlgEstatisticasEspectrais", "Dados de saída", None))
        self.cbSD.setText(_translate("DlgEstatisticasEspectrais", "Desvio padrão", None))
        self.cbMedia.setText(_translate("DlgEstatisticasEspectrais", "Média", None))
        self.cbAmplitude.setText(_translate("DlgEstatisticasEspectrais", "Amplitude", None))
        self.cbMin.setText(_translate("DlgEstatisticasEspectrais", "Mínimo", None))
        self.cbCV.setText(_translate("DlgEstatisticasEspectrais", "Coeficiente de variação", None))
        self.cbMax.setText(_translate("DlgEstatisticasEspectrais", "Máximo", None))
        self.cbSoma.setText(_translate("DlgEstatisticasEspectrais", "Soma", None))
        self.cbMediana.setText(_translate("DlgEstatisticasEspectrais", "Mediana", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DlgEstatisticasEspectrais", "Configuração", None))

        #self.leInFolder.setText("C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\entrada_pesada")
        #self.leOutFolder.setText("C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\saida")


        self.toolbFindInFolder.clicked.connect(self.controller.findInFolder)
        self.toolbFindOutFolder.clicked.connect(self.controller.findOutFolder)
        
        # self.controller.parametros_teste()
