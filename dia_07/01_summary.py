# %%

import pandas as pd
import random

idade = random.choices(range(10 , 81), k= 20 )

idade = pd.Series(idade)
idade

idade.sum()

idade.mean()
idade.max()
idade.min()
idade.describe()

# %%

df = pd.read_csv("../data/clientes.csv", sep=';')
df.head()


# %%

df.dtypes


# %%

filtro = df.dtypes == "object"

filtro = df.dtypes[~filtro].index.to_list()

df[filtro]

# %%

df[filtro].mean()

# %%

df[filtro].describe()

