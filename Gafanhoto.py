'''
Created on Jul 7, 2015

@author: Paloschi
'''
from PyQt4 import QtGui
from Visao import TelaPrincipal
import ConfigParser
from Modelo import GeneralTools


if __name__ == '__main__':
    import sys
    import ctypes

    config = ConfigParser.RawConfigParser()
    config.read('workspace.properties')
    
    company=config.get('Version', 'company')
    product=config.get('Version', 'product')
    subproduct=config.get('Version', 'subproduct')
    version=config.get('Version', 'version')

    myappid = (company + "." + product + "." + subproduct + "." + version)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(config.get('Icon', 'icon.general')))
    
    print("Numero de nucleos: " + str(GeneralTools.available_cpu_count()))

    ex = TelaPrincipal.Ui_MainWindow()
    
    ex.show()
    sys.exit(app.exec_())
    
