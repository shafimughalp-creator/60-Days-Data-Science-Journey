

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name':       ['Ahmed', 'Sara', 'John', 'Mia', 'Tom', 'Zara', 'Ali'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Salary':     [50000, 80000, 55000, np.nan, 70000, 65000, np.nan],
    'Age':        [28, np.nan, 45, 29, 38, np.nan, 32]
})

print(df)

# Question 1 — Easy
# How many missing values are in each column?
# Write the code to find out.

print(df.isnull().sum())

# Question 2 — Easy
# Fill the missing Salary values with the average salary.
# Fill the missing Age values with the average age.
# Then print the DataFrame to confirm no blanks are left.

df["Salary"] = df['Salary'].fillna(df['Salary'].mean())

df["Age"] = df['Age'].fillna(df['Age'].mean())


print(df)

# 
