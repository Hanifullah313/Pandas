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
# selecting single column
salary_col = df['salary']
print(f'salaries : \n {salary_col}\n\n')

# selecting multiple columns
salary_performance = df[['salary', 'job performance']]
print(f'salaries and job performance : \n {salary_performance}')