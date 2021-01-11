# -*- coding: utf-8 -*-

from Modelo.Funcoes.AbstractFunction import Function as AbstractFunction


if __name__ == "__main__":
    
    from Modelo import beans
    from Modelo.Funcoes.Filtros import FiltroSavitz
    
    import warnings
    warnings.filterwarnings('ignore')

    
    root_path="C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\entrada_pesada"
    root_out="C:\\Users\\Paloschi\\Desktop\\data\\Rasters\\TesteFiltro\\saida"
    
    images_in = beans.SerialFile(root_path=root_path)
    
    filtro = FiltroSavitz()
    paramIn = dict()
    
    paramIn["images"] = images_in
    
    filtro.data = paramIn
    
    images_filtred = filtro.data["images"]
    
    images_filtred.root_path = root_out
    
    images_filtred.saveListLike1Image(name="teste_pesado", images_bands_matrix=images_filtred.data, ext="tif")
    






