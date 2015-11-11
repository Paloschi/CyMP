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
from DlgInvdistnnShapeEcmwf2Raster import UI_DlgInterpoladorShapeEcmwf
from DlgInvdistnnRaster2Raster import Ui_InvdistnnRaster2Raster
from DlgDistribuidorDeIndice import Ui_DistribuidorDeIndice
from DlgDecendial2Diario import Ui_Decendial2Diario
import ConfigParser
from Visao import DlgETc, DlgTAW, DlgDr

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

    def popupDr(self):
        popup = DlgDr.Ui_Dialog(self)
        popup.setupUi(popup)
        popup.show()   

    def popupTAW(self):
        popup = DlgTAW.Ui_Dialog(self)
        popup.setupUi(popup)
        popup.show()   
        
    def popupETc(self):
        popup = DlgETc.Ui_Dialog(self)
        popup.setupUi(popup)
        popup.show()        
        
    def popupDecendial_2_diario(self):
        popup = Ui_Decendial2Diario(self)
        popup.setupUi(popup)
        popup.show()

    def popupEstimativa_de_datas_de_colheita(self):
        
        popup = Ui_DlgEstimativaDatasAgricolas(self)
        popup.setupUi(popup)
        
        popup.show()
        
    def popupDestribuidor_de_indice(self):
        
        popup = Ui_DistribuidorDeIndice(self)
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
        
        self.menuBH = QtGui.QMenu(self.menubar)
        self.menuBH.setObjectName(_fromUtf8("menuBH"))
        
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
        
        self.actionETc = QtGui.QAction(MainWindow)
        self.actionETc.setObjectName(_fromUtf8("actionETc"))
        
        self.actionTAW = QtGui.QAction(MainWindow)
        self.actionTAW.setObjectName(_fromUtf8("actionTAW"))
        
        self.actionEsgotamento_BHFAO = QtGui.QAction(MainWindow)
        self.actionEsgotamento_BHFAO.setObjectName(_fromUtf8("actionEsgotamento_BHFAO"))
        
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

        self.actionDecendial_2_diario = QtGui.QAction(MainWindow)
        self.actionDecendial_2_diario.setObjectName(_fromUtf8("actionDecendial_2_diario"))
               
        self.actionFiltro_Savitz_Golay = QtGui.QAction(MainWindow)
        self.actionFiltro_Savitz_Golay.setObjectName(_fromUtf8("actionFiltro_Savitz_Golay"))
        
        self.actionEstatisticasEspectrais = QtGui.QAction(MainWindow)
        self.actionEstatisticasEspectrais.setObjectName(_fromUtf8("actionEstatisticasEspectrais"))

        self.actionDistribuidorDeIndice = QtGui.QAction(MainWindow)
        self.actionDistribuidorDeIndice.setObjectName(_fromUtf8("actionDistribuidorDeIndice"))
        
        self.menuBH.addAction(self.actionETc)
        self.menuBH.addAction(self.actionTAW)
        self.menuBH.addAction(self.actionEsgotamento_BHFAO)
        
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
        self.menuFun_o_es.addAction(self.actionDistribuidorDeIndice)
        self.menuFun_o_es.addAction(self.actionDecendial_2_diario)
        
        self.menuModelo.addAction(self.actionRodar)
        
        self.menubar.addAction(self.menuBH.menuAction())
        #self.menubar.addAction(self.menuDados.menuAction())
        self.menubar.addAction(self.menuFun_o_es.menuAction())
        #self.menubar.addAction(self.menuModelo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        config = ConfigParser.RawConfigParser()
        config.read('workspace.properties')
        version=config.get('Version', 'version')
            
        MainWindow.setWindowTitle(_translate("MainWindow", "Gafanhoto " + version, None))
        self.menuBH.setTitle(_translate("MainWindow", "Balanço Hídrico (BH)", None))
        #self.menuDados.setTitle(_translate("MainWindow", "Dados", None))
        self.menuInterpoladores.setTitle(_translate("MainWindow", "Interpoladores", None))
        self.menuCarregar_Dado.setTitle(_translate("MainWindow", "Carregar dado", None))
        self.menuFun_o_es.setTitle(_translate("MainWindow", "Functions", None))
        #self.menuModelo.setTitle(_translate("MainWindow", "Modelo", None))
        self.actionETc.setText(_translate("MainWindow", "Evapotranspiração da cultura (ETc)", None))
        self.actionTAW.setText(_translate("MainWindow", "Capacidade de armazenamento de água (TAW)", None))
        self.actionEsgotamento_BHFAO.setText(_translate("MainWindow", "Calcular Esgotamento BHFAO (Dr)", None))
        self.actionCarregar_dado_Simples.setText(_translate("MainWindow", "Carregar dado Simples", None))
        self.actionCarregar_lista_de_dados.setText(_translate("MainWindow", "Carregar lista de dados", None))
        self.actionCriar_dado_tabelado.setText(_translate("MainWindow", "Criar dado tabelado", None))
        self.actionListar_dados.setText(_translate("MainWindow", "Mostrar dados do modelo", None))
        self.actionListar_Fun_oes.setText(_translate("MainWindow", "Listar Funções", None))
        self.actionRodar.setText(_translate("MainWindow", "Executar", None))
        self.actionInterpolador.setText(_translate("MainWindow", "Interpolador ECMWF", None))
        self.actionInterpoladorRaster2Raster.setText(_translate("MainWindow", "Interpolador Raster pra raster", None))
        self.actionEstimativa_de_datas_de_colheita.setText(_translate("MainWindow", "Estimativa de datas de colheita", None))
        self.actionDistribuidorDeIndice.setText(_translate("MainWindow", "Distribuidor de índice", None))
        self.actionDecendial_2_diario.setText(_translate("MainWindow", "Decendial para diário", None))
        
        self.actionFiltro_Savitz_Golay.setText(_translate("MainWindow", "Filtro Savitz Golay", None))
        self.actionEstatisticasEspectrais.setText(_translate("MainWindow", "Estatisticas Espectrais", None))

        self.actionEstimativa_de_datas_de_colheita.triggered.connect(self.popupEstimativa_de_datas_de_colheita)
        self.actionFiltro_Savitz_Golay.triggered.connect(self.popupFiltro_Savitz_Golay)
        self.actionEstatisticasEspectrais.triggered.connect(self.popupEstatistiscas_Espectrais)
        self.actionInterpolador.triggered.connect(self.popupInterpolador_ECMWF)
        self.actionInterpoladorRaster2Raster.triggered.connect(self.popupInterpoladorRaster2Raster)
        self.actionDistribuidorDeIndice.triggered.connect(self.popupDestribuidor_de_indice)
        self.actionDecendial_2_diario.triggered.connect(self.popupDecendial_2_diario)
        self.actionETc.triggered.connect(self.popupETc)
        self.actionTAW.triggered.connect(self.popupTAW)
        self.actionEsgotamento_BHFAO.triggered.connect(self.popupDr)
