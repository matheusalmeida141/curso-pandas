# %%


import pandas as pd

# %%

def read_file(file_name:str):

    df = pd.read_csv(f"../data/ipea/{file_name}.csv", sep=';')
    df = df.rename(columns={"valor": file_name})
    df = df.set_index(["nome", "período"])
    df = df.drop(["cod"], axis= 1)
    return df
# %%

df = read_file("homicidios")

# %%

df_negros = read_file("homicidios-negros")
# %%


pd.concat([df, df_negros], axis= 1)


# %%

import os

file_names = os.listdir("../data/ipea")

dfs = []

for i in file_names:
    dfs.append(read_file(i.split('.')[0]))
# %%

dfs

# %%

pd.concat(dfs, axis=1).reset_index().sort_values(["período", "nome"])
# %%
