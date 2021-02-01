'''
Created on Sep 17, 2015

@author: rennan.paloschi
'''
import os
import datetime

diretorio = "D:\\ClimatcDataECMWF_ERA5LAND\\ECMWF_ERA5LAND\\4-SKT\\4-SKT_1km\\"
os.chdir(diretorio)

'''
    Remover ou substituir fraze
'''

prefixo = ""
ext = ".tif"
subistituir = ".250m_16_dias_EVI_PR"
por = ""

lista_arquivos = (os.listdir('.'))

lista_arquivos.sort(reverse=True)

for nome in lista_arquivos:

    # ano = nome[0:4]
    # dia = nome[-7:-4]
    # print("Ano: ", ano, "Dia: ", dia)

    try:
        #data = datetime.strptime(ano + dia, "%Y%j")
        data = datetime.datetime.strptime(nome[:-4], "%Y-%m-%d")
        print(data)
        data = data + datetime.timedelta(days=1)
        novo_nome = prefixo + data.strftime("%Y-%m-%d") + ext

        print(novo_nome)
        os.rename(nome, novo_nome)

    except Exception as e:
        print(e)