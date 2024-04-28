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
# %%
db.creacion_tablas_esquema(query.creacion_esquema , 'AlumnaAdalab', 'NomeRiu_Hotels')
#%%
db.creacion_tablas_esquema(query.crear_tabla_hotel, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_meal, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_room, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_agent, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_booking, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_clients, 'AlumnaAdalab')

#%%
tuplas_hotel = [('City Hotel',), ('Resort Hotel',)]

tuplas_meal = [('BB',), ('FB',), ('HB',), ('SC',), ('Undefined',)]

tuplas_room = [('A',), ('B',), ('C',), ('D',), ('E',), ('F',), ('G',), ('H',), 
              ('I',), ('J',), ('K',), ('L',), ('M',), ('N',), ('O',), ('P',),
              ('Q',), ('R',), ('S',), ('T',), ('U',), ('V',), ('W',), ('X',),
              ('Y',), ('Z',), ('Undefined',)]

tuplas_agent = list(set([(element,) for element in df['agent']]))

df['hotel'] = df['hotel'].replace("City Hotel", 1)
df['hotel'] = df['hotel'].replace("Resort Hotel", 2)
df['hotel'] = df['hotel'].astype(int)

tuplas_booking = list(zip(df['hotel'], df['agent'], df['adr'], df['lead_time'], df['arrival_date'], df['stays_in_weekend_nights'], df['stays_in_week_nights'], df['adults'], df['children'], df['babies'], df['reserved_room_type'], df['assigned_room_type'], df['meal'], df['required_car_parking_spaces'], df['total_of_special_requests'], df['booking_changes'], df['days_in_waiting_list'], df['reservation_status_date'], df['reservation_status'], df['courtesy'], df['is_canceled']))
tuplas_client = list(zip(df['country'], df['market_segment'], df['distribution_channel'], df['customer_type'], df['is_repeated_guest'], df['previous_bookings_not_canceled'], df['previous_cancellations']))
#%%
tuplas_booking1 = tuplas_booking[0:29360]
tuplas_booking2 = tuplas_booking[29361:58721]
tuplas_booking3 = tuplas_booking[58722:88081]
tuplas_booking4 = tuplas_booking[88082:117443]
#%%
tuplas_client1 = tuplas_client[0:29360]
tuplas_client2 = tuplas_client[29361:58721]
tuplas_client3 = tuplas_client[58722:88081]
tuplas_client4 = tuplas_client[88082:117443]
#%%
db.insertar_datos(query.insertar_hotel, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_hotel)
#%%
db.insertar_datos(query.insertar_meal, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_meal)
#%%
db.insertar_datos(query.insertar_room, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_room)
# %%
db.insertar_datos(query.insertar_agent, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_agent)
# %%
db.insertar_datos(query.insertar_booking, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_booking1)
#%%
db.insertar_datos(query.insertar_booking, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_booking2)
#%%
db.insertar_datos(query.insertar_booking, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_booking3)
#%%
db.insertar_datos(query.insertar_booking, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_booking4)
# %%
db.insertar_datos(query.insertar_client, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_client1)
# %%
db.insertar_datos(query.insertar_client, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_client2)
# %%
db.insertar_datos(query.insertar_client, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_client3)
# %%
db.insertar_datos(query.insertar_client, 'AlumnaAdalab', 'NomeRiu_Hotels', tuplas_client4)
