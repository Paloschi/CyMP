# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Apr 13 10:03:42 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class TreeWidgetItem(QtGui.QTreeWidgetItem):
    def mouseMoveEvent(self, e):
        
        #if e.buttons() != QtCore.Qt.RightButton:
            #return

        # write the relative cursor position to mime data
        mimeData = QtCore.QMimeData()
        # simple string with 'x,y'
        mimeData.setText('%d,%d' % (e.x(), e.y()))

        # let's make it fancy. we'll show a "ghost" of the button as we drag
        # grab the button to a pixmap
        pixmap = QtGui.QPixmap.grabWidget(self)

        # below makes the pixmap half transparent
        painter = QtGui.QPainter(pixmap)
        painter.setCompositionMode(painter.CompositionMode_DestinationIn)
        painter.fillRect(pixmap.rect(), QtGui.QColor(0, 0, 0, 127))
        painter.end()

        # make a QDrag
        drag = QtGui.QDrag(self)
        # put our MimeData
        drag.setMimeData(mimeData)
        # set its Pixmap
        drag.setPixmap(pixmap)
        # shift the Pixmap so that it coincides with the cursor position
        drag.setHotSpot(e.pos())

        # start the drag operation
        # exec_ will return the accepted action from dropEvent
        if drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
            print 'moved'
        else:
            print 'copied'

