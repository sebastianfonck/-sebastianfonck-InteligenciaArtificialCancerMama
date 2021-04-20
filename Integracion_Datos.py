import pandas as pd
import numpy as np

import CargaDatos

dataM3=CargaDatos.Carga_Manizales_2003()

dataP3=CargaDatos.Carga_pasto_2003()

filas="{0[0]} " .format(dataM3.shape)
#print(filas)


for i in range(3):
    numbers = []
    numbers.append(i)


for x in range(len(numbers)):
    print (numbers[x])