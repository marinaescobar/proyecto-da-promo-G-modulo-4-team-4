
#%%
from src import soporte as sp
import pandas as pd

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
# %%
df.head(5)

df["arrival_date_day_of_month"].isnull().sum()
#%%
df["arrival_date_day_of_month"].unique()
#%%
Nulos = (df.isnull().sum()/df.shape[0])*100
# %%
Nulos
#%%
df_month = df[(df["arrival_date_week_number"].notnull()) & (df["arrival_date_month"].isnull())  ]
# %%
df_month["arrival_date_week_number"].unique()

# %%
