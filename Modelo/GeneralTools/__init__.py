# -*- coding: utf-8 -*-
from PyQt4 import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

def ajeitarExt(ext):
    ext = str(ext).lower()
    if ext[0] != "." : ext = "." + ext
    return ext

def construirPathCompleto(path, nome, extencao):
    """
        Essa fun��o da uma arrumada no path por causa das barras invertidas que as vezes bugam
    """

    if path[-1] != "/" : path += "/" 
    
    extencao = ajeitarExt(extencao)
    path_completo = path + nome + extencao
        
    return path_completo   
