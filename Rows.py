import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding ="latin1")
#print(df)

df2 = pd.read_excel("SampleSuperstore.xlsx")
#print(df2)

df3 = pd.read_json("sample_Data.json")
#print(df3)

print("First 10 rows of df2")
print(df2.head(10))

print("last 10 rows of df2")
print(df2.tail(10))


print("First 5 rows shown by default of df2")
print(df2.head())

print("last 5 rows of df2")
print(df2.tail())