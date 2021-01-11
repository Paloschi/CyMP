# -*- coding: utf-8 -*-


from Modelo.beans.AbstractData import FILE_DATA, FUNCTION_DATA, SERIAL_FILE_DATA, TABLE_DATA, ABData
from Modelo.beans.FileData import FileData
from Modelo.beans.RasterData import RasterFile
from Modelo.beans.SerialFileData import SerialFile, SerialTemporalFiles
from Modelo.beans.TableData import TableData
from Modelo.beans.VectorData import VectorFile




if __name__ == "__main__":
    
    imagem_teste = RasterFile(file_full_path="C:\\Users\\rennan.paloschi\\Desktop\\testeLTZ.tif")
    print (imagem_teste.getRasterInformation())