
# ✅ Method 2 — .loc[] — Label-Based Selection
# Use .loc when you want to select by row label and column name.

import pandas as pd

data = {
    "Name" : ["Shafi","Shafay","Suhail","Aqsa","Hassan","Hussain"] ,
    "Age" : ["18","19","20","21","22","15"] ,
    "City" : ["Multan","Lahore","Murree","Jhang","RYK","India"]
}

df = pd.DataFrame(data)

print(df.loc[0])  # row with index label 0 
print(df.loc[0,"Name"])  # Shafi is selected 
print(df.loc[ 0:2 , "Name" : "Age" ])  # Rows 0 to 2 

