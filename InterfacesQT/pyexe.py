'''
Created on Jun 12, 2015
precisa colocar o argumento py2exe
@author: Paloschi
'''
import matplotlib
matplotlib.use("Agg") # overrule configuration

print(matplotlib.get_configdir())

from distutils.core import setup
import py2exe

setup(
    data_files= matplotlib.get_py2exe_datafiles(),
    options = {
            
            "py2exe":{
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", ],
            'packages':['fiona',"rasterio","PyQt4.QtCore","PyQt4.QtGui" ],
            'excludes': ['_gtkagg', '_tkagg'],
            "includes" : ["sip", "matplotlib.backends.backend_tkagg", "FileDialog", "lxml._elementpath"],

        }
    },
    console = [{'script': 'Gafanhoto.py'}]
)

#setup(console=['MainWindow_2.py'])