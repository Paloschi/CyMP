'''
Created on Oct 5, 2015

@author: rennan.paloschi
'''
from Modelo.beans import SerialTemporalFiles
from datetime import timedelta
import calendar
from Modelo.beans import RasterFile
import numpy

serie_imagem_in = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\7-Cortado_tamanho_Modis\\evpt_2012")
serie_imagem_in.loadListByRoot()
serie_imagem_in.prefixo = "evpt_"
serie_imagem_in.date_mask = "%Y%m%d"

serie_imagem_out = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\8-Diario")
serie_imagem_out.loadListByRoot()
serie_imagem_out.prefixo = "evpt_diario_"
serie_imagem_out.date_mask = "%Y-%m-%d"
serie_imagem_out.mutiply_factor = 100
serie_imagem_out.out_datatype = "uint16"

n_imagens = len(serie_imagem_in)

for i in range(n_imagens):
    data = serie_imagem_in.getDate_time(i)
    dia_mes = data.day
    if dia_mes <= 10: duracao = 10
    elif dia_mes <= 20: duracao = 20
    else : duracao =  int(calendar.monthrange(data.year, data.month)[1]) - 20
   
    imagem_ = serie_imagem_in[i].loadRasterData()
    imagem_ = (imagem_ / 10) * serie_imagem_out.mutiply_factor
    if serie_imagem_out.out_datatype != None:
        imagem_ = numpy.array(imagem_).astype(serie_imagem_out.out_datatype)
    
    for ii in range (0, duracao):
        img = RasterFile()
        img.file_path = serie_imagem_out.root_path   
        data_img = data + timedelta(ii)
        img.file_name = serie_imagem_out.prefixo + data_img.strftime(serie_imagem_out.date_mask) + serie_imagem_out.sufixo
        img.data = imagem_
        img.file_ext = "tif"
        metadata = serie_imagem_in[i].metadata
        metadata.update(nodata=0)
        #serie_imagem_in[i].metadata
        #print "---------------------"
        #print metadata
        #print "---------------------"
        img.saveRasterData(metadata=metadata)

        
        

        