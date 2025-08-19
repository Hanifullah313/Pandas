import pandas as pd 
"""
info method is used for :
 1: Displaying a summary of the DataFrame's columns, non-null values, and data types.
 2: Providing insights into the DataFrame's structure and contents.
 3: Assisting in understanding the data before performing analysis or manipulation.
 4: Helping identify potential issues with the data, such as missing values or incorrect data types.
 5: Serving as a quick reference for the DataFrame's schema and basic statistics.
 """

df2 = pd.read_excel("SampleSuperstore.xlsx")
#print(df2.info())

data ={
    "Name": ['hanif','kashif','uzaifa'],
    "age": [ 12,35,6],
    "city": ['isb','swat', 'dir']
}

df = pd.DataFrame(data)
print(df.info())