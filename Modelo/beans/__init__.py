# -*- coding: utf-8 -*-

from AbstractData import FILE_DATA, FUNCTION_DATA, SERIAL_FILE_DATA, TABLE_DATA, ABData

from FileData import FileData
from RasterData import RasterFile
from SerialFileData import SerialFile, SerialTemporalFiles
from TableData import TableData 




if __name__ == "__main__":
    
    imagem_teste = RasterFile(file_full_path="C:\\Users\\rennan.paloschi\\Desktop\\testeLTZ.tif")
    print imagem_teste.getRasterInformation()