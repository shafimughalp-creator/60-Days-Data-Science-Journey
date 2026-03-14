

# Day 6: Handling Missing Values · GroupBy · Aggregations


# Day 6 — Proper Beginner Version
# We have 3 topics today:

# 1 Handling Missing Values
# 2 GroupBy
# 3 Aggregations


# Building the data first 

import pandas as pd 
import numpy as np 

df = pd.DataFrame({
    'Name':       ['Ali', 'Sara', 'John', 'Mia', 'Tom'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance'],
    'Salary':     [50000, 80000, 55000, np.nan, 70000],
    'Age':        [28, np.nan, 45, 29, 38]
})


print(df)   # PRINTING ALL THE DATA 

# Step 1: What is NaN?
# NaN means "this cell is empty." Nothing more. Just a blank space 
# in your data. Like someone forgot to fill in a form field.
# In our data:

# Sara forgot to fill her Age
# Mia forgot to fill her Salary
# That's all NaN is.


# Step 2: Finding the blanks
# First thing you always do with real data — check where the blanks are.

print(df.isnull())
# True means there is a blank.
# False means data exists.

print(df.isnull().sum())
# This tells you how many blanks are in each column. 
# Much more useful than staring at True/False.


# Step 3: Removing the blanks
print(df.dropna())

# Sara and Mia are gone. 
# Why? Because dropna() removes any row that has even one blank.
# Sara had a blank Age. Mia had a blank Salary. Both deleted.


# Step 4: Filling the blanks instead of removing
# Sometimes deleting is too aggressive.
# You lose good data. 
# For example Mia's Department and Age are perfectly fine — 
# only Salary is missing.
# So instead of deleting, we fill the blank with something

Average_salary = df["Salary"].mean()
print(Average_salary)

# now using fillina()
df["Salary"] = df['Salary'].fillna(df['Salary'].mean())
df["Age"] = df['Age'].fillna(df['Age'].mean())

print(df)

# Check: are there any blanks left in df?
print(df.isnull().sum())