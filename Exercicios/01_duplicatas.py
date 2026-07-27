# Selecione a primeira transação diária de cada cliente.

# %%

import pandas as pd


# %%


df = pd.read_csv("../data/transacoes.csv", sep=";")

df

# %%

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])


df["DtCriacao"] = df["DtCriacao"].dt.date

df


# %%


df.sort_values("DtCriacao").drop_duplicates(subset=["IdCliente", "DtCriacao"]).sort_values("IdCliente")

# %%
