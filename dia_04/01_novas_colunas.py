# %%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=';')
df.head()


# %%

df["pontos_100"] = df["qtdePontos"] + 100

df.head()


# %%

df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()


# %%
df["emailTwitch"] = df["flEmail"] * df["flTwitch"]
df.head()
# %%
df["qtSocial"] = df["flEmail"] + df['flTwitch'] + df["flBlueSky"] + df["flInstagram"]

df.head()
# %%

df["todas_social"] = df["flEmail"] * df['flTwitch'] * df["flBlueSky"] * df["flInstagram"]
df.head()

# %%

df["logPontos"] = np.log( df['qtdePontos'] + 1)
df.head()
# %%

df["logPontos"].describe()

# %%

import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()


# %%
