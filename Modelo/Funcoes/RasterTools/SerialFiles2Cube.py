'''
Created on 04/12/2015

@author: Paloschi
'''
from Modelo.beans.SerialFileData import SerialFile

nome_cubo = "Cubo_dr_soja_2011_12"

if __name__ == '__main__':
    
    imagens = SerialFile(root_path="C:\\Users\\Paloschi\\Desktop\\Tudo_Necessario\\4-Dr")
    imagens.saveListLike1Image(nome_cubo)
    