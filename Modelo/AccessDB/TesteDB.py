'''
Created on 5 de abr de 2017

@author: Rennan
'''

import psycopg2
import subprocess
import os

input_path = "C:\\CyMP\\Gafanhoto\\DADOS\\Imagens Cascavel\\Modis\\*.tif"
        
os.environ['PATH'] = r';C:\Program Files\PostgreSQL\9.6\bin'
os.environ['PGHOST'] = 'localhost'
os.environ['PGPORT'] = '5432'
os.environ['PGUSER'] = 'postgres'
os.environ['PGPASSWORD'] = '9mkjdpxg'
os.environ['PGDATABASE'] = 'TestePostGis'
        
#rastername = str(name)
#rasterlayer = rastername.lower()
        
conn = psycopg2.connect(database="TestePostGis", user="postgres", host="localhost", password ="9mkjdpxg")
cur = conn.cursor()


query= "SELECT rast from map LIMIT 3"

cur.execute(query)

cursor = cur.fetchall()
print(str(cursor))

#for row in cursor:
#    print(row)
#cmds = 'raster2pgsql -a -s 4326 -I -M -F -t 500x500 "' + input_path + '" public.map | psql'
        
#subprocess.call(cmds, shell=True)