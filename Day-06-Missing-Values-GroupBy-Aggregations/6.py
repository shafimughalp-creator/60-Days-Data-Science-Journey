


# Question 3 — Easy
# Drop any row that has at least one missing value from the original DataFrame.
# How many rows are left?

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name':       ['Ahmed', 'Sara', 'John', 'Mia', 'Tom', 'Zara', 'Ali'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Salary':     [50000, 80000, 55000, np.nan, 70000, 65000, np.nan],
    'Age':        [28, np.nan, 45, 29, 38, np.nan, 32]
})

print(df)

print(df.dropna())

# 3 rows are left now 
