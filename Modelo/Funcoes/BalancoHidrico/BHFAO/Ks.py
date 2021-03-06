# -*- coding: utf-8 -*-
'''
Created on Nov 18, 2015

@author: rennan.paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA
import threading
import numpy
from Modelo.beans.RasterData import RasterFile

class Ks(AbstractFunction):
    
    def __setParamIN__(self):
        
        self.descriptionIN["RAW"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagem RAW"}
        self.descriptionIN["TAW"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens TAW"}
        self.descriptionIN["Dr"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagem Dr"}
        self.descriptionIN["Ks"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagem Ks"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["Ks"] = {"Type":SERIAL_FILE_DATA, "Description":"Série de imagen Ks"}
    
    def __execOperation__(self):
        
        serie_raw = self.paramentrosIN_carregados["RAW"].loadListByRoot()
        serie_taw = self.paramentrosIN_carregados["TAW"].loadListByRoot()
        serie_dr = self.paramentrosIN_carregados["Dr"].loadListByRoot()
        
        serie_ks = self.paramentrosIN_carregados["Ks"]
        
        #factor_raw = float(serie_raw.mutiply_factor)
        #factor_taw = float(serie_taw.mutiply_factor)
        #factor_dr = float(serie_dr.mutiply_factor)
        #factor_ks = float(serie_ks.mutiply_factor)
        
        n_taw = len(serie_taw)
        
        taw_ = serie_taw[0].loadRasterData()

        n_linhas = len(taw_)
        n_colunas = len(taw_[0])

        for i in range(n_taw):
            
            if threading.currentThread().stopped()  : return 
            self.setProgresso(i, n_taw)
            
            taw = serie_taw[i]
            data_taw = serie_taw.getDate_time(file=taw)
            taw_ = numpy.array(taw.loadRasterData()).astype(dtype="float32")
            #taw_ *= factor_taw
            
            raw_ = self.LoadImgByDate(serie_raw, data_taw, 1)
        
            dr_ = self.LoadImgByDate(serie_dr, data_taw, 1)
            
            if dr_ is None: 
                self.console(u"Aviso: Imagem de Dr para a data: " + str(data_taw))

            if raw_ is None: 
                self.console(u"Aviso: Imagem de RAW para a data: " + str(data_taw)) 
                
            if dr_ is not None and raw_ is not None:     
                       
                ''' ----------------------------------------------- '''
                
                ks_ = numpy.zeros((n_linhas, n_colunas))
                #ks_ +=1
                
                ''' ----------------------------------------------- '''
                

                
                a = (taw_ - (- dr_)) 
                b = (taw_ - raw_)
                c = a / b
                
                
                
                for i in range(len(ks_)) :
    
                    ks_[i][-dr_[i] >= raw_[i]] = c[i][-dr_[i] >= raw_[i]]
                    ks_[i][-dr_[i] < raw_[i]] = 1
                    ks_[i][ks_[i] == -float('Inf')] = -1
                    ks_[i][taw_[i] == float('NaN')] = -1
                    
                    #ks_[i][taw_[i] == 127] = taw.metadata["nodata"]
                    #ks_[i][raw_[i] == 0] = taw.metadata["nodata"]
    
                    
                
                ''' ------------------------------------------------ '''

                         
                #ks_ = numpy.round(ks_, 2)  
                #ks_ *= factor_ks
                #ks_ = self.compactar(ks_)
                
                #ks_ = numpy.ma.masked_array(ks_, 999)
                
                ks_ = 1 - ks_ # invertendo o Ks pra dar certo na formulas
                
                
                print ("Valor de taw_:" + str(taw_[60][83]))
                print ("Valor de raw_:" + str(raw_[60][83]))
                print ("Valor de dr_:" + str(dr_[60][83]))    
                print ("Valor de Ks:" + str(ks_[60][83]))  
                print ("------------------------------")
                
                #print data_taw
                #for i in range(n_linhas):
                    #for ii in range(n_colunas):
                        #if taw_[i][ii] != 0.0 and taw_[i][ii] != 127.0 and ks_[i][ii] != 1 and ks_[i][ii] != 0:
                            #print a[i][ii], b[i][ii], c[i][ii]
                            #print taw_[i][ii], raw_[i][ii], dr_[i][ii], ks_[i][ii]
                            #print "----------------------------------"
                
                
                ks = RasterFile(file_path=serie_ks.root_path, ext="tif")
                ks = serie_ks.setDate_time(data_taw, file=ks)       
                ks.data = ks_.astype(dtype="float32")
                ks.metadata = taw.metadata
                ks.metadata.update(dtype = ks.data.dtype)
                ks.metadata.update(nodata=2)
                ks.saveRasterData()
                ks.data = None
                serie_ks.append(ks)
            
        return serie_ks
            
    def LoadImgByDate(self, serie, date, factor): 
        try:    
            img = self.procura_img_por_data(serie, date)
            img_ = numpy.array(img.loadRasterData()).astype(dtype="float32")
            return img_
        except:
            return None