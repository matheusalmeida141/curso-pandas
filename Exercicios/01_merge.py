
# 06.04 - Quem teve mais transações de Streak?


# %%

import pandas as pd


transacoes = pd.read_csv("../data/transacoes.csv", sep=';')
transacoes

# %%

transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=';')
transacao_produto.head()

produtos = pd.read_csv("../data/produtos.csv", sep=';')
produtos.head()
# %%


df_join = transacoes.merge(transacao_produto, how="left", on=["IdTransacao"]).merge(produtos, how="inner", on=["IdProduto"])
# %%

df_join.groupby("DescNomeProduto").count()[:-20]
# %%

df_join.head()
# %%

filtro = df_join["DescNomeProduto"] == "Presença Streak"

df_join[ filtro ].groupby("IdCliente").agg({"IdTransacao": "count"}).sort_values(by="IdTransacao", ascending=False)
#%%



