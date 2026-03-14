
# Topic 2 — GroupBy

import pandas as pd 

data = ({
    "Name" : ["Ali","Sara","Jhon","Tim","Mia"] , 
    "Department" : ["HR","IT","IT","FINANACE","CEO"] ,
    "Salary" : [50000.0,80000.0,55000.0,60000.0,70000.0] ,
    "Age" : [18,18,19,20,21] ,
})

df = pd.DataFrame(data)

# Step 1 :
result = df.groupby("Department")["Salary"].mean()
print(result)

# Step 2
#df.groupby('Department')['Salary'].mean()
#│   │                   │          │
#│   │                   │          └── What to calculate
#│   │                   └── Which column to calculate on
#│   └── Group by which column
#└── Your DataFrame

# Step 3: Swap the Calculation
# You are not limited to mean. Try all of these one by one:

print(df.groupby("Department")["Salary"].sum()) # TOTAL SALARY PER DEPARTMENT
print(df.groupby("Department")["Salary"].max()) # HIGHEST SALARY PER DEPARTMENT
print(df.groupby("Department")["Salary"].min()) # LOWEST SALARY PER DEPARTMENT
print(df.groupby("Department")["Salary"].count()) # HOW MANY EMPLOYEES ? 

# Step 4: reset_index()

# Without reset index 
print(df.groupby("Department")["Salary"].mean())
# With reset index 
print(df.groupby("Department")["Salary"].mean().reset_index())


# How many employees are in each department?
print(df.groupby('Department')['Name'].count().reset_index())