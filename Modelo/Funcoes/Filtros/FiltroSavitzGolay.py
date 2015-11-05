# -*- coding: utf-8 -*-
'''
Created on May 5, 2015

@author: Paloschi
'''

import gdal
from Modelo.Funcoes import AbstractFunction
from numpy.core.numeric import array
from numpy import double
progress = gdal.TermProgress_nocb    
import numpy as np
from Modelo.beans import SERIAL_FILE_DATA, TABLE_DATA, SerialFile, RasterFile
import sys
import threading


class FiltroSavitz(AbstractFunction):
    '''
    Essa classe representa um filtro que filtra uma serie de imagens com o SavitzGolay
    '''
    
    def __setParamIN__(self):
        
        #self.descriptionIN["nome_atributo"] = {"Required":True, "Type":FILE_DATA, "Description":"um arquivo qualquer requerido"}
        
        self.descriptionIN["images"] = {"Required":True, "Type":SERIAL_FILE_DATA, "Description":"Série de imagens para aplicar o filtro"}
        
        conf_algoritimo = dict()
        conf_algoritimo["window_size"] = {"Required":True, "Type":None, "Description":"Série de imagens para aplicar o filtro"}
        conf_algoritimo["order"] = {"Required":True, "Type":None, "Description":"parametros de configuração filtro"} # não implementado
        #conf_algoritimo["null_value"] = {"Required":True, "Type":None, "Description":"parametros de configuração filtro"} # não implementado
        
        self.descriptionIN["conf_algoritimo "] = {"Required":False, "Type":TABLE_DATA, "Table_Description":conf_algoritimo,"Description":"tabela de parametros para configuração do filtro"}
   
     
    def __setParamOUT__(self):
        self.descriptionOUT["images"] = "Série de imagens filtradas" 
    
    def __execOperation__(self):
        
        images = self.paramentrosIN_carregados["images"]
        if self.paramentrosIN_carregados.has_key("conf_algoritimo") : conf_algoritimo = self.paramentrosIN_carregados["conf_algoritimo"]
        else : conf_algoritimo = dict()
        img_matrix = images.loadListRasterData()
        
        if img_matrix == None:
            print self.console("Erro no carregamento das imagens")
            threading.currentThread().stop() 
            return
        
        self.imagem_0 = img_matrix[0] # imagem de referencia pra leitura de valores null
        conf_algoritimo["NoData"] = self.imagem_0[0][0]
        #conf_algoritimo["NoData"] = double(images[0].getRasterInformation()["NoData"])

        self.n_bandas = len(img_matrix)
        self.n_linhas = len(img_matrix[0])
        self.n_colunas = len(img_matrix[0][0])
        
        sys.stdout.write("Numero de bandas: " + str(self.n_bandas))
        sys.stdout.write(" Numero de linhas: " + str(self.n_linhas))
        print(" Numero de colunas: " + str(self.n_colunas))
        
        
    
        linhas_filtradas = self.filtrar(img_matrix, conf_algoritimo)
        if threading.currentThread().stopped()  : return 
        results = linhas_filtradas
        
        #results = np.zeros((self.n_bandas, self.n_linhas, self.n_colunas,))
        #results = array(results).astype(dtype="int16")

        #i_imagem = 0
        #i_linha = 0
        #i_coluna = 0
        
        #sys.stdout.write( "Criando nova série de imagens com valores filtrados: ")
        #progress( 0.0 )
        
        #print ("numero de colunas", self.n_colunas)

        #for linha in linhas_filtradas:
            
            #i_imagem=0      
            #progress( (i_linha+1) / float(self.n_linhas))  
              
            #while self.imagem_0[i_linha][i_coluna] == conf_algoritimo["NoData"]:
                #i_coluna+=1
                #if i_coluna>=self.n_colunas:
                    #i_coluna=0
                    #i_linha+=1
                    
            #for pixel in linha:
                #results[i_imagem][i_linha][i_coluna] = pixel
                #i_imagem+=1
            #i_coluna+=1
 
            #if i_coluna>=self.n_colunas:
                    #i_coluna=0
                    #i_linha+=1   
        
        imgs_saida = SerialFile()
        imgs_saida.metadata = images.metadata
        i_imagem = 0
        for img in self.paramentrosIN_carregados["images"]:
            img.data = results[i_imagem]
            i_imagem+=1
            imgs_saida.append(img)
        
        #saida = TableData()
        #saida["images"] = img_saida
        
        return imgs_saida
    
    def filtrar(self, images, lol, **config):
        
        if config.get("window_size") == None : window_size=5
        else : window_size = config.get("window_size")
        if config.get("order") == None : order=3
        else : order = config.get("order")
        if config.get("NoData") == None : noData=0
        else : noData = config.get("NoData")
                
        print ("valor do primeiro pixel", images[0][0][0])
        sys.stdout.write( "Filtrando imagens: ")
        
        linhas_filtradas = list()   
        n_iteracoes = 0
        total = self.n_linhas
        progress( 0.0)

        results = np.zeros((self.n_bandas, self.n_linhas, self.n_colunas,))

        for i_linhas in range(0, self.n_linhas):   
            n_iteracoes+=1 
            
            progresso = n_iteracoes/float(total)
            progress(progresso)
            self.progresso  = progresso*100
            
            if threading.currentThread().stopped()  : return 
                                                                                                                                                                                                                                                                                                                                                                                                   
            for i_colunas in range(0, self.n_colunas):
                line = list()
                if self.imagem_0[i_linhas][i_colunas] != noData :
                    for img in images:
                        line.append(img[i_linhas][i_colunas])
                    line_filtred = array((savitzky_golay(line, window_size, order)))
                    
                    for i_images in range(self.n_bandas):
                        results[i_images][i_linhas][i_colunas] = line_filtred[i_images]             
                    
                    #linhas_filtradas.append(line_filtred)
                    
        return results
    
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
        
def savitzky_golay(y, window_size=5, order=3, deriv=0, rate=1):
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


#vector = array([2402,2307,2093,1948,1865,1773,1937,2224,2837,3954,4605,7191,7744,7967,8188,8202,7708,7608,6360,5365,3173,2722,2621,2552,2659,3860,4609,5288,5749,5508,5649,2629])
#print savitzky_golay(y = vector, window_size=)


