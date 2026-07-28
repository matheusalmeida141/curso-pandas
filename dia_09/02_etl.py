# %%

import pandas as pd
import sqlalchemy


with open("etl.sql") as open_file:
    query = open_file.read()


print(query)
# %%


engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

df = pd.read_sql_query(query, con=engine)

df.head()

df.columns
# %%

from sklearn import cluster

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[['totalRevenue', 'qtdSalles']])
# %%
df["cluster"] = kmean.labels_
df


# %%

df.to_sql("cluster",con=engine, index=False, if_exists="replace")
# %%
