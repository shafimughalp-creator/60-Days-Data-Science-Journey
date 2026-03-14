
# Question 4 — Medium
# Find the average salary of each department



import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name':       ['Ahmed', 'Sara', 'John', 'Mia', 'Tom', 'Zara', 'Ali'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Salary':     [50000, 80000, 55000, np.nan, 70000, 65000, np.nan],
    'Age':        [28, np.nan, 45, 29, 38, np.nan, 32]
})

# Step 1 - fill blanks first
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Step 2 - groupby + agg
result = df.groupby('Department')['Salary'].agg(['sum', 'count']).reset_index()
print(result)




