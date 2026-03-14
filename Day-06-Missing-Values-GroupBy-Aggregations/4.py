



# Step 5: Putting It All Together
# Now let's combine everything from Day 6 into one real workflow:

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name':       ['Ali', 'Sara', 'John', 'Mia', 'Tom'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance'],
    'Salary':     [50000, 80000, 55000, np.nan, 70000],
    'Age':        [28, np.nan, 45, 29, 38]
})

# step 1 check for missing values 
print(df.isnull())

# filling missing values 
df["Salary"] = df['Salary'].fillna(df['Salary'].mean())
df["Age"] = df['Age'].fillna(df['Age'].mean())


# step 3 group and aggregate 
result = df.groupby("Department").agg({
    "Salary" : ["min","max"] ,
    "Age" : ["max","min"]
}).reset_index()

print(result)