class Ui_MainWindow(QtGui.QMainWindow):
    
    def __init__(self):

        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
    def dragEnterEvent(self, e):
        e.accept()    
        
    def initUI(self):
        self.setAcceptDrops(True)
        
    def setupUi(self, MainWindow):
        self.setAcceptDrops(True)
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(777, 474)
        #MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        ## uniform one for the horizontal headers.

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget_2 = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget_2.setAcceptDrops(True)
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        item_0 = TreeWidgetItem(self.treeWidget_2)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsDragEnabled)
        item_0 = TreeWidgetItem(self.treeWidget_2)
        item_1 = TreeWidgetItem(item_0)
        item_1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsDragEnabled)
       
        self.horizontalLayout.addWidget(self.treeWidget_2)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setAcceptDrops(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsDragEnabled)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_0 = TreeWidgetItem(self.treeWidget)
        item_1 = TreeWidgetItem(item_0)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.treeWidget_3 = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget_3.setAcceptDrops(True)
        self.treeWidget_3.setObjectName(_fromUtf8("treeWidget_3"))
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsDragEnabled)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_0 = TreeWidgetItem(self.treeWidget_3)
        item_1 = TreeWidgetItem(item_0)
        self.horizontalLayout.addWidget(self.treeWidget_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget_3.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuBH = QtGui.QMenu(self.menubar)
        self.menuBH.setObjectName(_fromUtf8("menuBH"))
        self.menuDados = QtGui.QMenu(self.menubar)
        self.menuDados.setObjectName(_fromUtf8("menuDados"))
        self.menuCarregar_Dado = QtGui.QMenu(self.menuDados)
        self.menuCarregar_Dado.setObjectName(_fromUtf8("menuCarregar_Dado"))
        self.menuFun_o_es = QtGui.QMenu(self.menubar)
        self.menuFun_o_es.setObjectName(_fromUtf8("menuFun_o_es"))
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
        self.menuBH.addAction(self.actionETc)
        self.menuBH.addAction(self.actionTAW)
        self.menuBH.addAction(self.actionEsgotamento_BHFAO)
        self.menuCarregar_Dado.addAction(self.actionCarregar_dado_Simples)
        self.menuCarregar_Dado.addAction(self.actionCarregar_lista_de_dados)
        self.menuCarregar_Dado.addAction(self.actionCriar_dado_tabelado)
        self.menuDados.addAction(self.menuCarregar_Dado.menuAction())
        self.menuDados.addAction(self.actionListar_dados)
        self.menuFun_o_es.addAction(self.actionListar_Fun_oes)
        self.menuModelo.addAction(self.actionRodar)
        self.menubar.addAction(self.menuBH.menuAction())
        self.menubar.addAction(self.menuDados.menuAction())
        self.menubar.addAction(self.menuFun_o_es.menuAction())
        self.menubar.addAction(self.menuModelo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Gafanhoto", None))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "Funções", None))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "Item", None))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "New Subitem", None))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Modelo XYZ", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Item", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(5).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(6).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(7).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(8).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(9).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(10).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(11).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(12).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(13).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(14).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(15).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget.topLevelItem(15).child(0).setText(0, _translate("MainWindow", "New Subitem", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "Dados", None))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("MainWindow", "Item", None))
        self.treeWidget_3.topLevelItem(1).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(2).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(3).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(4).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(5).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(6).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(7).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(8).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(9).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(10).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(11).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(12).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(13).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(14).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(15).setText(0, _translate("MainWindow", "New Item", None))
        self.treeWidget_3.topLevelItem(15).child(0).setText(0, _translate("MainWindow", "New Subitem", None))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        self.memenuBHetTitle(_translate("MainWindow", "File", None))
        self.menuDados.setTitle(_translate("MainWindow", "Dados", None))
        self.menuCarregar_Dado.setTitle(_translate("MainWindow", "Carregar dado", None))
        self.menuFun_o_es.setTitle(_translate("MainWindow", "Funções", None))
        self.menuModelo.setTitle(_translate("MainWindow", "Modelo", None))
        self.actiactionETcText(_translate("MainWindow", "Carregar Modelo", None))
        self.actiactionTAWText(_translate("MainWindow", "Salvar Modelo (Ctrl + S)", None))
        self.actiBHFAOText(_translate("MainWindow", "Salvar Como", None))
        self.actionCarregar_dado_Simples.setText(_translate("MainWindow", "Carregar dado Simples", None))
        self.actionCarregar_lista_de_dados.setText(_translate("MainWindow", "Carregar lista de dados", None))
        self.actionCriar_dado_tabelado.setText(_translate("MainWindow", "Criar dado tabelado", None))
        self.actionListar_dados.setText(_translate("MainWindow", "Mostrar dados do modelo", None))
        self.actionListar_Fun_oes.setText(_translate("MainWindow", "Listar Funções", None))
        self.actionRodar.setText(_translate("MainWindow", "Executar", None))
        
 
        self.treeWidget_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_3.customContextMenuRequested.connect(self.openMenu)
        #headers.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        #headers.customContextMenuRequested.connect(self.contextMenuEvent)
    
    def openMenu(self, position):
      
        indexes = self.treeWidget_3.selectedIndexes()
        if len(indexes) > 0:
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1
         
        menu = QtGui.QMenu()
        if level == 0:
            menu.addAction("Adicionar dado", self.new_data)
            menu.addAction("Adicionar dado serial", self.new_serialdata)
            menu.addAction("Adicionar dado tabelado", self.new_tabledata)
            menu.addAction("Remover dado", self.remove_data)
            menu.addAction("Copiar dado", self.copy_data)
        elif level == 1:
            menu.addAction(self.tr("Edit object/container"))
        elif level == 2:
            menu.addAction(self.tr("Edit object"))
         
        menu.exec_(self.treeWidget_3.viewport().mapToGlobal(position)) 
        
    def new_data(self, parent=None):
        print("Adicionando dado simples")
    
    def new_serialdata(self, parent=None):
        print("Adicionando dado serial")
    
    def new_tabledata(self, parent=None):
        print("Adicionando dado tabelado")
    
    def remove_data(self, parent=None):

        root = self.treeWidget_3.invisibleRootItem()
        for item in self.treeWidget_3.selectedItems():
            (item.parent() or root).removeChild(item)
    
    def copy_data(self, parent=None):
        pass
        
    def create_popup_menu(self, parent=None):
        self.popup_menu = QtGui.QMenu(parent)
        self.popup_menu.addAction("New", self.new_cluster)
        self.popup_menu.addAction("Rename", self.rename_cluster)
        self.popup_menu.addSeparator()
        self.popup_menu.addAction("Delete", self.delete_cluster)
            
    def contextMenuEvent(self, event):
         
        menu = QtGui.QMenu(self)
        
        quitAction = menu.addAction("Quit")
        
        index = self.indexAt(event.pos())
        
        print (index.collum())
        
        action = menu.exec_(self.menuDados.mapToGlobal(event.pos()))
        
        if action == quitAction:
            QtGui.qApp.quit()
            
    def dropEvent(self, e):
        # get the relative position from the mime data
        mime = e.mimeData().text()
        x, y = map(int, mime.split(','))

        if e.keyboardModifiers() & QtCore.Qt.ShiftModifier:
            # copy
            # so create a new button
            button = TreeWidgetItem('Button', self)
            # move it to the position adjusted with the cursor position at drag
            button.move(e.pos()-QtCore.QPoint(x, y))
            # show it
            button.show()
            # store it
            #self.buttons.append(button)
            # set the drop action as Copy
            e.setDropAction(QtCore.Qt.CopyAction)
        else:
            # move
            # so move the dragged button (i.e. event.source())
            e.source().move(e.pos()-QtCore.QPoint(x, y))
            # set the drop action as Move
            e.setDropAction(QtCore.Qt.MoveAction)
        # tell the QDrag we accepted it
        e.accept()
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    #controller = InterpoladorECMWF_Demo_Controller.InterpoladorECMWF_Demo_Controller()

    ex = Ui_MainWindow()
    #controller.form = ex
    
    ex.show()
    sys.exit()
