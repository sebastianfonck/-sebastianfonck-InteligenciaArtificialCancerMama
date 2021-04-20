import numpy as np
import pandas as pd

import tools

# Limpieza de los datos
# Selección de los datos
# Integración de los datos
# Construcción de nuevos datos
# Dar Formato a los datos

# == Preparacion abortos == 
abortos = tools.cargar_aborto_autorizado()
# Quitar filas con permiso: "To save the woman's life"
abortos = abortos[abortos['Subgroup'] != "To save the woman's life"]
# Elimnar columnas no necesarias
abortos = abortos[['Country or Area','Year', 'Value']]
# Agrupar registros para quitar repetidos
abortos = pd.groupby(abortos, by=['Country or Area','Year']).max()
# Eliminar filas que carecen de información: Todos los atributos tiene valor
#tools.mostrar_info(abortos, 'Aborto autorizado')


# == Preparacion PIB per capita ==
pib = tools.cargar_pib_percapita()
# Eliminar columnas no necesarias
pib = pib[['Country or Area', 'Year', 'Value']]
# Tomar solo el año 2007
pib = pib[pib['Year'] == 2007]
# Eliminar filas que carecen de información: Todos los atributos tienen valor
#tools.mostrar_info(pib, 'Pib per capita')

# == Preparación edad de maternidad ==
edad_madre = tools.cargar_edad_de_madres()
# Elimnar columnas no necesarias
edad_madre = edad_madre[['Country or Area', 'Year', 'Age of mother', 'Value']]
# Eliminar filas que generan ruido
edad_madre = edad_madre[edad_madre['Age of mother'] != 'Total']
edad_madre = edad_madre[edad_madre['Age of mother'].str.isnumeric() == True]
edad_madre = edad_madre[edad_madre['Year'] == 2007]
#tools.mostrar_info(edad_madre, 'Edad de madre primeriza')

# == Unir abortos y pib
unidos = pd.merge(abortos, pib, 
            left_on=['Country or Area', 'Year'], 
            right_on=['Country or Area', 'Year'], 
            how='right', 
            suffixes=('_aborto', '_pib'))
#tools.mostrar_info(unidos)

# == Unir (abortos y pib) y edad_madre
unidos = pd.merge(unidos, edad_madre, 
            left_on=['Country or Area', 'Year'], 
            right_on=['Country or Area', 'Year'], 
            how='inner', 
            suffixes=('_unidos', '_madre'))
tools.mostrar_info(unidos, 'Unidos todos')

# == Ajustes a los datos finales
# cambiar nombres a columnas
unidos.rename(columns={'Country or Area':'Country'}, inplace=True)
unidos.rename(columns={'Value_aborto':'Abortion'}, inplace=True)
unidos.rename(columns={'Value_pib':'Gdp'}, inplace=True)
unidos.rename(columns={'Age of mother':'Age'}, inplace=True)
unidos.rename(columns={'Value':'Children'}, inplace=True)

# Normalizar columna de Pib: (valor - min) / (max - min)
print(unidos['Gdp'].min(), unidos['Gdp'].max())
npib = lambda a: (a - 0) / (unidos['Gdp'].max() - 0)
unidos['Gdp'] = npib(unidos['Gdp'])

# == Separar la edad en columnas
#print(unidos['Age'].unique())
unidos['Age'] = unidos['Age'].astype(float)
Ages = [0,14,17,35,100]
Ages_n = [1,2,3,4]
# Convierte a categorias
unidos['Age'] = pd.cut(unidos['Age'], Ages, labels=Ages_n) 
#print(unidos['Age'].unique())
#print(unidos.head())

# Agrupar nacimientos por rango de edad
unidos = unidos.groupby(by=['Country','Year', 'Abortion','Gdp', 'Age'])['Children'].agg(
    {'Children': 'sum'}).reset_index()
# Genera columnas
unidos = pd.concat([unidos, pd.get_dummies(unidos['Age'], prefix='Age')], axis=1)
#tools.mostrar_info(unidos, 'Unidos todos')

# Normalizar columna de Children: (valor - min) / (max - min)
#print(unidos['Children'].min(), unidos['Children'].max())
nchildren = lambda a: (a - 0) / (unidos['Children'].max() - 0)
unidos['Children'] = nchildren(unidos['Children'])

# Separar países en columnas
#print(unidos['Country'].unique()) # Listado de países sin repeticiones
unidos = pd.concat([unidos, pd.get_dummies(unidos['Country'], prefix='Country')], axis=1)

# Borrar columnas no usadas
unidos.drop('Year', axis=1, inplace=True)
unidos.drop('Country', axis=1, inplace=True)
unidos.drop('Age', axis=1, inplace=True)

tools.mostrar_info(unidos, 'Unidos todos')

# Datset resultado
#np.savetxt("./unidos.csv", unidos,  delimiter=",", fmt="%s", )
unidos.to_csv(r"./unidos.csv", index = False)
