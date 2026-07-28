# %% 
import pandas as pd



# %%
df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
})

df_02 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["kozato", "laura", "dan",],
    "idade":[32,29,31],
})
# %%

pd.concat([df, df_02], ignore_index=True)
# %%

df_03 = pd.DataFrame({
    "idades": [ 21, 23, 12, 43,]
})


# %%
pd.concat([df, df_03], axis = 1)

# %%

df_03 = df_03.sort_values("idades")


# %%


pd.concat([df, df_03], axis=1)


# %%

df_03 = df_03.reset_index(drop=True)

# %%


pd.concat([df, df_03], axis=1)

# %%
