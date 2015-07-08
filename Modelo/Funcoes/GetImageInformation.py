'''
Created on Mar 1, 2015

@author: Paloschi
'''

import subprocess
from Modelo.Funcoes import AbstractFunction

class GetImgInfo(AbstractFunction.Function):
    '''
    recupera informacoes de imagens como numero de linhas e tamanho da imagem para usar na interpolacao por exemplo
    '''
    caption_nx_ny_name = 'Size is ' 
    caption_xmin_ymin = 'Upper Left'
    caption_xmax_xmin = 'Lower Right'
        
    def __setParamIN__(self):
        self.descriptionIN["imagem"] = "uma imagem tif para coletar suas informacoes"
        
    def __setParamOUT__(self):
        self.descriptionOUT["nx"] = "numero de colunas da imagem"  
        self.descriptionOUT["ny"] = "numero de linhas da imagem"  
        self.descriptionOUT["ymax"] = "coordenada y maxima da imagem"  
        self.descriptionOUT["ymin"] = "coordenada y minima da imagem"
        self.descriptionOUT["xmax"] = "coordenada x maxima da imagem"  
        self.descriptionOUT["xmin"] = "coordenada x minima da imagem"
    
    def __execOperation__(self):
           
        data = dict()
        
        image_path = self.paramentrosIN_carregados["imagem"]
        
        print("Obtendo informacao da imagem")
        
        print(image_path)
               
        info = subprocess.check_output(['gdalinfo', '-nogcp','-nomd', '-norat', '-noct', str(image_path)])
        
        print info
        # recupera numero de linhas e colunas
        
        index_init = info.index(self.caption_nx_ny_name)
        text_rest = info[index_init:]
        index_end = text_rest.index('\n') + index_init
        
        info_s = info[index_init + len(self.caption_nx_ny_name):index_end]
        info_s = info_s.replace('\r', '').split(', ')
        
        data['nx'] = info_s[0]
        data['ny'] = info_s[1]
        
        # recupera numero inicio do mapa xmax e ymax
        index_init = info.index(self.caption_xmin_ymin)
        text_rest = info[index_init:]
        index_end = text_rest.index('\n') + index_init
        
        info_s = info[index_init + len(self.caption_xmin_ymin):index_end]
        info_s = info_s.replace('\r', '').replace('(','').replace(')','').split(' ')
        
        for atr in info_s:
            if atr == '':
                info_s.remove(atr)
        
        data['xmin'] = info_s[0].replace(' ', '').replace(',', '')
        data['ymax'] = info_s[1].replace(' ', '').replace(',', '')
        
        # recupera numero inicio do mapa xmin e ymin
        index_init = info.index(self.caption_xmax_xmin)
        text_rest = info[index_init:]
        index_end = text_rest.index('\n') + index_init
        
        info_s = info[index_init + len(self.caption_xmax_xmin):index_end]
        info_s = info_s.replace('\r', '').replace('(','').replace(')','').split(' ')
        
        for atr in info_s:
            if atr == '':
                info_s.remove(atr)
        
        data['xmax'] = info_s[0].replace(' ', '').replace(',', '')
        data['ymin'] = info_s[1].replace(' ', '').replace(',', '')
       
        print("Informacoes da imagem lidas")
       
        return data 
    
    
    
    
#functionParam = Dados.TableData()
    
#functionParam["imagem"] = Dados.SimpleData(data="C:/imagemteste.tif", path="C:/imagemteste.tif")

#getImgInfo = GetImgInfo(functionParam)

#informacoes = getImgInfo.data

#for key in getImgInfo.descriptionOUT:
    #print (informacoes[key])

