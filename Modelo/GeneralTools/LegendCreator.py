# -*- coding: utf-8 -*-
'''
Created on 23/01/2016

@author: Paloschi
'''
from Modelo.beans.SerialFileData import SerialTemporalFiles
from datetime import datetime as dt
import datetime
from datetime import timedelta
from matplotlib.dates import seconds

path = "D:\\1 - Mestrado (segundo semestre)\\1-Dissertacao\\DVD Apendice A\\Imagens\\2-Kc"
prefixo = ""
sufixo = ""
mascara = "%Y-%m-%d"
duracao = 50

serie_img = SerialTemporalFiles(root_path = path)
serie_img.sufixo = sufixo
serie_img.prefixo = prefixo
serie_img.date_mask = mascara

tempo = datetime.timedelta(milliseconds = 0)
duracao = datetime.timedelta(milliseconds = duracao)

#print "---------------------"
#print "tempo", tempo
#print "duração", duracao
#print "---------------------"

serie_img.loadListByRoot()

for i in range(len(serie_img)):
    tempo_somado = tempo + duracao
    data = serie_img.getDate_time(i)
    print (i + 1)
    print (tempo, "-->", tempo_somado)
    print (dt.strftime(data,"%d/%m/%Y"))
    tempo = tempo_somado
    print ("")
    
