'''
Created on 27/09/2015

@author: Rennan
'''

from Modelo.beans import RasterFile
import datetime
import numpy as np
import time

def Ds_DC_to_date(data):
        
        n = len(str(data))
        year = int(str(data)[0:4])    
        days = int(str(data)[4:n])
        date = datetime.datetime(year, 1, 1) + datetime.timedelta(days - 1)
        return date
    
def normalize_datas(semeadura, colheita):
    
    ano_semeadura = semeadura.astype(int)/1000
    dia_semeadura = semeadura - ano_semeadura * 1000
    
    ano_colheita = colheita.astype(int)/1000
    dia_colheita = colheita - ano_colheita * 1000
    
    primeira_data = np.min(semeadura)
    primeiro_ano = primeira_data/1000
    primeiro_dia = primeira_data - primeiro_ano * 1000
    
    semeadura_normalizada = (ano_semeadura - primeiro_ano - 1) * (primeiro_dia - dia_semeadura)  + (ano_semeadura - primeiro_ano) * dia_semeadura + (ano_semeadura - primeiro_ano) * (365 - primeiro_dia) 
    colheita_normalizada = ((ano_colheita - primeiro_ano) - 1) * (primeiro_dia - dia_colheita)  + (ano_colheita - primeiro_ano) * dia_colheita + (ano_colheita - primeiro_ano) * (365 - primeiro_dia)
    
    #print colheita_normalizada
    #print ((ano_colheita - primeiro_ano) - 1) * (primeiro_dia - dia_colheita) + (ano_colheita - primeiro_ano) * dia_colheita + (ano_colheita - primeiro_ano) * (365 - primeiro_dia)
    
    return semeadura_normalizada, colheita_normalizada, primeiro_ano, primeiro_dia


raster = RasterFile(file_full_path="C:\\Users\\Paloschi\\Desktop\\2013-2014\\semeadura.tif")
imagem_semeadura = raster.loadRasterData()
raster = RasterFile(file_full_path="C:\\Users\\Paloschi\\Desktop\\2013-2014\\colheita.tif")
imagem_colheita = raster.loadRasterData()

semeadura_normalizado, colheita_normalizado, ano_inicio, dia_inicio = normalize_datas(imagem_semeadura, imagem_colheita)

print (semeadura_normalizado)
print (colheita_normalizado)

ultimo_dia = np.max(colheita_normalizado)

periodo_kc = 120
delta_c = colheita_normalizado - semeadura_normalizado
kc_vetorizado = range(100,221)
kc_vetorizado[0] = 0

n_linhas = len(semeadura_normalizado)
n_colunas = len(semeadura_normalizado[0])
        
for dia in range(ultimo_dia):
    
    tempo_em_campo = dia - semeadura_normalizado
    
    #print tempo_em_campo
    
    i_FKc = imagem_kc_ = np.zeros((n_linhas, n_colunas))
    
    for i in range(n_linhas) :
        mask = ((tempo_em_campo[i] > 0) & (tempo_em_campo[i] < delta_c[i]))
        i_FKc[i][mask] = (tempo_em_campo[i][mask] * periodo_kc)/delta_c[i][mask]
        i_FKc[i][mask] +=1
    
    for i in range(n_linhas) :
        i_FKc[i] = [kc_vetorizado[int(index)] for index in i_FKc[i]]
        
    #print i_FKc
    #print datetime.datetime(ano_inicio, 1, 1) + datetime.timedelta(dia + dia_inicio - 1)

