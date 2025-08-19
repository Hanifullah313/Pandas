import pandas as pd
# data of 10 random people also include salary and job performance 
data = {
    "Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    "Age": [23, 45, 34, 25, 32, 29, 41, 38, 27, 30],
    "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin'],
    "salary": [55000, 72000, 68000, 48000, 61000, 59000, 75000, 70000, 53000, 62000],
    "job_per": [88, 75, 92, 85, 79, 90, 87, 80, 95, 83]
}

df=pd.DataFrame(data)

# filtering rows based on single condition
high_salary = df[df['salary']>60000]
#print(f'salary > 60000: \n {high_salary}')

# filtering rows based on multiple conditions
high_salary_performance = df[(df['salary']>60000) & (df['job_per']>85)]
#print(f'salary > 60000 and job performance > 85: \n {high_salary_performance}')

# filtering rows based on OR condition
high_salary_or_performance = df[(df['salary']>60000) | (df['job_per']>85)]
print(f'salary > 60000 or job performance > 85: \n {high_salary_or_performance}')