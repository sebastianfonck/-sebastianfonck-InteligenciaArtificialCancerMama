import pandas as pd

clientes = {'first_name' : ['Oralie' ,'Imojean' ,'Michele', 'Ailbert', 'Stevy'],
           'last_name' : ['Fidgeon' ,'Benet' ,'Woodlands', 'Risdale', 'MacGorman'],
           'age' : [30 ,21 ,29 ,22, 24]}
clientes = pd.DataFrame(clientes, columns = ['first_name', 'last_name', 'age'])
#print(clientes)

# Concatenar datos de dos fuentes similares
nuevos_clientes = pd.DataFrame({'first_name' : ['Rebe',],
                            'last_name' : ['MacCrossan',],
                            'age' : [21,]},
                           columns = ['first_name', 'last_name', 'age'])
clientes = pd.concat([clientes, nuevos_clientes])
#print(clientes)

# Concatenar columna para poner ids
clientes.index = range(clientes.shape[0])
ids = pd.DataFrame({'client_id': [1, 2, 3, 4, 5, 6]}, columns = ['client_id'])
clientes = pd.concat([ids, clientes], axis=1,)
#print(clientes)

# Unir dos fuentes distintas con alguna relación
facturas = {'invoice_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'client_id' : [3, 2, 7, 2, 7, 3, 1, 4 ,2, 3, 6, 2],
            'amount': [77.91, 24.36, 74.65, 19.75, 27.46, 17.13, 45.77, 81.7, 14.41, 52.69, 32.03, 12.78]}
facturas = pd.DataFrame(facturas, columns = ['invoice_id', 'client_id', 'amount'])
#print(facturas)

unidos = pd.merge(clientes, facturas, 
            left_on='client_id', 
            right_on='client_id', 
            how='outer')
print(unidos)

# Si hubieran columnas con nombre igual se pude poner un sufijo
#clientes2 = pd.merge(clientes, clientes, on='client_id', suffixes=('_1', '_2'))
#print(clientes2)
