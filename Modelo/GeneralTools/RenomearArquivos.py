'''
Created on 01/09/2015

@author: Rennan
'''

import os

os.chdir("D://1 - Mestrado (segundo semestre)//projetos///Estimativa de Semeadura e colheita//Imagens//Recortadas Talhoes de soja 11-12//IintervaloPersonalizado(35-60)//Flat//Soltas")

nomes_substituir = list()
for nome in os.listdir('.'):
    #novo_nome = nome.replace(".tif_EbM", "")
    #os.rename(nome, novo_nome)
    nomes_substituir.append(nome)

os.chdir("D://1 - Mestrado (segundo semestre)//projetos///Estimativa de Semeadura e colheita//Imagens//Recortadas Talhoes de soja 11-12//IintervaloPersonalizado(35-60)//Flat+Savitzky//soltas")

nomes_substituir.reverse()

for nome in os.listdir('.'):
    #print nome
    #print nomes_substituir.pop()
    os.rename(nome, nomes_substituir.pop())
    
print ('OK')