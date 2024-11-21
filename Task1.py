# Kural tabanlı sınıflandırma ile potansiyel müşteri getirisi hesaplama
# 1
import pandas as pd


# 1 Read and show data
pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)
df=pd.read_excel("miuul_gezinomi.xlsx")
print(df.head())
print(df.shape)
print(df.tail())
print(df.columns)

# 2 Unique city frequency  # value_counts
print(df["SaleCityName"].unique())
print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# 3
print(df["ConceptName"].nunique())

# 4
print(df["ConceptName"].value_counts())

# 5
print(df.groupby("SaleCityName")["Price"].sum())

# 6
print(df.groupby("ConceptName")["Price"].sum())

# 7
print(df.groupby("SaleCityName")["Price"].sum())

# 8
print(df.groupby("ConceptName")["Price"].mean())

# 9
print(df.groupby(["ConceptName","SaleCityName"])["Price"].mean())
