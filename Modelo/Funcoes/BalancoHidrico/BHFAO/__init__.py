
from numpy import ma
import numpy

if __name__ == '__main__':
    matriz = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    matriz = numpy.array(matriz)
    matriz[0] = ma.masked
    
    print matriz
    
    matriz += 8
    
    print matriz