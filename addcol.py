import pandas as pd
# data of 10 random people also include salary and job performance 
data = {
    "Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    "Age": [23, 45, 34, 25, 32, 29, 41, 38, 27, 30],
    "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin'],
    "salary": [55000, 72000, 68000, 48000, 61000, 59000, 75000, 70000, 53000, 62000],
    "job performance": [88, 75, 92, 85, 79, 90, 87, 80, 95, 83]
}

df=pd.DataFrame(data)
print(f'before addding bonus column in  df : \n\n{df}\n\n')
#adding new column
df["bonus"]=df["salary"]*0.1
#print(f'after addding bonus column in  df : \n\{df}')
df.insert(0, "Em_ID",[0,1,2,3,4,5,6,7,8,9])
print(f'after addding EM_ID Through Insert Methed column in  df : \n\{df}')