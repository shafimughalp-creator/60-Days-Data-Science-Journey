

# Topic 3 — Aggregations
# First — What problem does .agg() solve?
# In Topic 2 I learned GroupBy. But notice — every time 
# I wanted a different calculation I had to write a separate line:

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name':       ['Ali', 'Sara', 'John', 'Mia', 'Tom'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance'],
    'Salary':     [50000, 80000, 55000, np.nan, 70000],
    'Age':        [28, np.nan, 45, 29, 38]
})

# Step 1: Your First .agg()
result = df.groupby("Department")["Salary"].agg(["mean","max","min","count"])
print(result)

# One table. Four calculations. All departments. That's .agg().


# Step 2: Breaking Down the Syntax
#        df.groupby('Department')['Salary'].agg(['mean', 'max', 'min', 'count'])
# │                        │          │
# │                        │          └── List of calculations you want
# │                        └── Column to calculate on
# └── Group by Department
# The only new thing is .agg([]) — you pass a list of calculations inside it.


# Step 3: Multiple Columns at Once
# What if you want stats for both Salary AND Age at the same time?

result = df.groupby("Department").agg({
    "Salary" : ["mean","max","min"] ,
    "Age" : ["mean","max","min"]
})

print(result)

# Step 4: value_counts()
# This one is simple but super useful. It answers:

"How many times does each value appear in a column?"

print(df["Department"].value_counts())

