'''
Created on Mar 1, 2015

@author: Paloschi
'''
from Modelo.beans import Dados
from lxml import etree


class InterpolaTabela(Dados.AbtractData):
    
    '''
    faz todos os tramites necessarios pra interpolar uma tabela
    '''
    
    def __init__(self, nome):
        self.__data = None
        self.data_name = nome
        self.data_type = "operation"
    
    @property    
    def data(self):             
        dados = self.__data.data
        table = dados['table_data']
        tabela_data = table.data
        atributo_interpolacao = dados['atributo']
        format_image_data = dados['format_image_data']
        
        print("Preparando interpolacao:")
              
        self.WriteVRTfiles(tabela_data, atributo_interpolacao)        
        self.WriteCSVfiles(tabela_data, atributo_interpolacao)
        
        path = tabela_data['data_path']
        keys = tabela_data.keys()
        
        print("Preparacao completa, interpolando:")
        
        for key in keys: 
            if (key!="data_path"):           
                informacao = self.CreateInterpolationTable(path, key, atributo_interpolacao, format_image_data)
                
                interpolation_table = Dados.TableData("iformacao de interpolacao")
                interpolation_table.data = informacao
                
                interpolador = InterpoladorIvD("interpolando ECMWF")
                interpolador.data = interpolation_table
            
                print (interpolador.data)
            
        print ("Interpolacao completa")
        return ("Interpolacao completa")
        
    @data.setter
    def data(self, data):
        self.__data = data
        
    def WriteCSVfiles(self, table, atribute):
        
        print("-Criando arquivos CSV para alimentar intorpolador")
        
        path = table['data_path']
        keys = table.keys()
        
        for key in keys:
            if (key!="data_path"):   
                file_path = str(path).replace('.shp', ('_' + str(key) + "_" + atribute + '.csv'))
                with open(file_path,'w') as csv:
                    csv.write("Easting,Northing,Value\n")
                    for tupla in table[key]:
                        print(tupla['geometry']['coordinates'])
                        cx = tupla['geometry']['coordinates'][0]
                        cy = tupla['geometry']['coordinates'][1]
                        value = tupla['properties'][atribute]
                        line = str(cx) + ',' + str(cy) + ',' + str(value) + '\n'
                        csv.write(line)
                    
        print('-Arquivos CSV criados')

    def WriteVRTfiles(self, table, atribute):
        
        print("-Criando arquivos VTR para alimentar intorpolador")
        
        path = table['data_path']
        keys = table.keys()
        
        for key in keys:
            if (key!="data_path"): 
                
                
                file_csv_path = str(path).replace('.shp', ('_' + str(key) + "_" + atribute +'.csv'))  
                cvs_name = file_csv_path.split("/")[-1].split(".")[0]
                file_vtr_path = str(path).replace('.shp', ('_' + str(key) + "_" + atribute +'.vrt'))
                
                root = etree.Element("OGRVRTDataSource")
                csv_node = etree.Element("OGRVRTLayer", name=cvs_name)   
                root.append(csv_node)
                                      
                csv_node.append(etree.XML("<SrcDataSource>" +file_csv_path+"</SrcDataSource>"))
                csv_node.append(etree.XML("<GeometryType>wkbPoint</GeometryType>"))
                csv_node.append(etree.XML('<GeometryField encoding="PointFromColumns" x="Easting" y="Northing" z="Value"/>'))
                
                tree = etree.ElementTree(root)
                tree.write(file_vtr_path, pretty_print=True)
                    
        print('-Arquivos CSV criados')
    
    def CreateInterpolationTable(self, path, tupla, atribute,  format_image_data):
      
        file_vtr_path = str(path).replace('.shp', ('_' + str(tupla) + "_" + atribute + '.vrt'))
        file_tif_path = str(path).replace('.shp', ('_' + str(tupla) + "_" + atribute + '.tif'))
        cvs_name = file_vtr_path.split("/")[-1].split(".")[0]
        format_image_data["fileIn"] = file_vtr_path
        format_image_data["fileOut"] = file_tif_path
        format_image_data["name_file"] = cvs_name
        
        return format_image_data
    
class InterpoladorIvD(Dados.AbtractData):
    '''
    classdocs
    '''

    def __init__(self, nome=None):
        self.__data = None
        self.data_name = [nome, 'interpolacao'] 
        self.data_type = "operation"
    
    @property    
    def data(self):
        
        tabela = self.__data.data
        
        #print (["xmin",  tabela['xmin']])
        
        xmin = tabela['xmin']
        xmax = tabela['xmax']
        ymin = tabela['ymin']
        ymax = tabela['ymax']
        ny = tabela['ny']
        nx = tabela['nx']
        fileIn = tabela['fileIn']
        #fileOut = str(fileIn).replace(".vrt", "interpolado.tiff")
        fileOut = tabela['fileOut']
        name_file = tabela['name_file']
        
        
        try:
            self.call_interpolador(xmin, xmax, ymin, ymax, nx, ny, name_file, fileIn, fileOut)
            
            return fileOut
        
        except Exception:
            print 'erro ao chamar subprocesso gdal_grid'
            return Exception()
        
    @data.setter
    def data(self, data):
        self.__data = data
           
    def call_interpolador(self, xmin, xmax, ymin, ymax, nx, ny, name_file, fileIn, fileOut):

        import subprocess
        
        subprocess.call (['gdal_grid', '-a', 'invdist:radius1=0.36:radius2=0.36:smoothing=0.1', '-txe', 
                              str(xmin), str(xmax), '-tye', str(ymin), str(ymax), '-outsize', 
                              str(nx), str(ny), '-of', 'GTiff', '-ot', 'Float64', '-l', name_file, fileIn, fileOut]) 

            