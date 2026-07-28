# %%

import pandas as pd



# %%

clientes = pd.read_csv("../data/clientes.csv", sep=';')
transacao = pd.read_csv("../data/transacoes.csv", sep=';')

transacao.head()
# %%

transacao.merge(right=clientes, 
                how="left", 
                left_on = "IdCliente", 
                right_on = "idCliente",
                suffixes = ["Transacoes", "Clientes"]
                )
# %%
