


import pandas as pd

data = {
    'product': ['A', 'B', 'C', 'D'],
    'sales': [1000, 1500, 800, 2000],
    'cost': [600, 900, 500, 1100]
}

df = pd.DataFrame(data)

df['profit'] = df['sales'] - df['cost']
df['profit_margin'] = (df['profit'] / df['sales']) * 100

df['sales_category'] = df['sales'].apply(lambda x: 'High' if x >= 1500 else 'Low')
print(df[['product', 'sales', 'sales_category']])

def profit_label(margin):
    if margin >= 45:
        return 'Excellent'
    elif margin >= 40:
        return 'Good'
    else:
        return 'Average'

df['margin_label'] = df['profit_margin'].apply(profit_label)
print(df[['product', 'profit_margin', 'margin_label']])


# 📌 PART 4 — apply() on Multiple Columns (axis=1)
# Sometimes you need to look at multiple columns at once in your function:

def bonus(row) :
    if row["sales"] > 1500 and row["profit_margin"] > 40 :
        return "Big Bonus"
    elif row['sales'] > 1000 :
        return "Small Bonus"
    else :
        return "No bonus"
    
df["bonus"] = df.apply( bonus , axis=1 ) 
print(df[["product","sales","profit","bonus"]])   