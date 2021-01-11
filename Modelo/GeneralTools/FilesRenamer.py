'''
Created on Sep 17, 2015

@author: rennan.paloschi
'''
import os

diretorio = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Modis\\1-EVI_AQUA_TERA_11-12"
os.chdir(diretorio)

'''
    Remover ou substituir fraze
'''

subistituir = ".250m_16_dias_EVI_PR"
por = ""

for nome in os.listdir('.'):
    novo_nome = nome.replace(subistituir,por)
    os.rename(nome, novo_nome)
    print ('OK')