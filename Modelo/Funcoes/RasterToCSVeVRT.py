# -*- coding: utf-8 -*-

'''
Created on Jan 21, 2015
@author: Paloschi
'''

from Modelo.beans import SerialFiles, TableData, FileData
from gdal import TermProgress_nocb
from Modelo.Funcoes import AbstractFunction
from Modelo.Funcoes import GetImageInformation
from lxml import etree

class RasterToCSVeVRT(AbstractFunction):
    '''
    Operacao que transforma imagens em arquivos CSV
    '''
    def __setParamIN__(self):
        self.descriptionIN["images"] = "lista de imagesn para transformar"
        self.descriptionIN["out_folder"] = "outro numero"
        
    def __setParamOUT__(self):
        self.descriptionOUT["CSVs"] = "lista de arquivos CSV"  
        
    def __execOperation__(self):
        
        imagensIN = self.brutedata["images"]
        outFolder = self.paramentrosIN_carregados["out_folder"]
        nullValue = float(-128)
        
        listaCSV = SerialFiles()
        listaVRT = SerialFiles()
        
        print "numero de imagens" + str(imagensIN)
        
        for img in imagensIN :
            matriz = img.loadData()
            nullValue = matriz[0][0]
            endereco_completo = img.data
            nome_img = img.data_name
            
            paramIN = TableData()
            paramIN["imagem"] = img
            
            getImgInfo = GetImageInformation.GetImgInfo()
            abd = GetImageInformation.GetImgInfo()
            abd.data = paramIN
            info = getImgInfo.data
            
            print (info)
    
            xmin = float(info["xmin"])
            xmax = float(info["xmax"])
            nx = float(info["nx"])
            x_pixelSize = (xmax - xmin) / nx
        
            ymin = float(info["ymin"])
            ymax = float(info["ymax"])
            ny = float(info["ny"])
            y_pixelSize = (ymax - ymin) / ny    
            
            print("-Criando arquivos CSV para alimentar intorpolador")
        
            progress = TermProgress_nocb   
            progress(0.0)
        
            n_linhas = len(matriz)
            n_colunas = len(matriz[0])
            
            file_csv_path = outFolder + nome_img + '.csv'
            
            print(file_csv_path)
            
            init_y_position = ymax - (y_pixelSize/2)
            init_x_position = xmin + (x_pixelSize/2)
        
            with open(file_csv_path,'w') as csv:
                csv.write("Easting,Northing,Value\n")
                for i_linha in range(0, n_linhas):
                    progress(i_linha/float(n_linhas))
                    cy = init_y_position - (y_pixelSize * i_linha)
                    cy = str(cy)
                    for i_coluna in range(0, n_colunas):
                        value = matriz[i_linha][i_coluna]
                        
                        if value != nullValue:                 
                            #print(cy)
                            cx = init_x_position + (x_pixelSize * i_coluna)
                            
                            line = str(cx) + ',' + cy + ',' + str(value) + '\n'
                            csv.write(line)
                            
            csv = FileData(data=file_csv_path)
            
            listaCSV.append(csv)
            
            cvs_name = file_csv_path.split("/")[-1].split(".")[0]
            file_vtr_path = outFolder + nome_img + '.vtr'
                
            root = etree.Element("OGRVRTDataSource")
            csv_node = etree.Element("OGRVRTLayer", name=cvs_name)   
            root.append(csv_node)
                                      
            csv_node.append(etree.XML("<SrcDataSource>" +file_csv_path+"</SrcDataSource>"))
            csv_node.append(etree.XML("<GeometryType>wkbPoint</GeometryType>"))
            csv_node.append(etree.XML('<GeometryField encoding="PointFromColumns" x="Easting" y="Northing" z="Value"/>'))
                
            tree = etree.ElementTree(root)
            tree.write(file_vtr_path, pretty_print=True)
            
            vrt = FileData(data=file_vtr_path)
            listaVRT.append(vrt)
                     
        print('-Arquivos CSV criados')

        saida = TableData()
        saida["CSVs"] = listaCSV
        saida["VRTs"] = listaVRT
        
        return saida