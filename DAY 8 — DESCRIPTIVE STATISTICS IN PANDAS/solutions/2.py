
# ✏️ DAY 8 — ALL PRACTICE TASKS
# Task 1 — describe()
# Create a DataFrame with columns Product, Price, Quantity (5 rows of your choice). 
# Run df.describe() and write in a comment what the mean price and max quantity are.

import pandas as pd 


data = {
    "Product" : ["Football","Cricket_balls","Baseball_bat","Football","Rugby"] ,
    "Price" : [1000,2000,3000,4000,2000] ,
    "Quantity" : [2,3,4,2,3]
}

df = pd.DataFrame(data)
print(df.describe())

# mean   2400.000000   2.80000
# max    4000.000000   4.00000

# Task 2 — Individual Stats
# Using the same DataFrame, find:

# The minimum price
# The maximum quantity
# The average price

# Print all three using separate commands.

print("Minimum price =" , df["Price"].min())
print("Maximum price =" , df["Price"].max())
print("Average price = " , df['Price'].mean())


# Task 3 — Median vs Mean
# Add a row where Price is 9999 (an extreme value). Now compare:

# df['Price'].mean() vs df['Price'].median()

# Which one better represents a "typical" price? Write your answer as a comment.

df.loc[len(df)] = ["NEW PRICE = " , 9999 , 1 ]

print("Mean = " , df["Price"].mean())
print("Median = " , df["Price"].median())



# Task 4 — value_counts()

# Create a DataFrame with a Category column containing values like 'Electronics', 'Clothing',
# 'Food' repeated across 8 rows. Use value_counts() to find which category appears most.

data2 = {
    "Category" : ["Electronics","Clothing","Food","Food","Food","Clothing","Clothing","Electronics"]
}

df2 = pd.DataFrame(data2)
print(df2["Category"].value_counts())


# Task 5 — Missing Values
# Create a DataFrame with at least 2 None values in different columns.
#  Use isnull().sum() to confirm you can detect them.

data3 = {
    "Name" : ["Shafi","Shafay", None , "Ali" , None],
    "Grade" : ["A","B",None,None,"C"]
}

df3 = pd.DataFrame(data3)
print(df3.isnull().sum())



# Task 6 — df.info() Reading
# Using your DataFrame from Task 1, run df.info(). Answer these 3 questions in comments:

# How many non-null values does each column have?
# What is the dtype of Price?
# What is the dtype of Product?

print(df.info())

# 6 non-null  values in each colomn 

# dtype of product is string 
# dtype of price is int


data4 = {
    'Student': ['Ali', 'Sara', 'Umar', None, 'Bilal'],
    'Math':    [88, 95, None, 70, 60],
    'English': [75, 80, 90, 85, 55]
}
df4 = pd.DataFrame(data4)


print(df4.info())
print(df4.describe())
print(df4['Math'].mean())
print(df4['Math'].median())
print(df4.isnull().sum())
print(df4['Student'].value_counts())