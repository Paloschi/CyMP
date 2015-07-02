# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interpoladorECMWF_Demo.ui'
#
# Created: Mon Mar 09 16:34:54 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(436, 361)
        self.leShapePath = QtGui.QLineEdit(Form)
        self.leShapePath.setGeometry(QtCore.QRect(10, 40, 301, 20))
        self.leShapePath.setObjectName(_fromUtf8("leShapePath"))
        self.cbAtribute = QtGui.QComboBox(Form)
        self.cbAtribute.setEnabled(False)
        self.cbAtribute.setGeometry(QtCore.QRect(10, 90, 331, 22))
        self.cbAtribute.setObjectName(_fromUtf8("cbAtribute"))
        self.cbAtribute.addItem(_fromUtf8(""))
        self.btnFindShp = QtGui.QPushButton(Form)
        self.btnFindShp.setGeometry(QtCore.QRect(330, 40, 75, 23))
        self.btnFindShp.setObjectName(_fromUtf8("btnFindShp"))
        self.bbOkCancela = QtGui.QDialogButtonBox(Form)
        self.bbOkCancela.setGeometry(QtCore.QRect(190, 330, 156, 23))
        self.bbOkCancela.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.bbOkCancela.setObjectName(_fromUtf8("bbOkCancela"))
        self.lwGroupAtributes = QtGui.QListWidget(Form)
        self.lwGroupAtributes.setEnabled(False)
        self.lwGroupAtributes.setGeometry(QtCore.QRect(10, 230, 331, 71))
        self.lwGroupAtributes.setObjectName(_fromUtf8("lwGroupAtributes"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.lwGroupAtributes.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.lwGroupAtributes.addItem(item)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 40, 2, 2))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.leImgRefPath = QtGui.QLineEdit(Form)
        self.leImgRefPath.setGeometry(QtCore.QRect(10, 150, 301, 20))
        self.leImgRefPath.setObjectName(_fromUtf8("leImgRefPath"))
        self.btnFindImgRef = QtGui.QPushButton(Form)
        self.btnFindImgRef.setGeometry(QtCore.QRect(330, 150, 75, 23))
        self.btnFindImgRef.setObjectName(_fromUtf8("btnFindImgRef"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Gafanhoto Beta 0.01 - Interpolador ECMWF", None))
        self.cbAtribute.setItemText(0, _translate("Form", "examlpe", None))
        self.btnFindShp.setText(_translate("Form", "Procurar", None))
        __sortingEnabled = self.lwGroupAtributes.isSortingEnabled()
        self.lwGroupAtributes.setSortingEnabled(False)
        item = self.lwGroupAtributes.item(0)
        item.setText(_translate("Form", "New Item", None))
        item = self.lwGroupAtributes.item(1)
        item.setText(_translate("Form", "New Item", None))
        self.lwGroupAtributes.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "Agrupar dados pelor atributos:", None))
        self.label_3.setText(_translate("Form", "Atributo a ser interpolado", None))
        self.label.setText(_translate("Form", "Shape ECMWF", None))
        self.label_4.setText(_translate("Form", "Imagem de referencia", None))
        self.btnFindImgRef.setText(_translate("Form", "Procurar", None))

