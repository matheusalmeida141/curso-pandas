# %%
import pandas as pd

df = pd.read_csv("../Exercicios/arquivo.csv")
df
# %%

df_stack = df.set_index(["nome", "período"]).stack().reset_index()

# %%
df_stack.head()
# %%

df_stack.columns = ["nome", "periodo", "metrica", "valor"]
df_stack
# %%

df_stack.pivot_table(values="valor",
                     index=["nome", "periodo"],
                     columns="metrica")
# %%


df_stack.pivot_table(values="valor",
                     index=["nome"],
                     columns="metrica",
                     aggfunc="mean")
# %%
