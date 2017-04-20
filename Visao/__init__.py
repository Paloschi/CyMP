'''
 Converter .ui papra .py 
 pyuic4 fileIn.ui -o fileOut.py
'''

def main():
    import matplotlib.pyplot as plt
    import numpy
    import pylab as pl
    import imageio 
    from Modelo.beans.RasterData import RasterFile
    from Modelo.beans.SerialFileData import SerialFile
    
    arquivo_path = "D:\\Projeto_Floresta_Seca_2016\\1_Dataset\\2_TRMM\\TRMM_Fabien\\TRMMcrop\\"

    raster_file = SerialFile()
    raster_file.file_full_path = arquivo_path
    images_Files = raster_file.loadListByRoot(arquivo_path)
    raster_info = raster_file[1].getRasterInformation()
    xmax = float(raster_info["xmax"])
    xmin = float(raster_info["xmin"])
    ymax = float(raster_info["ymax"])
    ymin = float(raster_info["ymin"])
    
    images = []
    
    for raster_file in images_Files:
        imarray = numpy.asanyarray(raster_file.loadRasterData())
        img_plot = plt.imshow(imarray, extent=[xmin,xmax,ymin,ymax], cmap="hot")
        images.append(img_plot)
      
    #plt.plot([0,1], [0,1], 'o', c='green', ms=20)
    
    imageio.mimsave('C:\\Users\\PGSERE16\\Desktop\\movie.gif', images)
    
    #plt.axis('equal')
    #plt.legend()
    #plt.show()
    
    
    return

if __name__ == '__main__':
    main()
    
    
    
    



