import pandas as pd

df = pd.read_csv("data/winemag-data_first150k.csv")
df.drop('Unnamed: 0', axis = 1, inplace = True)

df.head()