# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%

df.shape

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%

df.rename( columns = {"QtdePontos": "qtPontos", "DescSistemaOrigem": "SistemaOrigem"}, inplace= True )

# %%

df.dtypes
# %%

df[["IdCliente", "qtPontos"]]

# %%

df[["IdCliente", "IdTransacao" ,"qtPontos"]]

# %%
colunas = df.columns.tolist()
colunas.sort()
colunas

df = df[colunas]
df
# %%
