# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=';')

df
# %%


df.groupby("IdCliente").count()

# %%

df.groupby("IdCliente")["IdTransacao"].count()


# %%

df.groupby("IdCliente", as_index=False)[["IdTransacao"]].count()



# %%


summary = df.groupby("IdCliente", as_index=False).agg({

    "IdTransacao" : ["count"],
    "QtdePontos" : ["sum", "mean"]

})

summary
# %%

summary.columns
# %%

summary.columns = ["idCliente", "contagem", "qtdPontos", "mediaPontos"]
# %%
