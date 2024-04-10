
#%%
from src import soporte as sp

# %%
df = sp.open_csv('files/finanzas-hotel-bookings.csv')
# %%
sp.explore_df(df)
#%%
df_sin_noche = df.loc[(df['stays_in_weekend_nights'] == 0) & (df['stays_in_week_nights'] == 0), :]
#%%
sp.explore_columns(df_sin_noche)

# %%
df_cancelados = df.loc[(df['is_canceled'] == True), 'company']

df_cancelados.head()

# %%
