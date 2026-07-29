# %%

import pandas as pd

df = pd.read_csv("../Exercicios/arquivo.csv", sep=',')

df
# %%

df = df.set_index(["nome", "período"])
df.head()
# %%


df_stack = df.stack()

# %%


df_stack = df_stack.reset_index()


# %%

df_stack.rename(columns={"nome":"uf", "level_2":"nome", 0:"valor"}, inplace = True)



# %%
df_stack


# %%

df_stack = (df_stack.set_index(["uf", "período", "nome"])
    .unstack()
    .reset_index()
)

# %%

df_stack.columns

# %%

df_stack.head()
# %%

metricas = df_stack.columns.droplevel(0).to_list()[2:]

# %%

df_stack.columns = ["uf", "periodo"] + metricas

df_stack
# %%
