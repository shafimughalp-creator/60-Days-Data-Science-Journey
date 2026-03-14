

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name':       ['Ahmed', 'Sara', 'John', 'Mia', 'Tom', 'Zara', 'Ali'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Salary':     [50000, 80000, 55000, np.nan, 70000, 65000, np.nan],
    'Age':        [28, np.nan, 45, 29, 38, np.nan, 32]
})

print(df)

# Question 7 — Challenge
# Find the following for each department in one single .agg() call:

# Average Salary
# Maximum Salary
# Minimum Age
# Count of employees

Result = df.groupby("Department").agg({
    "Salary" : ["mean","max"] ,
    "Name" : ["count"] ,
    "Age" : ["min"]
})

print(Result)


