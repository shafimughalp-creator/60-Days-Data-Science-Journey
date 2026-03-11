
# 🔷 DATAFRAME — The Full Table
# A DataFrame is a 2D table with rows and columns — like an Excel sheet.
#  Each column is a Series.
# Creating a DataFrame from a dictionary:

import pandas as pd 

data = {
    "Name" : ["Shafi","Shafay","Suhail","Aqsa","Hassan","Hussain"] ,
    "Age" : ["18","19","20","21","22","15"] ,
    "City" : ["Multan","Lahore","Murree","Jhang","RYK","India"]
}

df = pd.DataFrame(data)
print(df)


# 🔷 First Commands You Must Know
# These are the first things you run every time you open a new dataset:


print(df.head())       # First 5 rows
print(df.tail())       # Last 5 rows
print(df.shape)        # (rows, columns) — e.g. (4, 3)
print(df.info())       # Column names, data types, null counts
print(df.describe())   # Stats: mean, min, max, std for numeric columns
print(df.columns)      # List of column names
print(df.dtypes)       # Data type of each column

# Always run these first when you get a new dataset. 
# This is called a "first look."
