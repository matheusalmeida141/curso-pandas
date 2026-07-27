# %%

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv", sep=';')
df
# %%


df = df.dropna()
# %%


df.dropna(how="all")


# %%

brinquedo = pd.DataFrame({
    "nome": ['teo', 'matheus', 'lucas', 'alberto'],
    "idade": [36, 23 ,None ,20],
    "salario": [1234, None, 4882, 3256]
})

brinquedo
# %%

brinquedo.dropna(how="all", subset=['salario'])



# %%

brinquedo["idade"].fillna(0)


# %%

brinquedo.fillna({"idade":0, "salario": 1600})
# %%
