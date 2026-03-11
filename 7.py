

# ✅ Method 3 — .iloc[] — Position-Based Selection
# Use .iloc when you want to select by number position (like list indexing).

import pandas as pd

data = {
    "Name" : ["Shafi","Shafay","Suhail","Aqsa","Hassan","Hussain"] ,
    "Age" : ["18","19","20","21","22","15"] ,
    "City" : ["Multan","Lahore","Murree","Jhang","RYK","India"]
}

df = pd.DataFrame(data)

print(df.iloc[0])  # First row (position 0)
print(df.iloc[0,1])   # Row position 0, column position 1 → 18
print(df.iloc[0:2,0:2])  # First 2 rows, first 2 columns

# .iloc is exclusive — 0:2 means positions 0 and 1 only (not 2).

