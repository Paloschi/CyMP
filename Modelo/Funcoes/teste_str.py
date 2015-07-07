'''
Created on Mar 3, 2015

@author: Paloschi
'''

package = 'PyQt4.uic'
archive = 'pyuic'
import fiona


shape_path = "C:/Users/Paloschi/Desktop/workspace/eclipse/Gafanhoto_1.0/data/ecmwf/2010/ECMWF_PR_2010.shp"
image_reference_path = "C:/Users/Paloschi/Desktop/workspace/eclipse/Gafanhoto_1.0/data/Modis/MOD13Q1.20150117.250m_16_dias_EVI_PR.tif"
    

with fiona.open(shape_path, 'r') as shape:
        print(len(shape))