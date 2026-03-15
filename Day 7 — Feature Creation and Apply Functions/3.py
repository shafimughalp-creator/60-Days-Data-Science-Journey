

# 📌 PART 5 — np.where() — Fastest Way for Simple Conditions
# Before learning apply(), learn np.where().
#  It's the fastest and most common way to create a conditional column.
#  You'll see it everywhere in real code:

import pandas as pd
import numpy as np

data = {
    'product': ['A', 'B', 'C', 'D'],
    'sales': [1000, 1500, 800, 2000],
    'cost': [600, 900, 500, 1100]
}

df = pd.DataFrame(data)

df["sales_category"] = np.where(df['sales'] >= 1500 , 'High' , "Low" )

print(df[['product','sales','sales_category']])


# 📌 PART 6 — pd.cut() — Grouping Numbers into Bins
#  pd.cut() lets you group a numeric column into labeled categories.
#  Very useful in EDA:

data2 = {
    'name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'age': [15, 28, 42, 67, 33]
}

df2 = pd.DataFrame(data2)

df2["age_group"] = pd.cut(
    df2["age"] ,
    bins=[0,18,60,100] ,
    labels=["young","adult,unc","old"]
)

print(df2)

# When to use pd.cut(): 
# When you want to turn a continuous number (age, salary, score) into meaningful groups.


# 📌 PART 7 — map() 

df["product_full"] = df['product'].map({"A" : "Apple" , "B" : "Banana" , "C" : "Cherry" , "D" : "Dates "})
print(df[["product","product_full"]])

