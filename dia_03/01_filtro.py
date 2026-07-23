# %%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv', sep=';')
df


# %%

filtro = df["QtdePontos"] >= 50
df[filtro]
# %%

filtro = (df["QtdePontos"] >= 50) & (df['QtdePontos'] < 100)
filtro 

# %%
df[filtro]
# %%

filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)
df[filtro]


# %%
