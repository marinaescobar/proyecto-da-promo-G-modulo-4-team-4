
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
df = sp.transformacion(df)
# %%
