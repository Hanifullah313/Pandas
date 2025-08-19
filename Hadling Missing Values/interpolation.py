import pandas as pd
# data of 10 random people also include salary and job performance 
data = {
    "Name": ['Alice', None, 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    "Age": [23, 45, 34, 25, None, 29, 41, 38, None, 30],
    "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin'],
    "salary": [55000, 72000, 68000, 48000, 61000, 59000, 75000, 70000, 53000, 62000],
    "job performance": [88, 75, None, 85, 79, 90, 87, 80, 95, 83]
}

df=pd.DataFrame(data)
df["Age"]=df["Age"].interpolate(method="linear")
print(df)