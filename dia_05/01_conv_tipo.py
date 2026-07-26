# %%

import pandas as pd



# %%

df = pd.read_csv("../data/clientes.csv", sep=';')
df



# %%


df["qtdePontos"].astype(float)
# %%


pd.to_datetime(df["DtCriacao"])


# %%

df["DtCriacao"].replace({"0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"}, inplace=True)
# %%


df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])



# %%
df["DtCriacao"].dt.year
# %%
