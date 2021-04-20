import numpy as np 
import pandas as pd 


def Carga_pasto_2003():
    """
        Carga de los datos del dataset de pasto del 2003 cancer de mama 
    """
    return pd.read_csv("c:/Users/sebastian/Desktop/2021/Electiva Datos/Proyecto de la materia/Datos/pasto 2003.csv", sep=';', index_col=0)

def Cargar_todos_los_Datos():
    """
        Cargar todos los dataset Disponibles
    """
    ds ={
        'Manizales 2003':Carga_Manizales_2003(),
        'Pasto 2003':Carga_pasto_2003()
    }

    return ds

def mostrar_informacion_datos(df): 
    """
        Se muestra la informacion de los Dataset
    """
    #print(df.info())
    #print(df.head())
    print(pd.isnull(df).sum)