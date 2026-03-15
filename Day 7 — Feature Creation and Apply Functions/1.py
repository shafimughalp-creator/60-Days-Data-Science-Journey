

# Day 7 — Feature Creation · Apply Functions · Practice Dataset

# 📌 PART 1 — What is Feature Creation?
# Feature creation means making new columns 
# from existing ones to give your model or analysis more useful information.

import pandas as pd
import numpy as np

data = {
    'product': ['A', 'B', 'C', 'D'],
    'sales': [1000, 1500, 800, 2000],
    'cost': [600, 900, 500, 1100]
}

df = pd.DataFrame(data)

# Creating new features 
df["Profit"] = df["sales"] - df["cost"]
df['Profit_Margin'] = (df['Profit'] / df['sales']) * 100

print(df)


# just created 2 new features from existing data. This is feature engineering.


# 📌 PART 2 — Extracting from Dates (Very Common!)

df["date"] = pd.to_datetime(['2024-01-15', '2024-03-22', '2024-07-04', '2024-11-30'])

df["month"] = df["date"].dt.month
df["day"] = df['date'].dt.day
df["weekend"] = df['date'].dt.day_name()

print(df[["date","month","day","weekend"]])

