import pandas as pd 

data ={
    "Name": ['hanif','kashif','uzaifa'],
    "age": [ 12,35,6],
    "city": ['isb','swat', 'dir']
}

df = pd.DataFrame(data)
print(df)
# Save in csv format
#df.to_csv("output.csv", index = False)

# Save in excel format
#df.to_excel("output.xlsx", index = False)

# Save in json format
df.to_json("output.json", index = False)
