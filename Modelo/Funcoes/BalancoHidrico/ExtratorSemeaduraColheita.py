# -*- coding: utf-8 -*-
'''
Created on Apr 8, 2015

@author: Paloschi
'''

from Modelo.beans import TableData, SERIAL_FILE_DATA, RasterFile                   
from numpy.core.numeric import array
import gdal
from Modelo.Funcoes import AbstractFunction
progress = gdal.TermProgress_nocb   
from datetime import datetime as dt
from datetime import timedelta
import numpy as np
import sys
import threading


class ExtratorSemeaduraColheita(AbstractFunction):
    '''
    Essa função foi criada para extrair as datas de semeadura (primeiro low peak), colheita (segundo low peak) e pico
    
    ela pode ser configurada pra procurar os picos e os picos inferiores em intervalos especificos que são equivalentes ao �ndice da imagem 
    na série de imagens
    
    também pode ser passado como parametro determinados avanço que são relativos em porcentagem com a distancia ente o pico
    
    ex.: se o pico se dá na imagem 8, a colheita na imagem 4 e colocar um avanço na data de colheita de 10% será feito (8 - 4) * 1,10 = 4.4,
         a data de colheita para esse pixel será a data equivalente a 4,4 imagens
    
    '''

    def __setParamIN__(self):
        self.descriptionIN["images"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens para procurar as datas"}
        
        self.descriptionIN["avanco_semeadura"] = {"Required":False, "Type":None, "Description":"parametro para avanco de semeadura (Default: 0)"}
        self.descriptionIN["avanco_colheita"] = {"Required":False, "Type":None, "Description":"parametro para avanco de colheita (Default: 0)"}
        self.descriptionIN["intervalo_semeadura"] = {"Required":True, "Type":None, "Description":"intervalo para procura da data nas imagens ex.: 3-24"}
        self.descriptionIN["intervalo_pico"] = {"Required":True, "Type":None, "Description":"intervalo para procura da data nas imagens ex.: 3-24"}
        self.descriptionIN["intervalo_colheita"] = {"Required":True, "Type":None, "Description":"intervalo para procura da data nas imagens ex.: 3-24"}
        self.descriptionIN["mask"] = {"Required":True, "Type":None, "Description":"Mascara usada para identificar a data de cada imagem ex.: %YY%mm%dd"}
        self.descriptionIN["prefixo"] = {"Required":True, "Type":None, "Description":"Prefixo usado antes da data no nome da imagem"}
        self.descriptionIN["sufixo"] = {"Required":True, "Type":None, "Description":"Sufixo usado depois da data no nome da imagem"}
        self.descriptionIN["null_value"] = {"Required":False, "Type":None, "Description":"valor nulo a ser ignorado"}
     
    def __setParamOUT__(self):
        self.descriptionOUT["imagem_semeadura"] = "imagem com as datas de semeadura" 
        self.descriptionOUT["imagem_pico"] = "imagem com as datas de pico vegetativo" 
        self.descriptionOUT["imagem_colheita"] = "imagem com as datas de colheita" 
        
    def __execOperation__(self):
        
        prefix = self.paramentrosIN_carregados["prefixo"]
        sufix = self.paramentrosIN_carregados["sufixo"]
        
        mask =  self.paramentrosIN_carregados["mask"]
        
        images_super = self.paramentrosIN_carregados["images"]
        avanco_semeadura = self.paramentrosIN_carregados["avanco_semeadura"]
        avanco_semeadura = avanco_semeadura
        avanco_colheita = self.paramentrosIN_carregados["avanco_colheita"]
        avanco_colheita = avanco_colheita
        
        intervalo_semeadura = self.paramentrosIN_carregados["intervalo_semeadura"]
        intervalo_pico = self.paramentrosIN_carregados["intervalo_pico"]
        intervalo_colheita = self.paramentrosIN_carregados["intervalo_colheita"]
        
        #barra_progresso = self.paramentrosIN_carregados["progress_bar"]
        
        intervalo_semeadura = intervalo_semeadura.split("-")
        intervalo_pico = intervalo_pico.split("-")
        intervalo_colheita = intervalo_colheita.split("-")
        
        images = images_super.loadListRasterData()
        
        if images==None:
            raise Exception("A funcao necessita de uma serie de imagens para funcionar")
        
        n_images = len(images)
        n_linhas = len(images[0])
        n_colunas = len(images[0][0])
        
        
        #nullValue = float(self.paramentrosIN_carregados["null_value"])
        

        #if(images[0][0][0] == nullValue) : print("null value igual") 
        #else : print("diferente")
        
        sys.stdout.write( "Criando imagens de referencia: ")
        self.console.print_text(u"Criando imagens de referência.")
        imagem_referencia = np.zeros((n_linhas, n_colunas))
        
        imagem_semeadura = array(imagem_referencia).astype(dtype="int32")
        imagem_colheita = array(imagem_referencia).astype(dtype="int32")
        imagem_pico = array(imagem_referencia).astype(dtype="int32")

        
        sys.stdout.write( "Gerando estimativas: ")
        self.console.print_text("Gerando estimativas.")
        progress(0.0)
        
        imagem_for_null_value = images[0]
        nullValue = imagem_for_null_value[0][0]
        #print(nullValue)
        
        avanco_semeadura = timedelta(avanco_semeadura)
        avanco_colheita = timedelta(avanco_colheita)
        
        images_super[0].metadata.update(nodata=0)
        #print images_super[0].metadata
        
        for i_linhas in range(0, n_linhas):
            progress(i_linhas/float(n_linhas))
            self.progresso = (i_linhas/float(n_linhas)) * 100
            for i_coluna in range(0, n_colunas):
                line = list()
                
                
                if threading.currentThread().stopped()  : return 
                    
                if nullValue != imagem_for_null_value[i_linhas][i_coluna] :
                            
                    for img in images:
                        line.append(img[i_linhas][i_coluna])
                    
                    cenaPico = self.findPeakHelper(line, int(intervalo_pico[0]), int(intervalo_pico[1])) # 3 - 23
                    data_txt_pico = images_super[cenaPico].file_name.replace(prefix, "").replace(sufix, "") 
                    data_pico = dt.strptime(data_txt_pico, mask)
                    ano_pico = data_pico.year
                    dia_juliano = data_pico.timetuple().tm_yday     
                    
                    imagem_pico[i_linhas][i_coluna] = ((ano_pico * 1000) + dia_juliano)
                      
                    cenaSemeadura = self.findLowPeakHelper(line, int(intervalo_semeadura[0]), int(intervalo_semeadura[1])) # 6 - 23
                    cenaColheita = self.findLowPeakHelper(line, int(intervalo_colheita[0]), int(intervalo_colheita[1])) # 11 - 34
                    
                    data_txt_semeadura = images_super[cenaSemeadura].file_name.replace(prefix, "").replace(sufix, "") 
                    data_semeadura = dt.strptime(data_txt_semeadura, mask)
                                   
                    data_txt_colheita = images_super[cenaColheita].file_name.replace(prefix, "").replace(sufix, "") 
                    data_colheita = dt.strptime(data_txt_colheita, mask)
                    
                    picoMenosSemeadura = data_pico - data_semeadura
                    ColheitaMenosPico = data_colheita - data_pico
                    data_semeadura += timedelta((picoMenosSemeadura.days * avanco_semeadura).days)
                    data_colheita += timedelta((ColheitaMenosPico.days * avanco_colheita).days)
                    
                    dia_juliano_semeadura = data_semeadura.timetuple().tm_yday 
                    imagem_semeadura[i_linhas][i_coluna] = ((data_semeadura.year * 1000) + dia_juliano_semeadura)
            
                    dia_juliano_colheita = data_colheita.timetuple().tm_yday 
                    imagem_colheita[i_linhas][i_coluna] = ((data_colheita.year * 1000) + dia_juliano_colheita)
                    
        saida = TableData()
        imagem_semeadura = RasterFile(data=imagem_semeadura)
        imagem_semeadura.metadata = images_super[0].metadata
        imagem_semeadura.data_name = "semeadura"
        
        imagem_colheita = RasterFile(data=imagem_colheita)
        imagem_colheita.metadata = images_super[0].metadata
        imagem_colheita.data_name = "colheita"
        
        imagem_pico = RasterFile(data=imagem_pico)
        imagem_pico.metadata = images_super[0].metadata
        imagem_pico.data_name = "cenaPico"
        
        saida["imagem_semeadura"] = imagem_semeadura
        saida["imagem_colheita"] = imagem_colheita
        saida["imagem_pico"] = imagem_pico
        
        return saida
    
    def findPeakHelper(self,num,start,end):
        mid = (start+end)/2
        if mid>start and mid < end:
            if(num[mid-1]<num[mid] and num[mid]>num[mid+1]):
                return mid
            if(num[mid-1]>num[mid]):
                return self.findPeakHelper(num,start,mid)
            else:
                return self.findPeakHelper(num,mid,end)
        else:
            if num[mid]>num[mid+1]:
                return mid
            else:return mid+1

    def findLowPeakHelper(self,num,start,end):
        mid = (start+end)/2
        if mid>start and mid < end:
            if(num[mid-1]>num[mid] and num[mid]<num[mid+1]):
                return mid
            if(num[mid-1]<num[mid]):
                return self.findLowPeakHelper(num,start,mid)
            else:
                return self.findLowPeakHelper(num,mid,end)
        else:
            if num[mid]>num[mid+1]:
                return mid
            else:return mid+1

    def valorPixelLinha(self, cena, vetor):
        if (cena - int(cena) > 0):
                valor = vetor[int(cena)] + ((vetor[int(cena)+1] - vetor[int(cena)]) * (cena - int(cena)))
        elif (cena - int(cena) < 0):  
                valor = vetor[int(cena)] + ((vetor[int(cena)] - vetor[int(cena)-1]) * (cena - int(cena)))
        else:
            valor = vetor[int(cena)]
        return valor




