# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

series_idade = pd.Series(idades)
series_idade
# %%
idades[0]
# %%
idades[-1]
# %%


series_idade[0]


# %%
series_idade[-1]
# %%

series_idade.iloc[0]

# %%

series_idade.iloc[-1]


# %%

series_idade.iloc[:3]
# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32,
]

indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idade = pd.Series(idades, index=indexs)
series_idade

# %%

series_idade['Ana']


# %%
