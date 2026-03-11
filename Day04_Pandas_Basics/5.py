

# 🔷 INDEXING — Accessing Your Data
# This is one of the most important skills. There are 3 main ways:


import pandas as pd 

data = {
    "Name" : ["Shafi","Shafay","Suhail","Aqsa","Hassan","Hussain"] ,
    "Age" : ["18","19","20","21","22","15"] ,
    "City" : ["Multan","Lahore","Murree","Jhang","RYK","India"]
}

df = pd.DataFrame(data)

# ✅ Method 1 — Select a Column

print(df["Age"]) # returns a SINGLE COLOUMN 
print(df[["Name","City"]])


