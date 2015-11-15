# -*- coding: utf-8 -*-
'''
Created on Oct 5, 2015

@author: rennan.paloschi
'''

from Modelo.beans import TABLE_DATA, FILE_DATA, SERIAL_FILE_DATA
from datetime import timedelta
import calendar
from Modelo.beans import RasterFile
import numpy
from Modelo.Funcoes import AbstractFunction
import threading

#serie_imagem_in = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\7-Cortado_tamanho_Modis\\evpt_2012")
#serie_imagem_in.loadListByRoot()
#serie_imagem_in.prefixo = "evpt_"
#serie_imagem_in.date_mask = "%Y%m%d"

#serie_imagem_out = SerialTemporalFiles(root_path="E:\\Gafanhoto WorkSpace\\Soja11_12\\Tratamento de dados\\ECMWF\\8-Diario")
#serie_imagem_out.loadListByRoot()
#serie_imagem_out.prefixo = "evpt_diario_"
#serie_imagem_out.date_mask = "%Y-%m-%d"
#serie_imagem_out.mutiply_factor = 100
#serie_imagem_out.out_datatype = "uint16"

class Funcao(AbstractFunction):
    
    def __setParamIN__(self): 
        self.descriptionIN["In"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Serie temporal de imagens de entrada"}
        self.descriptionIN["Out_config"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Serie temporal de saida saida (configuração)"}
        self.descriptionIN["Operation"] = {"Required":True, "Type":None, "Description":"Operação será aplicada aos valores das imagens baseando-se na quantia de dias do decende, ex.: chuva é soma, então.:'dividir'"}

    def __setParamOUT__(self):
        self.descriptionOUT["Out"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Serie temporal de saida saida"}
        
    def __execOperation__(self):
        
        serie_imagem_in = self.paramentrosIN_carregados["In"].loadListByRoot()
        serie_imagem_out = self.paramentrosIN_carregados["Out_config"]
        
        imagem_in_factor = float(serie_imagem_in.mutiply_factor)
        imagem_out_factor = float(serie_imagem_out.mutiply_factor)
        
        
        n_imagens = len(serie_imagem_in)
        
        if n_imagens is 0 :
            self.console(u"Erro: Nenhuma imagem encontrada na pasta especificada.") 
            self.console(u"Cancelando função.") 
            threading.currentThread().stop()
            return
        
        self.console(u"Construindo série temporal diária...")
        
        for i in range(n_imagens):
            
            self.progresso = (i / float(n_imagens)) * 100
            
            '''Recupera a data correspondente a imagem atual do laço '''
            data = serie_imagem_in.getDate_time(i)
            dia_mes = data.day
            
            '''Calcula quantos dias tem no decend atual'''
            if dia_mes <= 10: duracao = 10
            elif dia_mes <= 20: duracao = 10
            else : duracao =  int(calendar.monthrange(data.year, data.month)[1]) - 20
            
            if threading.currentThread().stopped()  :
                print "thread parada, retornando da função"
                return 
           
            imagem_ = serie_imagem_in[i].loadRasterData()
            imagem_ *= imagem_in_factor
            

            if self.paramentrosIN_carregados["Operation"] == "dividir valores": 
                imagem_ = (imagem_ / float(duracao))
            elif self.paramentrosIN_carregados["Operation"] == "manter valores": 
                pass
                
            imagem_ *= imagem_out_factor
            
            if serie_imagem_out.out_datatype != None:
                imagem_ = numpy.array(imagem_).astype(serie_imagem_out.out_datatype)
                #imagem_ = numpy.round(imagem_, 2)
            
            for ii in range (0, duracao):
                img = RasterFile()
                img.file_path = serie_imagem_out.root_path   
                data_img = data + timedelta(ii)
                img.file_name = serie_imagem_out.prefixo + data_img.strftime(serie_imagem_out.date_mask) + serie_imagem_out.sufixo
                img.data = imagem_
                img.file_ext = "tif"
                metadata = serie_imagem_in[i].metadata
                metadata.update(nodata=0)
                img.saveRasterData(metadata=metadata)

   
        self.console(u"Série temporal diária concluída.")

        