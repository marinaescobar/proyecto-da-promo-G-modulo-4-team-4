
#%%
from src import soporte as sp
import pandas as pd
import numpy as np

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
