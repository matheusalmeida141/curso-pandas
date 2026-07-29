# %%

import pandas as pd

df = pd.read_csv("dados_cartao.csv")
df.head()


# %%

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df["vlParcela"] = df["vlVenda"]/df["qtParcela"]
df


# %%
df["ordemParcela"] = df.apply(lambda row: [i for i in range(row["qtParcela"])], axis=1)

df

# %%

df_explode = df.explode([ "ordemParcela"])

df_explode

# %%

df_explode["dtParcela"] = df_explode.apply(lambda row: row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])  , axis= 1)
# %%

df_explode.head()
# %%

df_explode.groupby(["idCliente", "dtParcela"])['vlParcela'].sum().reset_index()


# %%
