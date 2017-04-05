'''
Created on 04/12/2015

@author: Paloschi
'''
from Modelo.beans.SerialFileData import SerialFile

nome_cubo = "Cubo_Ks_cascavel_soja_2011_12"

if __name__ == '__main__':
    
    imagens = SerialFile(root_path="C:\\CyMP\\Gafanhoto\\DADOS para Dr\\Imagens Cascavel\\Ks")
    imagens.saveListLike1Image(nome_cubo)
    