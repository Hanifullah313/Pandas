import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding ="latin1")
#print(df)

df2 = pd.read_excel("SampleSuperstore.xlsx")
#print(df2)

df3 = pd.read_json("sample_Data.json")
print(df3)