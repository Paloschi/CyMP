# -*- coding: utf-8 -*-

'''
Created on Jan 21, 2015
@author: Paloschi
'''

from Modelo.beans import SerialFile, TableData, FileData, SERIAL_FILE_DATA 
import gdal
import Modelo
progress = gdal.TermProgress_nocb
from Modelo.Funcoes import AbstractFunction
from lxml import etree
import threading

class RasterToCSVeVRT(AbstractFunction):
    '''
    Operacao que transforma imagens em arquivos CSV
    '''
    def __setParamIN__(self):
        self.descriptionIN["images"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"lista de imagens para transformar"}
        self.descriptionIN["out_folder"] = {"Required":True, "Type":None, "Description":"Pasta de saida para os arquivos CSV"}
        
    def __setParamOUT__(self):
        self.descriptionOUT["CSVs"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"lista de arquivos CSV"}
        self.descriptionOUT["VRTs"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"lista de arquivos vrt"}
        
    def __execOperation__(self):
        
        imagensIN = self.paramentrosIN_carregados["images"]
        outFolder = self.paramentrosIN_carregados["out_folder"]
        
        imagensIN.loadListByRoot()
        
        listaCSV = SerialFile()
        listaVRT = SerialFile()
        
        n_imagens = len(imagensIN)
        i_imagem = 0
        self.setProgresso(i_imagem, n_imagens)
        
        for img in imagensIN :

            matriz = img.loadRasterData()
            nome_img = img.file_name
            info = img.getRasterInformation()
    
            xmin = float(info["xmin"])
            xmax = float(info["xmax"])
            nx = float(info["nx"])
            x_pixelSize = (xmax - xmin) / nx
        
            ymin = float(info["ymin"])
            ymax = float(info["ymax"])
            ny = float(info["ny"])
            y_pixelSize = (ymax - ymin) / ny    
        
            n_linhas = len(matriz)
            n_colunas = len(matriz[0]) 
            
            csv_file = FileData(file_path=outFolder, file_name = nome_img, ext = "csv")
            file_csv_path = csv_file.file_full_path
            
            init_y_position = ymin + (y_pixelSize/2)
            init_x_position = xmin + (x_pixelSize/2)
            
            with open(file_csv_path,'w') as csv:
                csv.write("Easting,Northing,Value\n")
                for i_linha in range(0, n_linhas):
                    progress(i_linha/float(n_linhas-1))
                        
                    cy = init_y_position + (y_pixelSize * i_linha)
                    cy = str(cy)
                    for i_coluna in range(0, n_colunas):
                        
                        value = matriz[i_linha][i_coluna]
                        if threading.current_thread().stopped() : return None

                        cx = init_x_position + (x_pixelSize * i_coluna)
                        line = str(cx) + ',' + cy + ',' + str(value) + '\n'
                        csv.write(line)

            listaCSV.append(csv_file)
            
            vrt_file = csv_file
            vrt_file.file_ext = "vrt"
                
            root = etree.Element("OGRVRTDataSource")
            csv_node = etree.Element("OGRVRTLayer", name=csv_file.file_name)   
            root.append(csv_node)
                                      
            csv_node.append(etree.XML("<SrcDataSource>" +file_csv_path+"</SrcDataSource>"))
            csv_node.append(etree.XML("<GeometryType>wkbPoint</GeometryType>"))
            csv_node.append(etree.XML('<GeometryField encoding="PointFromColumns" x="Easting" y="Northing" z="Value"/>'))
                
            tree = etree.ElementTree(root)
            tree.write(vrt_file.file_full_path, pretty_print=True)
            
            listaVRT.append(vrt_file)
            
            i_imagem = i_imagem + 1.0
            self.setProgresso(i_imagem, n_imagens)

        saida = TableData()
        saida["CSVs"] = listaCSV
        saida["VRTs"] = listaVRT
        
        return saida

if __name__ == '__main__':   
    
    img_teste_path = "C:\\Users\\rennan.paloschi\\Desktop\\Dados_Gerais\\raster\\ECMWF\\Teste_raster_csv\\Imagens"
    img_teste = SerialFile(root_path=img_teste_path)
    img_teste.loadListByRoot()
    
    paramIN = dict()
    paramIN["images"] = img_teste
    paramIN["out_folder"] = "C:\\Users\\rennan.paloschi\\Desktop\\Dados_Gerais\\raster\\ECMWF\\Teste_raster_csv\\Saida\\"
    
    f = RasterToCSVeVRT()
    
    f.executar(paramIN)
    