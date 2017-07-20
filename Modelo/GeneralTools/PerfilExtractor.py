# -*- coding: utf-8 -*-
'''
Created on Jun 1, 2017

@author: Rennan Andres Paloschi
'''

import matplotlib.pyplot as plt
from Modelo.beans.SerialFileData import SerialTemporalFiles
import numpy

#-53.330847  -25.060710

#x = -53.537335
#y = -24.641008

x = -53.330847
y = -25.060710

variable1 = SerialTemporalFiles()
variable1.setValues("C:/CyMP/Gafanhoto/Dados/2-Balanco Hidrico/4-Dr", "%Y-%m-%d", "Dr_")
values_time_1 = variable1.getTimeVariableVector(x, y)

variable2 = SerialTemporalFiles()
variable2.setValues("C:/CyMP/Gafanhoto/Dados/2-Balanco Hidrico/5-Ks", "%Y-%m-%d", "Ks_")
values_time_2 = variable2.getTimeVariableVector(x, y)

plt.plot(values_time_1["times"], numpy.array(values_time_1["values"]))
plt.plot(values_time_2["times"], numpy.array(values_time_2["values"]))
plt.legend(["variavel 1", "variavel 2"])
plt.show()

