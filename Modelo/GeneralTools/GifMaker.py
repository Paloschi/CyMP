'''
Created on 01/10/2015

@author: Rennan
'''

__author__ = 'Robert'
import sys
sys.path.append('/Library/Python/2.7/site-packages')
from images2gif import writeGif
from PIL import Image
import os, cStringIO

os.chdir("C:\\Gafanhoto WorkSpace\\Soja11_12\\Kc_distribuido\\soltas")

file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.gif')))
#['animationframa.png', 'animationframb.png', ...] "

images = [Image.open(fn) for fn in file_names]

size = (150,150)
for im in images:
    im.thumbnail(size, Image.ANTIALIAS)


filename = "C:\\Gafanhoto WorkSpace\\Soja11_12\\Kc_distribuido\\kc_distribuido.gif"
writeGif(filename, images, duration=0.1)



