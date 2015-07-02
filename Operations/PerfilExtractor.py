# -*- coding: utf-8 -*-
'''
Created on Apr 8, 2015

@author: Paloschi
'''

from beans import Dados                                  
from numpy.core.numeric import array
import gdal
from Operations import OperationInterface
progress = gdal.TermProgress_nocb   
import matplotlib.pyplot as plt   
import datetime
from datetime import datetime as dt
from datetime import date


class ComparadorSemeaduraColheita(OperationInterface.Operation):
    '''
    Essa função foi criada para extrair as datas de semeadura (primeiro low peak), colheita (segundo low peak) e pico
    
    ela pode ser configurada pra procurar os picos e os picos inferiores em intervalos especificos que são equivalentes ao �ndice da imagem 
    na série de imagens
    
    também pode ser passado como parametro determinados avan�o que s�o relativos em porcentagem com a resolução temporal das imagems
    
    ex.: se o pico se dá na imagem 8 e colocar um avanço na data de colheita de -0,50 será feito 8 - 0,50 = 7,5, a data de colheita para esse pixel será 7,5 imagens
    
    '''

    def __setParamIN__(self):
        self.descriptionIN["images"] = "Série de imagens para procurar as datas"
        self.descriptionIN["avanco_semeadura"] = "parametro para avanco de semeadura (Default: 0)"
        self.descriptionIN["avanco_colheita"] = "parametro para avanco de colheita (Default: 0)"
        self.descriptionIN["intervalo_semeadura"] = "intervalo para procura da data nas imagens ex.: 3-24"
        self.descriptionIN["intervalo_pico"] = "intervalo para procura da data nas imagens ex.: 3-24"
        self.descriptionIN["intervalo_colheita"] = "intervalo para procura da data nas imagens ex.: 3-24"
        self.descriptionIN["null_value"] = "valor nulo a ser ignorado"
        #self.descriptionIN["progress_bar"] = "barra de progresso"
     
    def __setParamOUT__(self):
        self.descriptionOUT["imagem_semeadura"] = "imagem com as datas de semeadura" 
        self.descriptionOUT["imagem_pico"] = "imagem com as datas de pico vegetativo" 
        self.descriptionOUT["imagem_colheita"] = "imagem com as datas de colheita" 
        
    def __execOperation__(self):
        
        prefix = "_FiltroSavitsGolayMODMYD13Q1."
        sufix = ".250m_16_dias_EVI_PR_EbM"
        
        mask =  "%Y%m%d"
        
        images_super = self.brutedata["images"]
        avanco_semeadura = self.paramentrosIN_carregados["avanco_semeadura"]
        avanco_colheita = self.paramentrosIN_carregados["avanco_colheita"]
        
        intervalo_semeadura = self.paramentrosIN_carregados["intervalo_semeadura"]
        intervalo_pico = self.paramentrosIN_carregados["intervalo_pico"]
        intervalo_colheita = self.paramentrosIN_carregados["intervalo_colheita"]
        
        #barra_progresso = self.paramentrosIN_carregados["progress_bar"]
        
        intervalo_semeadura = intervalo_semeadura.split("-")
        intervalo_pico = intervalo_pico.split("-")
        intervalo_colheita = intervalo_colheita.split("-")
        
        images = images_super.loadData()
        
        n_linhas = len(images[0])
        n_colunas = len(images[0][0])
        
        #nullValue = images[0][0][0]
        nullValue = float(self.paramentrosIN_carregados["null_value"])
        
        if(images[0][0][0] == nullValue) : print("null value igual") 
        else : print("diferente")
        
        imagem_referencia = [[0 for x in range(n_colunas)] for x in range(n_linhas)]  
        
        imagem_semeadura = array(imagem_referencia)#.astype(dtype="int16")
        imagem_colheita = array(imagem_referencia)#.astype(dtype="int16")
        imagem_pico = array(imagem_referencia)#.astype(dtype="int16")
        
        progress( 0.0)
        
        for i_linhas in range(0, n_linhas):
            progress(i_linhas/float(n_linhas))
            #if (barra_progresso!=None) : barra_progresso.setProperty("value", (i_linhas/float(n_linhas))*100)
            self.progresso = ((i_linhas/float(n_linhas))*100)
            #if i_linhas/float(n_linhas) > 0.05 : break
            for i_coluna in range(0, n_colunas):
                line = list()

                if nullValue == images[1][i_linhas][i_coluna] :
                    imagem_semeadura[i_linhas][i_coluna] = 0
                    
                else:              
                    for img in images:
                        line.append(img[i_linhas][i_coluna])
                    
                    pico = self.findPeakHelper(line, int(intervalo_pico[0]), int(intervalo_pico[1])) # 3 - 23
                    data_txt = images_super[pico].data_name.replace(prefix, "").replace(sufix, "") 
                    ano = dt.strptime(data_txt, mask).year
                    dia_juliano = dt.strptime(data_txt, mask).timetuple().tm_yday       
                    imagem_pico[i_linhas][i_coluna] = ((ano * 1000) + dia_juliano)
                      
                    cenaSemeadura = self.findLowPeakHelper(line, int(intervalo_semeadura[0]), int(intervalo_semeadura[1])) # 6 - 23
                    cenaColheita = self.findLowPeakHelper(line, int(intervalo_colheita[0]), int(intervalo_colheita[1])) # 11 - 34
                    
                    #plt.plot([pico], [line[pico]], "yo")
                    
                    data_txt = images_super[cenaSemeadura].data_name.replace(prefix, "").replace(sufix, "") 
                    ano = dt.strptime(data_txt, mask).year
                    dia_juliano = dt.strptime(data_txt, mask).timetuple().tm_yday 
                    imagem_semeadura[i_linhas][i_coluna] = ((ano * 1000) + dia_juliano)
            
            
                    data_txt = images_super[cenaColheita].data_name.replace(prefix, "").replace(sufix, "") 
                    ano = dt.strptime(data_txt, mask).year
                    dia_juliano = dt.strptime(data_txt, mask).timetuple().tm_yday 
                    imagem_colheita[i_linhas][i_coluna] = ((ano * 1000) + dia_juliano)
                    
                    #plt.plot(line)
                      
        #plt.show()
        
        saida = Dados.TableData()
        
        imagem_semeadura = Dados.SimpleData(data=imagem_semeadura)
        imagem_semeadura.data_metadata = images_super[0].data_metadata
        imagem_semeadura.data_name = "semeadura"
        
        imagem_colheita = Dados.SimpleData(data=imagem_colheita)
        imagem_colheita.data_metadata = images_super[0].data_metadata
        imagem_colheita.data_name = "colheita"
        
        imagem_pico = Dados.SimpleData(data=imagem_pico)
        imagem_pico.data_metadata = images_super[0].data_metadata
        imagem_pico.data_name = "pico"
        
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
            #if (vetor[int(cena)+1] - vetor[int(cena)]) > 0:
                valor = vetor[int(cena)] + ((vetor[int(cena)+1] - vetor[int(cena)]) * (cena - int(cena)))
            #else:
             #   valor = vetor[int(cena)] + ((vetor[int(cena)] - vetor[int(cena)+1]) * (cena - int(cena)))
                
        elif (cena - int(cena) < 0):  
            #if  (vetor[int(cena)] - vetor[int(cena)-1]) > 0:
                valor = vetor[int(cena)] + ((vetor[int(cena)] - vetor[int(cena)-1]) * (cena - int(cena)))
            #else:
            #    valor = vetor[int(cena)] + ((vetor[int(cena)-1] - vetor[int(cena)]) * (cena - int(cena)))
        else:
            valor = vetor[int(cena)]
        return valor

    
#line = ComparadorSemeaduraColheita()

#root_ = "C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\3.EVI_Flat_Propriedades_SavitsGolay\\"
#images = Dados.SerialData()

#images.loadListByRoot(root_, "tif")

#parametrosIN = Dados.TableData()

#parametrosIN["images"] = images
#parametrosIN["avanco_semeadura"] = Dados.SimpleData(data=0)
#parametrosIN["avanco_colheita"] = Dados.SimpleData(data=0)
#parametrosIN["intervalo_pico"] = Dados.SimpleData(data="8-22")
#parametrosIN["intervalo_semeadura"] = Dados.SimpleData(data="0-14")
#parametrosIN["intervalo_colheita"] = Dados.SimpleData(data="14-27")

#line.data = parametrosIN
#imagens = line.data

#semeadura = imagens["imagem_semeadura"]
#colheita = imagens["imagem_colheita"]
#pico = imagens["imagem_pico"]

#semeadura.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\4.ImagensLowEpico\\", ext=".tif")
#colheita.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\4.ImagensLowEpico\\", ext=".tif")
#pico.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\4.ImagensLowEpico\\", ext=".tif")




