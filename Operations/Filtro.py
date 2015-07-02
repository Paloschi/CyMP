# -*- coding: utf-8 -*-
'''
Created on May 5, 2015

@author: Paloschi
'''
from beans import Dados
import gdal
from Operations import OperationInterface
from numpy.core.numeric import array
progress = gdal.TermProgress_nocb    

from multiprocessing import Pool
from multiprocessing import freeze_support



class Filtro(OperationInterface.Operation):
    '''
    classdocs
    '''
    
    def __setParamIN__(self):
        self.descriptionIN["images"] = "Série de imagens para aplicar o filtro"
        self.descriptionIN["window_size"] = "Série de imagens para aplicar o filtro"
        self.descriptionIN["order"] = "parametros de configuração filtro" # não implementado
        self.descriptionIN["null_value"] = "parametros de configuração filtro" # não implementado
     
    def __setParamOUT__(self):
        self.descriptionOUT["imagensFiltradas"] = "Série de imagens filtradas" 
    
    def __execOperation__(self):
        
        images_super = self.brutedata["images"]
        images = images_super.loadData()
        
        #freeze_support()
        
        metadata = images_super[0].data_metadata
        
        images = array(images).astype(dtype="int16")

        #print("Numero de bandas:" + str(len(images)))
        #print("Numero de linhas:" + str(len(images[0])))
        #print("Numero de colunas:" + str(len(images[0][0])))

        n_bandas = len(images)
        n_linhas = len(images[0])
        n_colunas = len(images[0][0])

        #quartil = int(n_linhas/6)
        quartil = int(n_linhas)

        #pool = Pool(processes=6)
        #pool = Pool(processes=1)
        
        parametro1 = dict()
        parametro1["images"] =  images[:, 0 : quartil]
        parametro1["window_size"] = self.paramentrosIN_carregados["window_size"]
        parametro1["order"] = self.paramentrosIN_carregados["order"]
        parametro1["null_value"] = self.paramentrosIN_carregados["null_value"]
 
        #parametro2 = dict()
        #parametro2["images"] = images[:, quartil : (2*quartil)]
        #parametro2["window_size"] = self.paramentrosIN_carregados["window_size"]
        #parametro2["order"] = self.paramentrosIN_carregados["order"]
        #parametro2["null_value"] = self.paramentrosIN_carregados["null_value"]
        
        #parametro3 = dict()
        #parametro3["images"] = images[: , 2*quartil : 3*quartil]
        #parametro3["window_size"] = self.paramentrosIN_carregados["window_size"]
        #parametro3["order"] = self.paramentrosIN_carregados["order"]
        #parametro3["null_value"] = self.paramentrosIN_carregados["null_value"]
        
        #parametro4 = dict()
        #parametro4["images"] = images[: , 3*quartil : 4*quartil]
        #parametro4["window_size"] = self.paramentrosIN_carregados["window_size"]
        #parametro4["order"] = self.paramentrosIN_carregados["order"]
        #parametro4["null_value"] = self.paramentrosIN_carregados["null_value"]
        
        #parametro5 = dict()
        #parametro5["images"] = images[: , 4*quartil : 5*quartil]
        #parametro5["window_size"] = self.paramentrosIN_carregados["window_size"]
        #parametro5["order"] = self.paramentrosIN_carregados["order"]
        #parametro5["null_value"] = self.paramentrosIN_carregados["null_value"]

        #parametro6 = dict()
        #parametro6["images"] = images[: , 5*quartil : n_linhas]    
        #parametro6["window_size"] = self.paramentrosIN_carregados["window_size"]
        #parametro6["order"] = self.paramentrosIN_carregados["order"]
        #parametro6["null_value"] = self.paramentrosIN_carregados["null_value"]
        
        #print("Toral de linhas a serem filtradas: " + str(n_linhas))
        #print("--------------")
        #print("Linhas do primeiro quartil: 0 - " + str(len(parametro1["images"][0])))
        #print("Linhas do segundo quartil: " + str(len(parametro1["images"][0])) + " - " + str(2*len(parametro1["images"][0])))
        #print("Linhas do terceiro quartil: " + str(2*len(parametro1["images"][0])) + " - "+ str(n_linhas))
        
        #results = pool.map(filtrar, (parametro1, parametro2, parametro3, parametro4, parametro5, parametro6))
        #results = pool.map(filtrar, (parametro1))
    
        results = self.filtrar(parametro1)
        
        #filtrar(parametro2)
        
        #print("juntando resultados")
        
        images = results#[0]
        #images.extend(results[1])
        #images.extend(results[2])
        #images.extend(results[3])
        #images.extend(results[4])
        #images.extend(results[5])
        
        #print("numero de linhas de saida: " + str(len(images)))
        
        results = [[[0 for x in range(n_colunas)] for x in range(n_linhas)] for x in range(n_bandas)] 
        results = array(results).astype(dtype="int16")
        
        
        #print ("ageitando linhas na matriz")
        progress( 0.0 )
    
        i_imagem =0
        i_linha = 0
        i_coluna = 0
        for linha in images:
            
            i_imagem=0      
            progress( (i_linha+1) / float(n_linhas))  
                  
            for pixel in linha:
                results[i_imagem][i_linha][i_coluna] = pixel
                i_imagem+=1
            i_coluna+=1
            
            if i_coluna>=n_colunas:
                i_coluna=0
                i_linha+=1
        
        saida = dict()
        
        saida["imagensFiltradas"]  = results
        
        saida["metaData"] = metadata
        
        return saida
    
    def filtrar(self, parametros):
        
        images = parametros["images"]
        window_size = parametros["window_size"]
        order = parametros["order"]
        null_value = parametros["null_value"]
        

        
        
        #if (images == None) : print ("Image None")
        
        #print (len(images)) 
         
        n_linhas = len(images[0])
        n_colunas = len(images[0][0])
        n_images = len(images)
    
        progress( 0.0)
        i_linhas = float(0) 
        
            
        linhas_filtradas = list()
            
        n_iteracoes= 0
    
        total = n_linhas
        if null_value!=None: nullValue = float(null_value) #-32768
        else : nullValue = None
        
        print("primeiro valor:" + str(images[0][0][0]))
        if nullValue == images[0][0][0] : print "são iguais"
    
        for i_linhas in range(0, n_linhas):   
            #print ("i_linhas" + str(i_linhas))
            n_iteracoes+=1 
            progress( n_iteracoes / float(total))  
            self.progresso = (n_iteracoes / float(total))*100
                
            #start_time = time.time()                                                                                                                                                                                                                                                                                                                                                                                                   
            for i_colunas in range(0, n_colunas):
                #print ("i_colunas" + str(i_colunas))
                
                line = list()
    
                #print(images[0][i_linhas][i_colunas])
                
                #nullValue = 0
                
                if images[0][i_linhas][i_colunas] == nullValue : 
                    line_filtred = array([0 for x in range(n_images)])       
                
                else :  
                    #print(i_colunas)
                    for img in images:
                        line.append(img[i_linhas][i_colunas])
                            
                    #plt.plot(line)
                    #line_filtred = array((Smooth(line, 1)))
                    
                    line_filtred = array((savitzky_golay(line, window_size, order)))
                    
                    #images[:, i_linhas, i_colunas] = bool(0)
                    
                line_filtred = line_filtred.astype(dtype="uint16")           
                linhas_filtradas.append(line_filtred)    
                #print ("foi 1")
                #plt.show()
                    
            #end_time = time.time()
            #estimed_time = ((end_time - start_time) * ((n_linhas) - n_iteracoes)) / 60 
            #print("tempo estimado (minutos): " + str(estimed_time))
            #print ("foi 1")
            
                    
        return linhas_filtradas
    
