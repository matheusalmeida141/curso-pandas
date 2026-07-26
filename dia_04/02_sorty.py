# %%
import pandas as pd


clientes= pd.read_csv("../data/clientes.csv", sep=';')
clientes.head()


# %%



clientes["qtdePontos"].sort_values()


# %%


max_pontos = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_pontos
clientes[filtro]

# %%

clientes.sort_values(by="qtdePontos", ascending=False).head(n=5)
# %%

clientes.sort_values(by=["qtdePontos", "DtCriacao"], ascending=[False,True])
# %%
