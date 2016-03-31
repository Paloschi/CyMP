# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgNovaSerieTempora.ui'
#
# Created: Mon Nov 09 11:00:26 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Modelo.beans.SerialFileData import SerialTemporalFiles
from PyQt4.Qt import QDialog
import os
import ConfigParser
from PyQt4.Qt import QString

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

class Ui_Dialog(QDialog):
    
    SerieTemporal = None
        
    def ok(self):
        
        if not os.path.exists(str(self.txIn.text())):
            self.message(u"Pasta especificada não encontrada")
            return False  
        
        self.SerieTemporal = SerialTemporalFiles()
        self.SerieTemporal.root_path = str(self.txIn.text())
        self.SerieTemporal.prefixo = str(self.txPrefixo.text())
        self.SerieTemporal.sufixo = str(self.txSufixo.text())
        self.SerieTemporal.mutiply_factor = self.txFatorMultiplicador.value()
        self.SerieTemporal.date_mask = str(self.cbMascara.currentText())
        
        self.close()
        
        return self.SerieTemporal
    
    def setForm(self, serieTemporal):
    
        if serieTemporal is not None:
            self.SerieTemporal = serieTemporal
            self.txIn.setText(serieTemporal.root_path)
            self.txPrefixo.setText(serieTemporal.prefixo)
            self.txSufixo.setText(serieTemporal.sufixo)
            self.txFatorMultiplicador.setValue(serieTemporal.mutiply_factor)
            index = self.cbMascara.findText(serieTemporal.date_mask)
            if(index>0):
                self.cbMascara.setCurrentIndex(index)
            else :
                self.cbMascara.setCurrentIndex(1)
                self.cbMascara.setItemText(1, serieTemporal.date_mask)
        
        

    def message(self, text):
        text = QString(text)
        QtGui.QMessageBox.about(self, "Ops...", text)       
    
    def findPath(self):
        config = ConfigParser.RawConfigParser()
        config.read('workspace.properties')
        workspace=config.get('WorkSpace', 'space.default')
        fname = QtGui.QFileDialog.getExistingDirectory(None, "Escolha uma pasta", workspace,)
        if fname!="" :
            self.txIn.setText (fname)
 
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tbIn = QtGui.QToolButton(Dialog)
        self.tbIn.setObjectName(_fromUtf8("tbIn"))
        self.gridLayout.addWidget(self.tbIn, 0, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txIn = QtGui.QLineEdit(Dialog)
        self.txIn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txIn.setText(_fromUtf8(""))
        self.txIn.setObjectName(_fromUtf8("txIn"))
        self.gridLayout.addWidget(self.txIn, 0, 1, 1, 1)
        self.txPrefixo = QtGui.QLineEdit(Dialog)
        self.txPrefixo.setObjectName(_fromUtf8("txPrefixo"))
        self.gridLayout.addWidget(self.txPrefixo, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.txSufixo = QtGui.QLineEdit(Dialog)
        self.txSufixo.setObjectName(_fromUtf8("txSufixo"))
        self.gridLayout.addWidget(self.txSufixo, 2, 1, 1, 1)
        self.cbMascara = QtGui.QComboBox(Dialog)
        self.cbMascara.setEditable(True)
        self.cbMascara.setObjectName(_fromUtf8("cbMascara"))
        self.cbMascara.addItem(_fromUtf8(""))
        self.cbMascara.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cbMascara, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.txFatorMultiplicador = QtGui.QDoubleSpinBox(Dialog)
        self.txFatorMultiplicador.setMaximum(1000)
        self.txFatorMultiplicador.setObjectName(_fromUtf8("txFatorMultiplicador"))
        self.gridLayout.addWidget(self.txFatorMultiplicador, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.txFatorMultiplicador.setValue(1)
        
        self.label_6 = QtGui.QLabel(Dialog)
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.tbIn.clicked.connect(self.findPath)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Nova série temporal", None))
        self.tbIn.setText(_translate("Dialog", "...", None))
        self.label.setText(_translate("Dialog", "Endereço das imagens", None))
        self.label_3.setText(_translate("Dialog", "Sufixo", None))
        self.cbMascara.setItemText(0, _translate("Dialog", "%Y%m%d", None))
        self.cbMascara.setItemText(1, _translate("Dialog", "Outro Formato", None))
        self.label_2.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Este campo representa uma série de caracteres que vem antes da informação de data, no exemplo &quot;IMG_MODIS_2014-04-23_FILTRADA.tif&quot;, a sequencia de caracteres &quot;IMG_MODIS_&quot; é o prefixo, e este deve ser comum a todas as imagens presentes.</p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "Prefixo", None))
        self.label_4.setText(_translate("Dialog", "Máscara de tempo", None))
        descricao = ('<html><head/><body><p><a href="https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior" target="_blank"></p></body></html>')
        self.label_4.setWhatsThis(_translate("Dialog", descricao, None))                     
        self.label_5.setText(_translate("Dialog", "Fator multiplicador", None))
        

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    app.exec_()  