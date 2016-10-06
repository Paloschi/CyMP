'''
Created on 19/09/2016

@author: Paloschi
'''
import os

arquivo_saida = open('All source Code.txt', 'w')

for root, directories, filenames in os.walk("C://Users//Paloschi//Desktop//teste_print//"):
    #for directory in directories:
        #print os.path.join(root, directory) 
    for filename in filenames: 
        if (str.split(filename, ".")[1] == "py") :
            #print os.path.join(root,filename) 
            
            f = open(os.path.join(root,filename), 'r')
            arquivo_saida.write("\n\n------------------  ")
            arquivo_saida.write(filename)
            arquivo_saida.write("  ------------------\n")
            arquivo_saida.write(f.read())
            
arquivo_saida.close()
        