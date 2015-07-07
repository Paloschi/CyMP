'''
Created on Jul 7, 2015

@author: Paloschi
'''
from PyQt4 import QtGui
from Visao import TelaPrincipal

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    
    app_icon = QtGui.QIcon()
    app_icon.addFile('img/favicon.ico')
    app.setWindowIcon(app_icon)

    #controller = InterpoladorECMWF_Demo_Controller.InterpoladorECMWF_Demo_Controller()

    ex = TelaPrincipal.Ui_MainWindow()
    #controller.form = ex
    
    ex.show()
    sys.exit(app.exec_())