def Smooth( array, smooth_window):

        a = len(array)
        temp_intensity = array[:] #don't use the changed intensity values
        for i in range(a):
            if smooth_window<=i and i <= a-smooth_window-1:
                for j in range(i-smooth_window,i):
                    array[i]+= temp_intensity[j]
                for j in range(i+1, i+smooth_window+1):
                    array[i]+= temp_intensity[j]
                array[i] /= smooth_window*2 +1
            elif i < smooth_window:
                for j in range(i):
                    array[i] += temp_intensity[j]
                for j in range(i+1, 2*i+1):
                    array[i] += temp_intensity[j]
                array[i]/=(2*i+1)
            elif i >= a-smooth_window - 1:
                for j in range(i+1, a):
                    array[i] += temp_intensity[j]
                for j in range(2*i-a +1 , i):
                    array[i]+= temp_intensity[j]
                array[i] /=  (2*a -2*i-1)
            else: print "ERROR in Smooth: out of range"
        return array
        
def savitzky_golay(y, window_size, order, deriv=0, rate=1):
        r"""Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
        The Savitzky-Golay filter removes high frequency noise from data.
        It has the advantage of preserving the original shape and
        features of the signal better than other types of filtering
        approaches, such as moving averages techniques.
        Parameters
        ----------
        y : array_like, shape (N,)
            the values of the time history of the signal.
        window_size : int
            the length of the window. Must be an odd integer number.
        order : int
            the order of the polynomial used in the filtering.
            Must be less then `window_size` - 1.
        deriv: int
            the order of the derivative to compute (default = 0 means only smoothing)
        Returns
        -------
        ys : ndarray, shape (N)
            the smoothed signal (or it's n-th derivative).
        Notes
        -----
        The Savitzky-Golay is a type of low-pass filter, particularly
        suited for smoothing noisy data. The main idea behind this
        approach is to make for each point a least-square fit with a
        polynomial of high order over a odd-sized window centered at
        the point.
        Examples
        --------
        t = np.linspace(-4, 4, 500)
        y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
        ysg = savitzky_golay(y, window_size=31, order=4)
        import matplotlib.pyplot as plt
        plt.plot(t, y, label='Noisy signal')
        plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
        plt.plot(t, ysg, 'r', label='Filtered signal')
        plt.legend()
        plt.show()
        References
        ----------
        .. [1] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of
           Data by Simplified Least Squares Procedures. Analytical
           Chemistry, 1964, 36 (8), pp 1627-1639.
        .. [2] Numerical Recipes 3rd Edition: The Art of Scientific Computing
           W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery
           Cambridge University Press ISBN-13: 9780521880688
        """
        import numpy as np
        from math import factorial
        
        try:
            window_size = np.abs(np.int(window_size))
            order = np.abs(np.int(order))
        except ValueError, msg:
            raise ValueError("window_size and order have to be of type int")
        if window_size % 2 != 1 or window_size < 1:
            raise TypeError("window_size size must be a positive odd number")
        if window_size < order + 2:
            raise TypeError("window_size is too small for the polynomials order")
        order_range = range(order+1)
        half_window = (window_size -1) // 2
        # precompute coefficients
        b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
        m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
        # pad the signal at the extremes with
        # values taken from the signal itself
        firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
        lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
        y = np.concatenate((firstvals, y, lastvals))
        return np.convolve( m[::-1], y, mode='valid')

if __name__ == '__main__':
    
    freeze_support()
    filtro = Filtro()
    
    root_ = "C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\Modis\\2014\\EVI"
    root_saida = "C:\\Users\\Paloschi\\Desktop\\data\\AjusteModeloDSDC\\3.EVI_Flat_Propriedades_SavitsGolay\\"
    
    images = Dados.SerialData()
    
    parametros = Dados.TableData()
    
    images.loadListByRoot(root_, "tif")
    
    dataSet = Dados.TableData()
    dataSet["images"] = images

    filtro.data = dataSet
    
    imagens_filtradas = filtro.data
    
    images.data_metadata = imagens_filtradas["metaData"]
    
    print (images.data_metadata)
    
    images.saveListByRoot(imagens_filtradas["imagensFiltradas"], root_saida + "_FiltroSavitsGolay", "tif")
    
    #images.saveListLike1Image(imagens_filtradas["imagensFiltradas"], root_saida + "filtradas_cubo", "tif")
    
    #images.saveListLike1Image(images.loadData(), root_saida + "puras_cubo", "tif")


