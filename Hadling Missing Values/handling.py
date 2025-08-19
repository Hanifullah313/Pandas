import pandas as pd
# data of 10 random people also include salary and job performance 
data = {
    "Name": ['Alice', None, 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    "Age": [23, 45, 34, 25, None, 29, 41, 38, 27, 30],
    "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin'],
    "salary": [55000, 72000, 68000, 48000, 61000, 59000, 75000, 70000, 53000, 62000],
    "job performance": [88, 75, None, 85, 79, 90, 87, 80, 95, 83]
}

df=pd.DataFrame(data)
print(f'before removing null values : \n\n {df}\n\n')

#Removing missing values through dropna() method
#df.dropna(inplace=True)
#print(f'before removing null values : \n\n {df}')

#filling missing values through fillna() method
#df.fillna(0, inplace=True)
#print(f'after filling  null values : \n\n {df}')


# another method of filling missing values 
df["Age"].fillna(df["Age"].mean() , inplace = True )
df["salary"].fillna(df["salary"].mean(), inplace = True)
df["job performance"].fillna(df["job performance"].mean(), inplace = True)
print(f'after filling  null values : \n\n {df}')