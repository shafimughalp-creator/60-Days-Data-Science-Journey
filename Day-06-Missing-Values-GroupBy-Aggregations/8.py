


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name':       ['Ahmed', 'Sara', 'John', 'Mia', 'Tom', 'Zara', 'Ali'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Salary':     [50000, 80000, 55000, np.nan, 70000, 65000, np.nan],
    'Age':        [28, np.nan, 45, 29, 38, np.nan, 32]
})

print(df)

# Question 5 — Medium
# Find the total salary and number of employees in each department.
# Use .agg() — do it in one line.

result = df.groupby("Department").agg({
    "Name" : ["count"] ,
    "Salary" : ["sum"]
})
print(result)

