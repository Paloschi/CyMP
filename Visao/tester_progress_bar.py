'''
Created on 13/10/2015

@author: Rennan
'''

import sys
from PyQt4 import QtCore, QtGui

from Visao.teste_progress_bar import Ui_Dialog

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())