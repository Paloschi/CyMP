# -*- coding: utf-8 -*-
'''
Created on Apr 8, 2015

@author: Paloschi
'''

from Modelo.beans import Dados                                  
from numpy.core.numeric import array
import gdal
from Modelo.Funcoes import AbstractFunction
progress = gdal.TermProgress_nocb   
import matplotlib.pyplot as plt   

class ComparadorSemeaduraColheita(AbstractFunction.Function):
    '''
    
    '''

    def __setParamIN__(self): # Arrumar descrições
        self.descriptionIN["images_colheita_estimada"] = "Série de imagens para procurar as datas"
        self.descriptionIN["imagem_semeadura_estimada"] = "parametro para avanco de semeadura (Default: 0)"
        self.descriptionIN["imagem_colheita_produtor"] = "parametro para avanco de colheita (Default: 0)"
        self.descriptionIN["imagem_semeadura_produtor"] = "intervalo para procura da data nas imagens ex.: 3-24"
     
    def __setParamOUT__(self):
        self.descriptionOUT["txt_comparacao"] = "imagem com as datas de semeadura" 
        
    def __execOperation__(self):
        
        images_super = self.brutedata["images"]
        avanco_semeadura = self.paramentrosIN_carregados["avanco_semeadura"]
        avanco_colheita = self.paramentrosIN_carregados["avanco_colheita"]
        
        intervalo_semeadura = self.paramentrosIN_carregados["intervalo_semeadura"]
        intervalo_pico = self.paramentrosIN_carregados["intervalo_pico"]
        intervalo_colheita = self.paramentrosIN_carregados["intervalo_colheita"]
        
        intervalo_semeadura = intervalo_semeadura.split("-")
        intervalo_pico = intervalo_pico.split("-")
        intervalo_colheita = intervalo_colheita.split("-")
        
        images = images_super.loadData()
        
        n_linhas = len(images[0])
        n_colunas = len(images[0][0])
        nullValue = images[0][0][0]
        
        imagem_referencia = [[0 for x in range(n_colunas)] for x in range(n_linhas)]  
        
        imagem_semeadura = array(imagem_referencia)#.astype(dtype="int16")
        imagem_colheita = array(imagem_referencia)#.astype(dtype="int16")
        imagem_pico = array(imagem_referencia)#.astype(dtype="int16")
        
        progress( 0.0)
        
        for i_linhas in range(0, n_linhas):
            progress(i_linhas/float(n_linhas))
            #if i_linhas/float(n_linhas) > 0.15 : break
            for i_coluna in range(0, n_colunas):
                
                line = list()

                if nullValue == images[1][i_linhas][i_coluna] :
                    imagem_semeadura[i_linhas][i_coluna] = 0
                    
                else:              
                    for img in images:
                        line.append(img[i_linhas][i_coluna])
                    
                    pico = self.findPeakHelper(line, int(intervalo_pico[0]), int(intervalo_pico[1])) # 3 - 23
                    
                    imagem_pico[i_linhas][i_coluna] = pico
                      
                    low1 = self.findLowPeakHelper(line, int(intervalo_semeadura[0]), int(intervalo_semeadura[1])) # 6 - 23
                    low2 = self.findLowPeakHelper(line, int(intervalo_colheita[0]), int(intervalo_colheita[1])) # 11 - 34
                    
                    plt.plot([low1, low2], [line[low1], line[low2]], "ro")
                    
                    plt.plot([pico], [line[pico]], "yo")
                    
                    dSemeadura1 = pico - low1  
                    dColheita1 = low2 - pico
                    
                    acrecimoSemeadura1 = dSemeadura1 - avanco_semeadura
                    acrecimoColheita1 = dColheita1 - avanco_colheita
                    
                    cenaSemeadura1 = low1 + acrecimoSemeadura1
                    imagem_semeadura[i_linhas][i_coluna] = cenaSemeadura1
            
                    cenaColheita1 = low2 + acrecimoColheita1
                    imagem_colheita[i_linhas][i_coluna] = cenaColheita1
                    
                    plt.plot(line)
                    
                    #valorSemeadura1 = self.valorPixelLinha(cenaSemeadura1, line)
                    #valorColheita1 = self.valorPixelLinha(cenaColheita1, line)
                      
        plt.show()
        
        saida = Dados.TableData()
        
        imagem_semeadura = Dados.SimFileDatata=imagem_semeadura)
        imagem_semeadura.data_metadata = images_super[0].data_metadata
        imagem_semeadura.data_name = "semeadura"
        
        imagem_colheita = Dados.SimFileDatata=imagem_colheita)
        imagem_colheita.data_metadata = images_super[0].data_metadata
        imagem_colheita.data_name = "colheita"
        
        imagem_pico = Dados.SimFileDatata=imagem_pico)
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

    
line = ComparadorSemeaduraColheita()

root_ = "C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\3.EVI_Flat_Propriedades_SavitsGolay\\"
images = Dados.ListData()

images.loadListByRoot(root_, "tif")

parametrosIN = Dados.TableData()

parametrosIN["images"] = images
parametrosIN["avanco_semeadura"] = Dados.SimFileDatata=0)
parametrosIN["avanco_colheita"] = Dados.SimFileDatata=0)
parametrosIN["intervalo_pico"] = Dados.SimFileDatata="8-22")
parametrosIN["intervalo_semeadura"] = Dados.SimFileDatata="0-14")
parametrosIN["intervalo_colheita"] = Dados.SimFileDatata="14-27")

line.data = parametrosIN
imagens = line.data

semeadura = imagens["imagem_semeadura"]
colheita = imagens["imagem_colheita"]
pico = imagens["imagem_pico"]

semeadura.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\4.ImagensLowEpico\\", ext=".tif")
colheita.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\4.ImagensLowEpico\\", ext=".tif")
pico.saveImage("C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\4.ImagensLowEpico\\", ext=".tif")




