# %%

import pandas as pd

# %%


df = pd.DataFrame({
    "nome": ["matheus", "lucas", "ana", "lucas"],
    "idadae": [29, 28, 28, 28],
    "salario": [1600, 2200, 1600, 1600]



})

df

# %%

df.drop_duplicates()
# %%


df.drop_duplicates(keep="last")
# %%


df.drop_duplicates(subset=["idadae"])
# %%
