'''
Created on Jul 7, 2015

@author: Paloschi
'''
import sys
from PyQt5 import QtGui, QtWidgets
from Visao import TelaPrincipal
from PyQt5 import QtCore
from PyQt5.Qt import QLocale, QTranslator
from Modelo.GeneralTools import available_cpu_count

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

import warnings
warnings.filterwarnings('ignore')

import multiprocessing as mp

         
if __name__ == '__main__':

    
    import sys
    import ctypes
    import configparser as ConfigParser
    
    mp.freeze_support() # optional if the program is not frozen

    config = ConfigParser.RawConfigParser()
    config.read('workspace.properties')
    
    company=config.get('Version', 'company')
    product=config.get('Version', 'product')
    subproduct=config.get('Version', 'subproduct')
    version=config.get('Version', 'Version')

    myappid = (company + "." + product + "." + subproduct + "." + version)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    app = QtWidgets.QApplication(sys.argv)
    icon=config.get('Icon', 'icon.general')
    app.setWindowIcon(QtGui.QIcon(icon))

    locale = QLocale.system().name()
    qtTranslator = QTranslator()
    coretranslator = QtCore.QTranslator(app)
    if qtTranslator.load("qt_"+locale):
        qtTranslator.load('qt_%s' % locale,
                          QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath))
        app.installTranslator(qtTranslator)
        app.installTranslator(coretranslator)
    
    print("Numero de nucleos: " + str(available_cpu_count()))

    try:

        ex = TelaPrincipal.Ui_MainWindow()
        ex.show()
        sys.exit(app.exec_())

    except Exception as e:
        print (e)




def catch_exceptions(t, val, tb):
    QtWidgets.QMessageBox.critical(None,
                                   "An exception was raised",
                                   "Exception type: {}".format(t))
    old_hook(t, val, tb)

old_hook = sys.excepthook
sys.excepthook = catch_exceptions