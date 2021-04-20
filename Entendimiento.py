import numpy as np 
import pandas as pd 
import CargaDatos

#dataM3=CargaDatos.Carga_Manizales_2003()
#CargaDatos.mostrar_informacion_datos(dataM3)

todos=CargaDatos.Cargar_todos_los_Datos()

for key in todos:
    print('')
    print('******', key,'*****')
    CargaDatos.mostrar_informacion_datos(todos[key])