# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2015

@author: Paloschi
'''
from Modelo.Funcoes import AbstractFunction
from Modelo.beans.AbstractData import FILE_DATA, TABLE_DATA
import subprocess

class IDW(AbstractFunction):
    '''
        Essa função realiza a interpolação IDW (inverso da distancia) de arquivos CSV configurados por arquivos VRT
        ela necessita do GDAL Core instalado pra funcionar, e o path do GDAL Core tem que estar
        setado na variavel de ambiente path do windows
    '''
    
    def __setParamIN__(self):
        u'''
            Parametros de arquivos de dados (csv, vrt e imagem de saida)
        '''
        self.descriptionIN["csv"] = {"Required":True, "Type":FILE_DATA, "Description":"nome do arquivo CSV"}
        self.descriptionIN["vrt"] = {"Required":True, "Type":FILE_DATA, "Description":"caminho completo do arquivo VRT"}
        self.descriptionIN["img_out"] = {"Required":True, "Type":FILE_DATA, "Description":"caminho completo da imagem de saida"}
        
        '''
            Parametros de configuração do algorítimo
        '''
        conf_algoritimo = dict()
        conf_algoritimo["power"] = {"Required":False, "Type":None, "Description":"Weighting power (default 2.0)"}
        conf_algoritimo["smoothing"] = {"Required":False, "Type":None, "Description":"Smoothing parameter (default 0.0)"}
        conf_algoritimo["radius1"] = {"Required":False, "Type":None, "Description":"The first radius (X axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0"}
        conf_algoritimo["radius2"] = {"Required":False, "Type":None, "Description":"The second radius (Y axis if rotation angle is 0) of search ellipse. Set this parameter to zero to use whole point array. Default is 0.0."}
        conf_algoritimo["angle"] = {"Required":False, "Type":None, "Description":"Angle of search ellipse rotation in degrees (counter clockwise, default 0.0)"}
        conf_algoritimo["max_points"] = {"Required":False, "Type":None, "Description":"Maximum number of data points to use. Do not search for more points than this number. This is only used if search ellipse is set (both radii are non-zero). Zero means that all found points should be used. Default is 0"}
        conf_algoritimo["min_points"] = {"Required":False, "Type":None, "Description":"Minimum number of data points to use. If less amount of points found the grid node considered empty and will be filled with NODATA marker. This is only used if search ellipse is set (both radii are non-zero). Default is 0"}
        conf_algoritimo["nodata"] = {"Required":False, "Type":None, "Description":"NODATA marker to fill empty points (default 0.0)"}
        
        self.descriptionIN["conf_algoritimo "] = {"Required":False, "Type":TABLE_DATA, "Table_Description":conf_algoritimo,"Description":"tabela de parametros para configuração do algoritimo"}
        
        u'''
            Parametros de configuração da imagem de saida
        '''
        conf_img_out = dict()
        conf_img_out["xmin"] = {"Required":True, "Type":None, "Description":u"posição inicial x"}
        conf_img_out["xmax"] = {"Required":True, "Type":None, "Description":u"posição final x"}
        conf_img_out["ymin"] = {"Required":True, "Type":None, "Description":u"posição inicial y"}
        conf_img_out["ymax"] = {"Required":True, "Type":None, "Description":u"posição final y"}
        conf_img_out["ny"] = {"Required":True, "Type":None, "Description":"Numero de linhas da imagem"}
        conf_img_out["nx"] = {"Required":True, "Type":None, "Description":"Numero de colunas da imagem"}
        
        self.descriptionIN["img_out_config"] =  {"Required":True, "Type":TABLE_DATA, "Table_Description":conf_img_out, "Description":"configuração da imgagem de saida"}
        
    def __setParamOUT__(self):
        self.descriptionOUT["imagem_interpolada"] = "imagem de saida interpolada"  
        
    def __execOperation__(self):
        
        csv = self.paramentrosIN_carregados["csv"]
        vrt = self.paramentrosIN_carregados["vrt"]
        img_out = self.paramentrosIN_carregados["img_out"]
        img_out_config = self.paramentrosIN_carregados["img_out_config"]
        
        '''
            Monta string de de parametros para configurar o algoritimo IDW
        '''
        str_algoritimo_conf = ""
        
        if self.paramentrosIN_carregados.has_key("conf_algoritimo") :
            conf_algoritimo = self.paramentrosIN_carregados["conf_algoritimo"]
            for key in conf_algoritimo.keys() :
                str_algoritimo_conf.join(key + "=" + str(conf_algoritimo[key]))
        
        '''
            Chama interpolador GDAl IDW
        '''
        try:
            subprocess.call (['gdal_grid', 
                              '-a', str_algoritimo_conf, 
                              '-txe', str(img_out_config["xmin"]), str(img_out_config["xmax"]), 
                              '-tye', str(img_out_config["ymin"]), str(img_out_config["ymax"]), 
                              '-outsize', str(img_out_config["nx"]), str(img_out_config["ny"]), 
                              '-of', 'GTiff', 
                              '-ot', 'Float64', 
                              '-l', csv.data_name, vrt.path, img_out.path]) 
            
        
        except Exception:
            print 'erro ao chamar subprocesso gdal_grid, verifiquei se a GDAL core está instalada e a variavel de ambiente está setada'
            
        saida = img_out.path
        
        return saida

