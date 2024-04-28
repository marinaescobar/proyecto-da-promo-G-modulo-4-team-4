
#%%
from src import soporte as sp
import pandas as pd
import numpy as np
from src import database as db
from src import queries as query


# %%
df = sp.open_csv('files/finanzas-hotel-bookings.csv')
# %%
sp.explore_df(df)
# %%
#%%
sp.df_information(df)
#%%
sp.explore_columns(df)
#%%
df = sp.eliminacion_nulos(df)
#%%
df = sp.limpieza(df)
# %%
df = sp.imputacion_nulos(df)
# %%
df = sp.limpieza_fase2(df)
# %%
df.to_csv('files/data-hotel.csv')
# %%
df = sp.open_csv('files/data-hotel-clean.csv')

df.columns
# %%
db.creacion_tablas_esquema(query.creacion_esquema , 'AlumnaAdalab', 'NomeRiu_Hotels')

db.creacion_tablas_esquema(query.crear_tabla_hotel, 'AlumnaAdalab')

db.creacion_tablas_esquema(query.crear_tabla_meal, 'AlumnaAdalab')

db.creacion_tablas_esquema(query.crear_tabla_room, 'AlumnaAdalab')

db.creacion_tablas_esquema(query.crear_tabla_agent, 'AlumnaAdalab')

db.creacion_tablas_esquema(query.crear_tabla_booking, 'AlumnaAdalab')

db.creacion_tablas_esquema(query.crear_tabla_clients, 'AlumnaAdalab')

#%%
tuplas_hotel = [('City Hotel',), ('Resort Hotel',)]
tuplas_meal = [('BB',), ('FB',), ('HB',), ('SC',), ('Undefined',)]
tuplas_row = [('A',), ('B',), ('C',), ('D',), ('E',), ('F',), ('G',), ('H',), 
              ('I',), ('J',), ('K',), ('L',), ('M',), ('N',), ('O',), ('P',),
              ('Q',), ('R',), ('S',), ('T',), ('U',), ('V',), ('W',), ('X',),
              ('Y',), ('Z',), ('Undefined',)]
tuplas_agent = list(set([(element,) for element in df['agent']]))

df['hotel'] = df['hotel'].replace("City Hotel", 1)
df['hotel'] = df['hotel'].replace("Resort Hotel", 2)
df['hotel'] = df['hotel'].astype(int)

tuplas_booking = list(zip(df['hotel']))


#%%
db.insertar_datos(query.insertar_hotel, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_hotel)

#%%
db.insertar_datos(query.insertar_meal, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_meal)

#%%
db.insertar_datos(query.insertar_room, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_row)

# %%
db.insertar_datos(query.insertar_agent, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_agent)