'''
Created on Jul 7, 2015

@author: Paloschi
'''
from PyQt4 import QtGui
from Visao import TelaPrincipal
import ConfigParser
from Modelo import GeneralTools
from PyQt4.Qt import QLocale, QTranslator

import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    import sys
    import ctypes
    

    #config = ConfigParser.RawConfigParser()
    #config.read('workspace.properties')
    
    #company=config.get('Version', 'company')
    #product=config.get('Version', 'product')
    #subproduct=config.get('Version', 'subproduct')
    #version=config.get('Version', 'Version')

    #myappid = (company + "." + product + "." + subproduct + "." + version)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Unioeste-LEA.Gafanhoto.Beta.1.0.0")
    
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("images/icons/icon_trator.png"))

    
    locale = QLocale.system().name()
    qtTranslator = QTranslator()
    if qtTranslator.load("qt_"+locale):
        app.installTranslator(qtTranslator)
    
    #print("Numero de nucleos: " + str(GeneralTools.available_cpu_count()))

    ex = TelaPrincipal.Ui_MainWindow()
    
    ex.show()
    sys.exit(app.exec_())
    
