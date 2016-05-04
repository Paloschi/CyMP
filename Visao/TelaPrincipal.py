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
from Visao import DlgETc, DlgTAW, DlgDr, DlgKs, DlgPPR, DlgYaFao

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

    def popupYaFao(self):
        popup = DlgYaFao.Ui_Dialog(self)
        popup.setupUi(popup)
        popup.show()  

    def popupPPB(self):
        popup = DlgPPR.Ui_Dialog(self)
        popup.setupUi(popup)
        popup.show()   

    def popupKs(self):
        popup = DlgKs.Ui_Dialog(self)
        popup.setupUi(popup)
        popup.show()   

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
        MainWindow.resize(751, 240)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setAcceptDrops(True)
        
        MainWindow.setIconSize(QtCore.QSize(200, 200))
        
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
        
        self.menuProdutividade = QtGui.QMenu(self.menubar)
        self.menuProdutividade.setObjectName(_fromUtf8("menuProdutividade"))
        
        self.menuCarregar_Dado = QtGui.QMenu(self.menuProdutividade)
        self.menuCarregar_Dado.setObjectName(_fromUtf8("menuCarregar_Dado"))
        
        self.menuFun_o_es = QtGui.QMenu(self.menubar)
        self.menuFun_o_es.setObjectName(_fromUtf8("menuFun_o_es"))
        
        self.menuInterpoladores = QtGui.QMenu(self.menubar)
        self.menuInterpoladores.setObjectName(_fromUtf8("menuInterpoladores"))
        
        self.menuEstatisticas = QtGui.QMenu(self.menubar)
        self.menuEstatisticas.setObjectName(_fromUtf8("menuEstatisticas"))
        
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
        
        self.actionKs = QtGui.QAction(MainWindow)
        self.actionKs.setObjectName(_fromUtf8("actionKs"))
        
        self.actionPPB = QtGui.QAction(MainWindow)
        self.actionPPB.setObjectName(_fromUtf8("actionPPB"))
        
        self.actionCarregar_lista_de_dados = QtGui.QAction(MainWindow)
        self.actionCarregar_lista_de_dados.setObjectName(_fromUtf8("actionCarregar_lista_de_dados"))
        
        self.actionCriar_dado_tabelado = QtGui.QAction(MainWindow)
        self.actionCriar_dado_tabelado.setObjectName(_fromUtf8("actionCriar_dado_tabelado"))
        
        self.actionYaFao = QtGui.QAction(MainWindow)
        self.actionYaFao.setObjectName(_fromUtf8("actionYaFao"))
        
       #self.actionListar_Fun_oes = QtGui.QAction(MainWindow)
        #self.actionListar_Fun_oes.setObjectName(_fromUtf8("actionListar_Fun_oes"))
        
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
        self.menuBH.addAction(self.actionKs)
        
        #self.menuCarregar_Dado.addAction(self.actionPPB)
        #self.menuCarregar_Dado.addAction(self.actionCarregar_lista_de_dados)
        #self.menuCarregar_Dado.addAction(self.actionCriar_dado_tabelado)
        
        self.menuProdutividade.addAction(self.actionPPB)
        self.menuProdutividade.addAction(self.actionYaFao)
        
        self.menuInterpoladores.addAction(self.actionInterpolador)
        self.menuInterpoladores.addAction(self.actionInterpoladorRaster2Raster)
        
        #self.menuFun_o_es.addAction(self.actionListar_Fun_oes)
        self.menuFun_o_es.addAction(self.menuInterpoladores.menuAction())
        self.menuFun_o_es.addAction(self.actionEstimativa_de_datas_de_colheita)
        self.menuFun_o_es.addAction(self.actionFiltro_Savitz_Golay)
        self.menuFun_o_es.addAction(self.actionDistribuidorDeIndice)
        self.menuFun_o_es.addAction(self.actionDecendial_2_diario)
        
        #self.menuEstatisticas.addAction(self.actionRodar)
        self.menuEstatisticas.addAction(self.actionEstatisticasEspectrais)
        
        self.menubar.addAction(self.menuFun_o_es.menuAction())
        self.menubar.addAction(self.menuBH.menuAction())
        self.menubar.addAction(self.menuProdutividade.menuAction())
        self.menubar.addAction(self.menuEstatisticas.menuAction())
        
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(26, 44, 600, 75))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #import inspect
        
        #path_ = inspect.getfile(self.__class__)
        #path_ = str(path_).replace("Visao\TelaPrincipal.py", "")
        
        self.logo_lea = QtGui.QPushButton(MainWindow)
        self.logo_lea.setGeometry(QtCore.QRect(26, 130, 200, 82))
        self.icon_lea = QtGui.QIcon("images\logo_lea.jpg")
        self.icon_lea.pixmap(QtCore.QSize(200, 200))
        self.logo_lea.setIcon(self.icon_lea)
        self.logo_lea.setIconSize(QtCore.QSize(200, 100))

        self.logo_lea = QtGui.QPushButton(MainWindow)
        self.logo_lea.setGeometry(QtCore.QRect(250, 130, 120, 82))
        self.icon_lea = QtGui.QIcon("images\logoPgeagrid2.png")
        self.icon_lea.pixmap(QtCore.QSize(200, 200))
        self.logo_lea.setIcon(self.icon_lea)
        self.logo_lea.setIconSize(QtCore.QSize(145, 80))        

        self.logo_lea = QtGui.QPushButton(MainWindow)
        self.logo_lea.setGeometry(QtCore.QRect(394, 130, 82, 82))
        self.icon_lea = QtGui.QIcon("images\logo_campus_cvel.jpg")
        self.icon_lea.pixmap(QtCore.QSize(200, 200))
        self.logo_lea.setIcon(self.icon_lea)
        self.logo_lea.setIconSize(QtCore.QSize(120, 82))       

        self.logo_lea = QtGui.QPushButton(MainWindow)
        self.logo_lea.setGeometry(QtCore.QRect(500, 130, 110, 82))
        self.icon_lea = QtGui.QIcon("images\capes-logo-CAPES.jpg")
        self.icon_lea.pixmap(QtCore.QSize(200, 200))
        self.logo_lea.setIcon(self.icon_lea)
        self.logo_lea.setIconSize(QtCore.QSize(120, 82))       
                
        #MainWindow.add(self.logo_lea)

    def retranslateUi(self, MainWindow):
        
        config = ConfigParser.RawConfigParser()
        config.read('workspace.properties')
        version=config.get('Version', 'version')
        
        texto = "Software de Estimativa de Produtividade\n"
        
        texto += "Desenvolvido pelo Laboratório de Estatística Aplicada (LEA) - UNIOESTE - 2016\n"
        texto += "Desenvolvedor: Rennan Andres Paloschi - rennan_paloschi@yahoo.com\n"
        texto += "Orientação: Jerry Adriani Johann\n"
        texto += "Co-orientação: Adair Santa Catarina"
        
        self.label.setText(_translate("Dialog", texto, None))
            
        MainWindow.setWindowTitle(_translate("MainWindow", "Crop-yield Modeling Platform - CyMP " + version, None))
        self.menuBH.setTitle(_translate("MainWindow", "Balanço Hídrico (FAO)", None))
        self.menuProdutividade.setTitle(_translate("MainWindow", "Estimativa de produtividade (FAO)", None))
        self.menuInterpoladores.setTitle(_translate("MainWindow", "Interpoladores", None))
        self.menuCarregar_Dado.setTitle(_translate("MainWindow", "Carregar dado", None))
        self.menuFun_o_es.setTitle(_translate("MainWindow", "Tratamento de dados", None))
        self.menuEstatisticas.setTitle(_translate("MainWindow", "Estatísticas", None))
        self.actionETc.setText(_translate("MainWindow", "Evapotranspiração (ETc - ETa)", None))
        self.actionTAW.setText(_translate("MainWindow", "Capacidade Hídrica (TAW/RAW)", None))
        self.actionEsgotamento_BHFAO.setText(_translate("MainWindow", "Calcular Esgotamento BHFAO (Dr)", None))
        self.actionKs.setText(_translate("MainWindow", "Fator de estresse hídrico da cultura (Ks)", None))
        
        self.actionPPB.setText(_translate("MainWindow", "Produtividade Potencial Bruta (PPB)", None))
        self.actionCarregar_lista_de_dados.setText(_translate("MainWindow", "Carregar lista de dados", None))
        self.actionCriar_dado_tabelado.setText(_translate("MainWindow", "Criar dado tabelado", None))
        self.actionYaFao.setText(_translate("MainWindow", "Produtividade atingível (Ya)", None))
        #self.actionListar_Fun_oes.setText(_translate("MainWindow", "Listar Funções", None))
        self.actionRodar.setText(_translate("MainWindow", "Executar", None))
        self.actionInterpolador.setText(_translate("MainWindow", "Interpolador shape ECMWF para raster", None))
        #self.actionInterpolador.setText(_translate("MainWindow", "Interpolador shape ECMWF para raster (em manutenção)", None))
        #self.actionInterpolador.setEnabled(False)
        self.actionInterpoladorRaster2Raster.setText(_translate("MainWindow", "Interpolador raster pra raster", None))
        self.actionEstimativa_de_datas_de_colheita.setText(_translate("MainWindow", "Estimativa de datas da cultura", None))
        self.actionDistribuidorDeIndice.setText(_translate("MainWindow", "Distribuidor de índice", None))
        self.actionDecendial_2_diario.setText(_translate("MainWindow", "Decendial para diário", None))
        
        self.actionFiltro_Savitz_Golay.setText(_translate("MainWindow", "Filtro Savitzky-golay", None))
        self.actionEstatisticasEspectrais.setText(_translate("MainWindow", "Estatísticas Descritivas (Perfil)", None))

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
        self.actionKs.triggered.connect(self.popupKs)
        self.actionPPB.triggered.connect(self.popupPPB)
        self.actionYaFao.triggered.connect(self.popupYaFao)
