

# Creating a Series with custom labels:

import pandas as pd 

ages = pd.Series([20,30,40,50] , index=["Shafi","Shafay","Suhail","Aqsa"])
print(ages)

# Accessing a value by label:
print(ages["Shafi"])

# Key things a Series has:

# values → the actual data as a NumPy array
# index → the labels
# dtype → the data type
# shape → how many items

print(ages.values)

print(ages.index)

print(ages.dtype)

print(ages.shape)

