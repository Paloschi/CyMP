'''
Created on 19/01/2016

@author: Paloschi
'''
import sys
from numpy import double

minimo = 25;
maximo = 51;

vermelho_default = 255
verde_default = 255
azul_default = 0

vermelho = True
verde = False
azul = False

vermelho_crescente = False
verde_crescente = True
azul_crescente = True

delta = maximo - minimo

for x in range(minimo, maximo):
    
    color_value = int((double(x - minimo) / (maximo - minimo)) * 255)
    #sys.stdout.write("-") 
    sys.stdout.write(str(x) + " ") 
    if vermelho: sys.stdout.write(str(color_value if vermelho_crescente else 255 - color_value) + " ")
    else : sys.stdout.write(str(vermelho_default)+" ")
    if verde: sys.stdout.write(str(color_value if verde_crescente else 255 - color_value) + " ")
    else : sys.stdout.write(str(verde_default)+" ")
    if azul: sys.stdout.write(str(color_value if azul_crescente else 255 - color_value) + " ")
    else : sys.stdout.write(str(azul_default)+" ")
    print ""
    
    if x == 3000 : input('pausa pro cafe')
    