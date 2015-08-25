'''
Created on Jul 7, 2015

@author: Paloschi
'''
from PyQt4 import QtGui
from Visao import TelaPrincipal

if __name__ == '__main__':
    import sys
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtGui.QApplication(sys.argv)
    

    
    app.setWindowIcon(QtGui.QIcon('images/icons/icon_trator.png'))
    #app_icon = QtGui.QIcon()
    #app_icon.addFile('images/icons/icon_trator.png')
    #app.setWindowIcon(app_icon)

    ex = TelaPrincipal.Ui_MainWindow()
    
    ex.show()
    sys.exit(app.exec_())