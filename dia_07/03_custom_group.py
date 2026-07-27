# %%

import pandas as pd
import numpy as np
df = pd.read_csv("../data/transacoes.csv", sep=';')
df
# %%


def diff_amp(x:pd.Series):

    amp, media = (x.max() - x.min()), x.mean()

    return np.sqrt(amp - media)**2 

def life_time(x:pd.Series):
    dt = pd.to_datetime(x)

    return (dt.max() - dt.min()).days

# %%

idades = pd.Series([23,12,3,21,3,12,321,3,23,1,413,13,13,12,3])
idades
# %%

diff_amp(idades)


# %%

df.groupby("IdCliente").agg({
    "IdTransacao": ["count"],
    "QtdePontos": ["sum","mean", diff_amp],
    "DtCriacao": [life_time]
})
# %%
