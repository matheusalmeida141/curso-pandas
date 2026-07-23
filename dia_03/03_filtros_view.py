# %%

import pandas as pd


clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %%

filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro].copy()
clientes_0

# %%
clientes_0["Floag_1"] = 1
clientes_0
# %%
