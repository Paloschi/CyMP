'''
Created on Jun 10, 2015

@author: Paloschi
'''
from PyQt4.QtGui import QFileDialog
from Modelo.Funcoes import PerfilExtractor
from Modelo.beans import Dados
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
    
import threading

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
    
class Controller(object):
    '''
    classdocs
    '''
    def __init__(self, ui):
        
        self.ui = ui
    
    def findInFolder(self):
        self.findPath(self.ui.leInFolder)
        
    def findOutFolder(self):
        self.findPath(self.ui.leOutFolder)
  
    def findPath(self, textToWrite):
        fname = QFileDialog.getExistingDirectory()
        textToWrite.setText (fname)
        
    def action_ok(self):
        
        self.extractor = PerfilExtractor.ComparadorSemeaduraColheita()
        self.tread = StoppableThread( self.executa, (self.extractor))
        
    def action_cancel(self):
        
        self.tread.stop()
        
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
        root_in = self.ajeitarPath(root_in)

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
    
