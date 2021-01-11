
if __name__ == '__main__':
    from datetime import timedelta
    from datetime import date
    import datetime

    date1 = date(2007, 1, 1)
    date2 = date(2007, 3, 27)

    date = timedelta((date2 - date1).days * 1.03)
    
    print (date)


from Modelo.Funcoes.BalancoHidrico.Etc import Etc
from Modelo.Funcoes.BalancoHidrico.ExtratorSemeaduraColheita import ExtratorSemeaduraColheita
from Modelo.Funcoes.BalancoHidrico.Distribuidor_IC import DistribuidorKC


