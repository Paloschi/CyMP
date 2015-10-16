# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_2.ui'
#
# Created: Tue Jun 09 11:16:29 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from DlgEstimativaDatasCultura import Ui_DlgEstimativaDatasAgricolas
from DlgFiltroSavitzGolay import Ui_DlgSavitzGolay
from DlgEstatisticasEspectrais import Ui_DlgEstatisticasEspectrais
from InterpoladorECMWF_Demo import UI_DlgInterpoladorShapeEcmwf
from DlgInvdistnnRaster2Raster import Ui_InvdistnnRaster2Raster

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

class Ui_MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
    def popupEstimativa_de_datas_de_colheita(self):
        
        popup = Ui_DlgEstimativaDatasAgricolas(self)
        popup.setupUi(popup)
        
        popup.show()
 
    def popupFiltro_Savitz_Golay(self):
        
        popup = Ui_DlgSavitzGolay(self)
        popup.setupUi(popup)
        
        popup.show()
        
    def popupEstatistiscas_Espectrais(self):

        popup = Ui_DlgEstatisticasEspectrais(self)
        popup.setupUi(popup)
        
        popup.show()
        
    def popupInterpolador_ECMWF(self):

        popup = UI_DlgInterpoladorShapeEcmwf()
        popup.setupUi(popup)
        popup.show()
                  
    def popupInterpoladorRaster2Raster(self):

        popup = Ui_InvdistnnRaster2Raster()
        popup.setupUi(popup)
        popup.show()
                  
 
                           
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(751, 59)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setAcceptDrops(True)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        
        self.menuDados = QtGui.QMenu(self.menubar)
        self.menuDados.setObjectName(_fromUtf8("menuDados"))
        
        self.menuCarregar_Dado = QtGui.QMenu(self.menuDados)
        self.menuCarregar_Dado.setObjectName(_fromUtf8("menuCarregar_Dado"))
        
        self.menuFun_o_es = QtGui.QMenu(self.menubar)
        self.menuFun_o_es.setObjectName(_fromUtf8("menuFun_o_es"))
        
        self.menuInterpoladores = QtGui.QMenu(self.menubar)
        self.menuInterpoladores.setObjectName(_fromUtf8("menuInterpoladores"))
        
        self.menuModelo = QtGui.QMenu(self.menubar)
        self.menuModelo.setObjectName(_fromUtf8("menuModelo"))
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionCarregar_Modelo = QtGui.QAction(MainWindow)
        self.actionCarregar_Modelo.setObjectName(_fromUtf8("actionCarregar_Modelo"))
        
        self.actionSalvar_Modelo_Ctrl_S = QtGui.QAction(MainWindow)
        self.actionSalvar_Modelo_Ctrl_S.setObjectName(_fromUtf8("actionSalvar_Modelo_Ctrl_S"))
        
        self.actionSalvar_Como = QtGui.QAction(MainWindow)
        self.actionSalvar_Como.setObjectName(_fromUtf8("actionSalvar_Como"))
        
        self.actionCarregar_dado_Simples = QtGui.QAction(MainWindow)
        self.actionCarregar_dado_Simples.setObjectName(_fromUtf8("actionCarregar_dado_Simples"))
        
        self.actionCarregar_lista_de_dados = QtGui.QAction(MainWindow)
        self.actionCarregar_lista_de_dados.setObjectName(_fromUtf8("actionCarregar_lista_de_dados"))
        
        self.actionCriar_dado_tabelado = QtGui.QAction(MainWindow)
        self.actionCriar_dado_tabelado.setObjectName(_fromUtf8("actionCriar_dado_tabelado"))
        
        self.actionListar_dados = QtGui.QAction(MainWindow)
        self.actionListar_dados.setObjectName(_fromUtf8("actionListar_dados"))
        
        self.actionListar_Fun_oes = QtGui.QAction(MainWindow)
        self.actionListar_Fun_oes.setObjectName(_fromUtf8("actionListar_Fun_oes"))
        
        self.actionRodar = QtGui.QAction(MainWindow)
        self.actionRodar.setObjectName(_fromUtf8("actionRodar"))
        
        self.actionInterpolador = QtGui.QAction(MainWindow)
        self.actionInterpolador.setObjectName(_fromUtf8("actionInterpolador"))

        self.actionInterpoladorRaster2Raster = QtGui.QAction(MainWindow)
        self.actionInterpoladorRaster2Raster.setObjectName(_fromUtf8("actionInterpoladorRaster2Raster"))
        
        self.actionEstimativa_de_datas_de_colheita = QtGui.QAction(MainWindow)
        self.actionEstimativa_de_datas_de_colheita.setObjectName(_fromUtf8("actionEstimativa_de_datas_de_colheita"))
        
        self.actionFiltro_Savitz_Golay = QtGui.QAction(MainWindow)
        self.actionFiltro_Savitz_Golay.setObjectName(_fromUtf8("actionFiltro_Savitz_Golay"))
        
        self.actionEstatisticasEspectrais = QtGui.QAction(MainWindow)
        self.actionEstatisticasEspectrais.setObjectName(_fromUtf8("actionEstatisticasEspectrais"))
        
        self.menuFile.addAction(self.actionCarregar_Modelo)
        self.menuFile.addAction(self.actionSalvar_Modelo_Ctrl_S)
        self.menuFile.addAction(self.actionSalvar_Como)
        
        self.menuCarregar_Dado.addAction(self.actionCarregar_dado_Simples)
        self.menuCarregar_Dado.addAction(self.actionCarregar_lista_de_dados)
        self.menuCarregar_Dado.addAction(self.actionCriar_dado_tabelado)
        
        self.menuDados.addAction(self.menuCarregar_Dado.menuAction())
        self.menuDados.addAction(self.actionListar_dados)
        
        self.menuInterpoladores.addAction(self.actionInterpolador)
        self.menuInterpoladores.addAction(self.actionInterpoladorRaster2Raster)
        
        self.menuFun_o_es.addAction(self.actionListar_Fun_oes)
        self.menuFun_o_es.addAction(self.menuInterpoladores.menuAction())
        self.menuFun_o_es.addAction(self.actionEstimativa_de_datas_de_colheita)
        self.menuFun_o_es.addAction(self.actionFiltro_Savitz_Golay)
        self.menuFun_o_es.addAction(self.actionEstatisticasEspectrais)
        
        self.menuModelo.addAction(self.actionRodar)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDados.menuAction())
        self.menubar.addAction(self.menuFun_o_es.menuAction())
        self.menubar.addAction(self.menuModelo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Gafanhoto 0.1.1", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuDados.setTitle(_translate("MainWindow", "Dados", None))
        self.menuInterpoladores.setTitle(_translate("MainWindow", "Interpoladores", None))
        self.menuCarregar_Dado.setTitle(_translate("MainWindow", "Carregar dado", None))
        self.menuFun_o_es.setTitle(_translate("MainWindow", "Funções", None))
        self.menuModelo.setTitle(_translate("MainWindow", "Modelo", None))
        self.actionCarregar_Modelo.setText(_translate("MainWindow", "Carregar Modelo", None))
        self.actionSalvar_Modelo_Ctrl_S.setText(_translate("MainWindow", "Salvar Modelo (Ctrl + S)", None))
        self.actionSalvar_Como.setText(_translate("MainWindow", "Salvar Como", None))
        self.actionCarregar_dado_Simples.setText(_translate("MainWindow", "Carregar dado Simples", None))
        self.actionCarregar_lista_de_dados.setText(_translate("MainWindow", "Carregar lista de dados", None))
        self.actionCriar_dado_tabelado.setText(_translate("MainWindow", "Criar dado tabelado", None))
        self.actionListar_dados.setText(_translate("MainWindow", "Mostrar dados do modelo", None))
        self.actionListar_Fun_oes.setText(_translate("MainWindow", "Listar Funções", None))
        self.actionRodar.setText(_translate("MainWindow", "Executar", None))
        self.actionInterpolador.setText(_translate("MainWindow", "Interpolador ECMWF", None))
        self.actionInterpoladorRaster2Raster.setText(_translate("MainWindow", "Interpolador Raster pra raster", None))
        self.actionEstimativa_de_datas_de_colheita.setText(_translate("MainWindow", "Estimativa de datas de colheita", None))
        
        self.actionFiltro_Savitz_Golay.setText(_translate("MainWindow", "Filtro Savitz Golay", None))
        self.actionEstatisticasEspectrais.setText(_translate("MainWindow", "Estatisticas Espectrais", None))

        self.actionEstimativa_de_datas_de_colheita.triggered.connect(self.popupEstimativa_de_datas_de_colheita)
        self.actionFiltro_Savitz_Golay.triggered.connect(self.popupFiltro_Savitz_Golay)
        self.actionEstatisticasEspectrais.triggered.connect(self.popupEstatistiscas_Espectrais)
        self.actionInterpolador.triggered.connect(self.popupInterpolador_ECMWF)
        self.actionInterpoladorRaster2Raster.triggered.connect(self.popupInterpoladorRaster2Raster)
