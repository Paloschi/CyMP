# -*- coding: utf-8 -*-
'''
Created on Jul 22, 2015

@author: Paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans import SERIAL_FILE_DATA
import gdal
from Modelo.beans.RasterData import RasterFile
progress = gdal.TermProgress_nocb
import numpy
import threading

class Etc(AbstractFunction):
    '''
        Essa função calcula a evapotranspiração da cultura ETc, baseado nas datas de plantio, evapotranspiração de referencia
    e os coeficientes da cultura.
        Formula: ETc = Kc * ET0
        Onde o Kc varia dependendo do estado fenologico da cultura.
        Para efeitos de histórico, periodos de ETc anteriores ao periodo da cultura devem ser inseridos, por default quando a
    cultura não está presente, o Kc é considerado de valor 1
        
        Esta função não entende datas por isso todos os parametros devem ser passados com referencia a cena
    '''
    
    def __setParamIN__(self):
        
        self.descriptionIN["ET0"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de evapotranspiração de referencia"}
        self.descriptionIN["Kc"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens de Kc distribuido"}
        self.descriptionIN["ETc"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Objeto série de imagens configurao para saida"}
        #self.descriptionIN["dias_inicio"] = {"Required":True, "Type":None, "Description":"Indica quantos dias anteriores a primeira data de semeadura que deve ser considerado"}
    
    def __setParamOUT__(self):
        self.descriptionOUT["ETc"] = {"Type":SERIAL_FILE_DATA, "Description":"Série de imagens de evapotranspiração da cultura"}
    
    def __execOperation__(self):
        '''
            Por padrão agora assumo que, quando uma variavel tiver como sufixo um underline "_"
            é porque esta variavel contem os valores carregados (matrizes brutas) dos dados
        '''
        
        self.print_text("Carregando imagens.")
        
        serie_ET0 = self.paramentrosIN_carregados["ET0"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_Kc = self.paramentrosIN_carregados["Kc"].loadListByRoot() # pucha e já carrega a lista caso não tenha sido carregada
        serie_ETc = self.paramentrosIN_carregados["ETc"] # pucha lista
        
        #Kc_factor = float(serie_Kc.mutiply_factor)
        ET0_factor = float(serie_ET0.mutiply_factor)
        #ETC_factor = float(serie_ETc.mutiply_factor)
        
        n_Kc = len(serie_Kc)
        
        self.console(str(n_Kc) + " imagens de Kc encontradas.")
        self.console(str(len(serie_ET0)) + " imagens de ETo encontradas.")
        
        self.console(u"Gerando imagens de saída...")

        '''
            O laço a seguir percorre todas as imagens de ET0 presentes
            ele verifica se há imagens de Kc correspondentes para realizar a multiplicação
            caso não haja ele simplesmente mantém a imagem de ET0 como imagem de ETc
            
            O calculo de Etc é Etc = Et0 * Kc
        '''
        i_ETo = None

        for i_Kc in range(n_Kc):
            
            if threading.currentThread().stopped()  : return

            self.setProgresso(i_Kc, n_Kc)

            kc = serie_Kc[i_Kc]

            data_kc = serie_Kc.getDate_time(file=kc)

            ET0 = None
            data_ETo = None
            if i_ETo is not None:
                i_ETo += 1
                data_ETo = serie_ET0.getDate_time(file=serie_ET0[i_ETo])

            if data_ETo is not None and data_ETo == data_kc: ET0 = serie_ET0[i_ETo]
            else:
                for i_ETo in range(0, len(serie_ET0)):
                    data_ETo = serie_ET0.getDate_time(file=serie_ET0[i_ETo])
                    if data_ETo == data_kc:
                        ET0 = serie_ET0[i_ETo]
                        break

            
            etc = RasterFile(file_path=serie_ETc.root_path, ext="tif")
            etc = serie_ETc.setDate_time(data_kc, file=etc)
            
            ET0_ = numpy.array(ET0.loadRasterData()).astype(dtype="float32") #* ET0_factor

            # ET0_ = (ET0_ * 100) * -1 ## comentar se for pra calcular ETa

            ET0_[ET0_==ET0.metadata["nodata"]] = 0 
            #ET0_ = ET0_ * ET0_factor # Problemas com o factor
            
            if kc is None: # caso não encontre nenhum kc correspondente a mesma data
                self.console(u"Sem Kc para o dia" + str(data))
                ETc_ = ET0_
                #ETc_ *= ETC_factor # Problemas com o factor
                #ETc_ = self.compactar(ETc_)
                etc.data = ETc_

            else:

                Kc_ = numpy.array(kc.loadRasterData()).astype(dtype="float32")


                #Kc_ *= Kc_factor # Problemas com o factor
                ETc_ = Kc_ * ET0_

                print("Shape kc:", Kc_.shape)
                print("Shape ET0:", ETc_.shape)
                #ETc_ *= ETC_factor # Problemas com o factor
                #ETc_ = self.compactar(ETc_) # Problemas com o factor
                etc.data = ETc_

                print("Valor de Kc/ETc:" + str(Kc_[970][483]))
                print("Valor de ETc/ETa:" + str(ETc_[970][483]))
                print("Valor de ET0/Ks:" + str(ET0_[970][483]))
                print("------------------------------")
            etc.metadata = ET0.metadata
            etc.metadata.update(nodata=0)
            etc.metadata.update(dtype = etc.data.dtype)
            etc.saveRasterData()
            
            serie_ETc.append(etc)
            
        self.console(u"Concluído")
            
        return serie_ETc
            
    
    def procurar_descende_correspondente(self, data, serie_temporal):
        '''
            Esse método procura a imagem correspondente para a data informada (feito para capturar o descende correto)
        '''
        img_correspondente = None
        
        for i_img in range(len(serie_temporal)-1):
            data_img =  serie_temporal.getDate_time(i_img)
            data_img_1 = serie_temporal.getDate_time(i_img+1)
            if data_img == data : 
                img_correspondente = serie_temporal[i_img]
                self.dias_decend = (data_img_1 - data_img).days
                break
            elif data_img < data and data_img_1 > data: 
                img_correspondente = serie_temporal[i_img]
                self.dias_decend = (data_img_1 - data_img).days
        
        if img_correspondente == None : img_correspondente = serie_temporal[-1]
           
        return img_correspondente

if __name__ == '__main__':
    from Modelo.beans import SerialTemporalFiles
    
    serie_Kc = SerialTemporalFiles(root_path="D:\\Agririsk\\Coamo_FAO_estimation\\Kc_2016_2017")
    serie_Kc.mutiply_factor = 1
    serie_Kc.date_mask = "%Y-%m-%d"
    
    serie_ET0 = SerialTemporalFiles(root_path="D:\\Agririsk\\Coamo_FAO_estimation\\ETo")
    serie_ET0.mutiply_factor = -1
    serie_ET0.sufixo = "ET0_"
    serie_ET0.date_mask = "%Y-%m-%d"
    
    serie_ETC = SerialTemporalFiles(root_path="D:\\Agririsk\\Coamo_FAO_estimation\\ETc")
    serie_ETC.mutiply_factor = 100
    serie_ETC.out_datatype = "int16"
    #serie_ETC.sufixo = "ETc_"
    serie_ETC.date_mask = "%Y-%m-%d"
    
    paramIN = dict()
    paramIN["ET0"] = serie_ET0
    paramIN["ETc"] = serie_ETC
    paramIN["Kc"] = serie_Kc
    
    Etc().executar(paramIN)
    


