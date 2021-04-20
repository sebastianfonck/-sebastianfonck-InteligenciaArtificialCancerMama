import numpy as np
import pandas as pd

def cargar_aborto_autorizado():
    """
        Permite cargar el dataset: Abortion laws by grounds on which abortion is permitted
    """
    return pd.read_csv("dataset/Abortion laws by grounds on which abortion is permitted/UNdata_Export_20210317_142012473.csv")

def cargar_pib_percapita():
    """
        Permite cargar el dataset: GDP per capita
    """
    return pd.read_csv("dataset/GDP per capita/UNdata_Export_20210317_140314267.csv")

def cargar_edad_de_madres():
    """
        Permite cargar el dataset: Live births by age of mother and sex of child
    """
    return pd.read_csv("dataset/Live births by age of mother and sex of child/UNdata_Export_20210317_135516577.csv")

def cargar_hijos_por_madres():
    """
        Permite cargar el dataset: Live births per woman
    """
    return pd.read_csv("dataset/Live births per woman/UNdata_Export_20210317_142531176.csv")

def cargar_desnutricion():
    """
        Permite cargar el dataset: Prevalence of undernourishment
    """
    return pd.read_csv("dataset/Prevalence of undernourishment/UNdata_Export_20210317_141123294.csv")

def cargar_todos_los_datasets():
    """
        Carga todos los datasets disponibles
    """
    
    ds = {
            'aborto_autorizado' : cargar_aborto_autorizado(),
            'pib_percapita' : cargar_pib_percapita(),
            'edad_de_madres' : cargar_edad_de_madres(),
            'hijos_por_madres' : cargar_hijos_por_madres(),
            'desnutricion' : cargar_desnutricion(),
        }
    return ds

def mostrar_info(df, nombre=''):
    """
        Muestra información de dataframe
    """
    print('')
    print('=================', nombre, '=================')
    print(' > Info:')
    print(df.info())
    print(' > Head:')
    print(df.head())
    print(' > Nulls:')
    print(pd.isnull(df).sum())
    print('=================', 'Fin', nombre, '=================')
    print('')
