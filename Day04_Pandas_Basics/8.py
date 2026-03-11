

# 🔷 Setting a Custom Index
# By default the index is 0, 1, 2... But you can set any column as the index:

import pandas as pd 

data = {
    "Name" : ["Shafi","Shafay","Suhail","Aqsa","Hassan","Hussain"] ,
    "Age" : ["18","19","20","21","22","15"] ,
    "City" : ["Multan","Lahore","Murree","Jhang","RYK","India"]
}

df = pd.DataFrame(data)

df = df.set_index("Name")
print(df)

print(df.loc["Shafi"])

df.reset_index()
print(df)