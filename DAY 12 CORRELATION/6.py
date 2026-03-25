

# 🟣 LEVEL 4 — Basic EDA
# ✅ Task 7

# Dataset:


import pandas as pd 


data = {
    "Name": ["Ali", "Sara", "Ahmed", "John", "Ayesha"],
    "Age": [20, 25, None, 30, 22],
    "Salary": [20000, 30000, 25000, None, 28000],
    "City": ["Multan", "Lahore", "Karachi", "Multan", "Lahore"]
}

df = pd.DataFrame(data)

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Questions:
# Which column has missing values?
# How many missing values are there?

# AGE AND SALARY HAS MISSING VALUES 
# BOTH HAS 1 MISSING VALUE EACH 

