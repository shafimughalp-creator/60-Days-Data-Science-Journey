
# 🚀 Day 5 — Filtering · Sorting · Selecting Columns · Boolean Conditions

# 1️⃣ Selecting Columns
# Selecting means grabbing specific columns from your DataFrame.

import pandas as pd 

data = {
    "Name" : ["Ali","Shafi","Shafay","Suhail"] ,
    "Age" : [18,19,20,21] ,
    "Salary" : [10000,20000,30000,40000] ,
    "City" : ["Multan","Ryk","Islamabad","Rawalpindi"]
}

df = pd.DataFrame(data)

# Selcting one coloumn
print(df["Name"])

# Selecting multiple coloumn
print(df[["Name","Age"]])

# Why it matters: Real datasets have 50+ columns. You only 
# need 3-4 for your analysis. Selecting saves memory and keeps things clean.

# 2️⃣ Filtering Rows
# Filtering means keeping only the rows that match a condition.

# Filter only people with salary above 10000
high_salary = df[df["Salary"] > 10000 ]
print(high_salary)

# Filter only people with from islamabad
Islamabad_people = df[df["City"] == "Islamabad"]
print(Islamabad_people)

# 3️⃣ Boolean Conditions
# Boolean means True/False. When you write
# df['Salary'] > 20000, Pandas checks every row and returns True or False.

print(df['Salary'] > 20000 )

# 4️⃣ Multiple Conditions (AND / OR)
# AND BOTH CONDITIONS = TRUE 
# OR EITHER 1 CONDITION TO BE TRUE 

# AND CONDITION 
Result = df[(df["Salary"] > 20000)  & (df["Age"] < 22 )]
print(Result)

# OR CONDITION 
Result_2 = df[(df["City"] == "Multan") | (df["City"] == "Ryk")]
print(Result_2)

# 5️⃣ Sorting
# Sorting means arranging rows in order

# Salary (low to high)
df_sorted = df.sort_values("Salary")
print(df_sorted)

# Salary (High to low)
df_high = df.sort_values("Salary",ascending=False)
print(df_high)

# Sort by multiple columns
df_multi = df.sort_values(['Age', 'Salary'], ascending=[True, False])
print(df_multi)