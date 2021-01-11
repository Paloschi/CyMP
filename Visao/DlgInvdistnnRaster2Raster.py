# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gafanhoto2.2InterpoladorInvdistnnRasterToRaster.ui'
#
# Created: Tue Oct 13 12:55:39 2015
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Controle import ConInvdistnnRaster2Raster
from PyQt5.Qt import QLocale, QTranslator

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



class Ui_InvdistnnRaster2Raster(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        
        #locale = QLocale.system().name()
        #qtTranslator = QTranslator()
        #if qtTranslator.load("qt_"+locale):
        #    Dialog.installTranslator(qtTranslator)
        
        self.controller = ConInvdistnnRaster2Raster.Controller(self)
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TabContent = QtWidgets.QTabWidget(Dialog)
        self.TabContent.setObjectName(_fromUtf8("TabContent"))
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 2, 2)
        self.TabContent.addTab(self.tab_4, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.txInFolder = QtWidgets.QLineEdit(self.tab_2)
        self.txInFolder.setObjectName(_fromUtf8("txInFolder"))
        self.gridLayout_3.addWidget(self.txInFolder, 0, 1, 1, 1)

        self.txOutFolder = QtWidgets.QLineEdit(self.tab_2)
        self.txOutFolder.setObjectName(_fromUtf8("txOutFolder"))
        self.gridLayout_3.addWidget(self.txOutFolder, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.btFindInFolder = QtWidgets.QToolButton(self.tab_2)
        self.btFindInFolder.setObjectName(_fromUtf8("btFindInFolder"))
        self.gridLayout_3.addWidget(self.btFindInFolder, 0, 2, 1, 1)
        self.btFindOutFolder = QtWidgets.QToolButton(self.tab_2)
        self.btFindOutFolder.setObjectName(_fromUtf8("btFindOutFolder"))
        self.gridLayout_3.addWidget(self.btFindOutFolder, 1, 2, 1, 1)
        self.TabContent.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        try:
            self.rbImgReference = QtWidgets.QRadioButton(self.tab_3)
            self.rbImgReference.setChecked(True)


            self.rbImgReference.setObjectName(_fromUtf8("rbImgReference"))
            self.verticalLayout_2.addWidget(self.rbImgReference)
            self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
            self.groupBox_2.setTitle(_fromUtf8(""))
            self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
            self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
            self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
            self.btFindImgReference = QtWidgets.QToolButton(self.groupBox_2)
            self.btFindImgReference.setObjectName(_fromUtf8("btFindImgReference"))
            self.gridLayout_5.addWidget(self.btFindImgReference, 0, 3, 1, 1)
            self.txImgReference = QtWidgets.QLineEdit(self.groupBox_2)
            self.txImgReference.setObjectName(_fromUtf8("txImgReference"))
            self.gridLayout_5.addWidget(self.txImgReference, 0, 2, 1, 1)
            self.label_7 = QtWidgets.QLabel(self.groupBox_2)
            self.label_7.setObjectName(_fromUtf8("label_7"))
            self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
            self.verticalLayout_2.addWidget(self.groupBox_2)
            self.rbManualConf = QtWidgets.QRadioButton(self.tab_3)
            self.rbManualConf.setEnabled(False)
            self.rbManualConf.setChecked(False)
            self.rbManualConf.setObjectName(_fromUtf8("rbManualConf"))
            self.verticalLayout_2.addWidget(self.rbManualConf)
            self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
            self.groupBox_3.setEnabled(False)
            self.groupBox_3.setTitle(_fromUtf8(""))
            self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
            self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
            self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
            self.label_10 = QtWidgets.QLabel(self.groupBox_3)
            self.label_10.setObjectName(_fromUtf8("label_10"))
            self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)
            self.label_9 = QtWidgets.QLabel(self.groupBox_3)
            self.label_9.setObjectName(_fromUtf8("label_9"))
            self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 1)
            self.label_12 = QtWidgets.QLabel(self.groupBox_3)
            self.label_12.setObjectName(_fromUtf8("label_12"))
            self.gridLayout_6.addWidget(self.label_12, 1, 2, 1, 1)
            self.label_13 = QtWidgets.QLabel(self.groupBox_3)
            self.label_13.setObjectName(_fromUtf8("label_13"))
            self.gridLayout_6.addWidget(self.label_13, 2, 2, 1, 1)
            self.label_11 = QtWidgets.QLabel(self.groupBox_3)
            self.label_11.setObjectName(_fromUtf8("label_11"))
            self.gridLayout_6.addWidget(self.label_11, 0, 2, 1, 1)
            self.label_8 = QtWidgets.QLabel(self.groupBox_3)
            self.label_8.setObjectName(_fromUtf8("label_8"))
            self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
            self.txXinit = QtWidgets.QLineEdit(self.groupBox_3)
            self.txXinit.setObjectName(_fromUtf8("txXinit"))
            self.gridLayout_6.addWidget(self.txXinit, 0, 1, 1, 1)
            self.txYinit = QtWidgets.QLineEdit(self.groupBox_3)
            self.txYinit.setObjectName(_fromUtf8("txYinit"))
            self.gridLayout_6.addWidget(self.txYinit, 1, 1, 1, 1)
            self.txLinesNumber = QtWidgets.QLineEdit(self.groupBox_3)
            self.txLinesNumber.setObjectName(_fromUtf8("txLinesNumber"))
            self.gridLayout_6.addWidget(self.txLinesNumber, 2, 1, 1, 1)
            self.txXend = QtWidgets.QLineEdit(self.groupBox_3)
            self.txXend.setObjectName(_fromUtf8("txXend"))
            self.gridLayout_6.addWidget(self.txXend, 0, 3, 1, 1)
            self.txYend = QtWidgets.QLineEdit(self.groupBox_3)
            self.txYend.setObjectName(_fromUtf8("txYend"))
            self.gridLayout_6.addWidget(self.txYend, 1, 3, 1, 1)
            self.txColumnsNumber = QtWidgets.QLineEdit(self.groupBox_3)
            self.txColumnsNumber.setObjectName(_fromUtf8("txColumnsNumber"))
            self.gridLayout_6.addWidget(self.txColumnsNumber, 2, 3, 1, 1)
            self.verticalLayout_2.addWidget(self.groupBox_3)
            self.TabContent.addTab(self.tab_3, _fromUtf8(""))
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName(_fromUtf8("tab"))
            self.gridLayout = QtWidgets.QGridLayout(self.tab)
            self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
            self.label_3 = QtWidgets.QLabel(self.tab)
            self.label_3.setObjectName(_fromUtf8("label_3"))
            self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
            self.label_4 = QtWidgets.QLabel(self.tab)
            self.label_4.setObjectName(_fromUtf8("label_4"))
            self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
            self.label_5 = QtWidgets.QLabel(self.tab)
            self.label_5.setObjectName(_fromUtf8("label_5"))
            self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
            self.txPower = QtWidgets.QDoubleSpinBox(self.tab)
            self.txPower.setProperty("value", 2.0)
            self.txPower.setObjectName(_fromUtf8("txPower"))
            self.gridLayout.addWidget(self.txPower, 1, 1, 1, 1)
            self.txRadius = QtWidgets.QDoubleSpinBox(self.tab)
            self.txRadius.setObjectName(_fromUtf8("txRadius"))
            self.gridLayout.addWidget(self.txRadius, 2, 1, 1, 1)
            self.txMaxPoint = QtWidgets.QSpinBox(self.tab)
            self.txMaxPoint.setProperty("value", 12)
            self.txMaxPoint.setObjectName(_fromUtf8("txMaxPoint"))
            self.gridLayout.addWidget(self.txMaxPoint, 3, 1, 1, 1)
            self.txMinPoint = QtWidgets.QSpinBox(self.tab)
            self.txMinPoint.setObjectName(_fromUtf8("txMinPoint"))
            self.gridLayout.addWidget(self.txMinPoint, 4, 1, 1, 1)
            self.label = QtWidgets.QLabel(self.tab)
            self.label.setObjectName(_fromUtf8("label"))
            self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
            self.TabContent.addTab(self.tab, _fromUtf8(""))
            self.verticalLayout.addWidget(self.TabContent)
            self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
            self.buttonBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
            self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
            self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
            self.verticalLayout.addWidget(self.buttonBox)

            self.retranslateUi(Dialog)
            self.TabContent.setCurrentIndex(0)

            self.buttonBox.accepted.connect(self.controller.action_ok)
            self.buttonBox.rejected.connect(self.controller.action_cancel)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

            self.controller.set_param()

        except Exception as e:
            print (e)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "CyMP - Interpolador raster pra raster", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Lucida Grande,Verdana,Geneva,Arial,sans-serif\'; font-size:8pt; font-weight:600; color:#000000; background-color:#ffffff;\">Invdistnn</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Interpolador raster pra raster (série de imagens)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Inverso da distância para uma potência com procura de vizinho mais próximo</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Inverse distance to a power with nearest neighbor searching.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:11pt; color:#000000;\">Mais informações: http://www.gdal.org/gdal_grid.html</span></a></p></body></html>", None))
        self.TabContent.setTabText(self.TabContent.indexOf(self.tab_4), _translate("Dialog", "Descrição", None))
        
        
        self.label_6.setText(_translate("Dialog", "Pasta de saída das imagens", None))
        self.label_2.setText(_translate("Dialog", "Pasta de entrada das imagens", None))
        self.btFindInFolder.setText(_translate("Dialog", "...", None))
        self.btFindOutFolder.setText(_translate("Dialog", "...", None))
        self.TabContent.setTabText(self.TabContent.indexOf(self.tab_2), _translate("Dialog", "Conf. pasta", None))
        self.rbImgReference.setText(_translate("Dialog", "Por imagem de referencia", None))
        self.btFindImgReference.setText(_translate("Dialog", "...", None))
        self.label_7.setText(_translate("Dialog", "Imagem:", None))
        self.rbManualConf.setText(_translate("Dialog", "Configuração manual", None))
        self.label_10.setText(_translate("Dialog", "Y Inicial:", None))
        self.label_9.setText(_translate("Dialog", "N. de linhas:", None))
        self.label_12.setText(_translate("Dialog", "Y Final:", None))
        self.label_13.setText(_translate("Dialog", "N. de Colunas:", None))
        self.label_11.setText(_translate("Dialog", "X Final:", None))
        self.label_8.setText(_translate("Dialog", "X Inicial:", None))
        self.TabContent.setTabText(self.TabContent.indexOf(self.tab_3), _translate("Dialog", "Conf. Imagem", None))
        self.label_3.setText(_translate("Dialog", "Raio:", None))
        self.label_4.setText(_translate("Dialog", "Máximo de pontos:", None))
        self.label_5.setText(_translate("Dialog", "Mínimo de pontos:", None))
        self.label.setText(_translate("Dialog", "Força:", None))
        self.TabContent.setTabText(self.TabContent.indexOf(self.tab), _translate("Dialog", "Conf. interpolador", None))
        
        self.btFindInFolder.clicked.connect(self.controller.findInFolder)
        self.btFindOutFolder.clicked.connect(self.controller.findOutFolder)
        self.btFindImgReference.clicked.connect(self.controller.findImgRef)
        
        #self.txInFolder.setText("C:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\2-CORTADAS_11-12")
        #self.txOutFolder.setText("C:\\Gafanhoto WorkSpace\\DataTestes\\out\\Primeira tentativa")
        #self.txImgReference.setText("C:\\Gafanhoto WorkSpace\\DataTestes\\out\\colheita.tif")
