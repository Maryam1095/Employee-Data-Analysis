# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:58:18 2023

@author: USER
"""
import pandas as pd

data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
    'Experience': [3, 7, 2, 5, 10, 4]
}

employee_df = pd.DataFrame(data)
#Displaying the first three rows 

first_three_rows = employee_df.iloc[:3]
print(first_three_rows)

# Select all rows where the Department is "Marketing" using loc
marketing_department = employee_df.loc[employee_df['Department'] == 'Marketing']
print(marketing_department)

# Select 'Age' and 'Gender' columns for the first 4 rows using iloc
age_gender_first_four_rows = employee_df.iloc[:4, [2, 3]]
print(age_gender_first_four_rows)

# Select 'Salary' and 'Experience' columns for all rows where Gender is "Male" using loc
male_employees_data = employee_df.loc[employee_df['Gender'] == 'Male', ['Salary', 'Experience']]
print(male_employees_data)

