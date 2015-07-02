'''
Created on Jun 10, 2015

@author: Paloschi
'''
from PyQt4.QtGui import QFileDialog
from Operations import PerfilExtractor
from beans import Dados
from ctypes.wintypes import DOUBLE
from numpy import double
from PyQt4 import QtCore
import time
import thread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
class Controller(object):
    '''
    classdocs
    '''
    def __init__(self, ui):
        
        self.ui = ui
    
    def findInFolder(self):
        self.findFolder(self.ui.leInFolder)

    def findImg(self):
        fname = QFileDialog.getOpenFileNameAndFilter()
        self.ui.leImgRefer (fname)
        
    def findOutFolder(self):
        self.findFolder(self.ui.leOutFolder)
  
    def findFolder(self, textToWrite):
        fname = QFileDialog.getExistingDirectory()
        textToWrite.setText (fname)

        
    def action_ok(self):
        self.extractor = PerfilExtractor.ComparadorSemeaduraColheita()
        thread.start_new_thread( self.executa, (self.extractor,) )

    def updatePBar(self, extractor):
        while(self.extractor.progresso<=100):
            self.ui.progressBar.setValue(self.extractor.progresso) 
            time.sleep(0.13)
            #print(self.extractor.progresso)
        
    def executa(self, extractor):
        
        root_out = self.ui.leOutFolder.text()
        

        extractor.data = self.carregarParamIN()
        imagens = extractor.data
        
        semeadura = imagens["imagem_semeadura"]
        semeadura.data_name = self.ui.leImgSemeadura.text()
        colheita = imagens["imagem_colheita"]
        colheita.data_name = self.ui.leImgColheita.text()
        pico = imagens["imagem_pico"]
        pico.data_name = self.ui.leImgPico.text()
        
        semeadura.saveImage(root_out, ext=".tif")
        colheita.saveImage(root_out, ext=".tif")
        pico.saveImage(root_out, ext=".tif")
        
        
    def carregarParamIN(self):

        images = Dados.SerialData()
        parametrosIN = Dados.TableData()
        root_in = self.ui.leInFolder.text()
        root_in = _fromUtf8(str(root_in) + "\\")
        root_in = str(root_in).replace("\\", "/")
        print(root_in)
        
        images.loadListByRoot(root_in, "tif")
        
        
        print("numero de imagens: " + str(len(images)))
        
        parametrosIN["images"] = images
        parametrosIN["avanco_semeadura"] = Dados.SimpleData(data= self.ui.dspASemeadura.value())
        parametrosIN["avanco_colheita"] = Dados.SimpleData(data= self.ui.dsbAColheita.value())
        parametrosIN["intervalo_pico"] = Dados.SimpleData(data= self.ui.lePPico.text())
        parametrosIN["intervalo_semeadura"] = Dados.SimpleData(data= self.ui.lePSemeadura.text())
        parametrosIN["intervalo_colheita"] = Dados.SimpleData(data= self.ui.lePColheita.text())
        parametrosIN["null_value"] = Dados.SimpleData(data= self.ui.leNullValue.text())
        parametrosIN["progress_bar"] = Dados.SimpleData(self.ui.progressBar)
        
        return parametrosIN