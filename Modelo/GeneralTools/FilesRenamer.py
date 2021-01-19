'''
Created on Sep 17, 2015

@author: rennan.paloschi
'''
import os
from datetime import datetime

diretorio = "D:\\Agririsk\\Coamo_FAO_estimation\\ETo"
os.chdir(diretorio)

'''
    Remover ou substituir fraze
'''

prefixo = ""
ext = ".tif"
subistituir = ".250m_16_dias_EVI_PR"
por = ""

for nome in os.listdir('.'):

    ano = nome[0:4]
    dia = nome[-7:-4]
    print("Ano: ", ano, "Dia: ", dia)

    try:
        data = datetime.strptime(ano + dia, "%Y%j")
        novo_nome = prefixo + data.strftime("%Y-%m-%d") + ext

        print(novo_nome)
        os.rename(nome, novo_nome)

    except Exception as e:
        print(e)