'''
Created on Oct 5, 2015

@author: rennan.paloschi
'''
from Modelo.beans import SerialTemporalFiles
import datetime
from datetime import timedelta

duracao = 10

serie_imagem = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Indices_BH\\ETc")
serie_imagem.loadListByRoot()
serie_imagem.prefixo = "evpt_"
serie_imagem.date_mask = "%Y%m%d"


for imagem in serie_imagem:
    data = serie_imagem.getDate_time(file=imagem)
    imagem_ = imagem.loadRasterData()
    imagem_ = imagem_ / 10
    
    for i in range (duracao):
        data = data + timedelta(1)
        serie_imagem.setDate_time(data, i)
        

        