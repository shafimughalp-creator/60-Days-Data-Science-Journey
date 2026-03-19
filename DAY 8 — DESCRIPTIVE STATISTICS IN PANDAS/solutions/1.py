

# 📅 Day 8 — Descriptive Statistics in Pandas · Summary Analysis

# 🧠 What problem does this solve?
# Imagine you're handed a dataset of 10,000 sales records. 
# You don't want to read every row. You want instant answers:


# What's the average? The highest? The lowest?
# Are there missing values?
# How spread out is the data?

# Descriptive statistics gives you that full picture in seconds.


# 📌 Concept 1 — df.describe() — The Full Summary

import pandas as pd

data = {
    'Name':  ['Ali', 'Sara', 'Umar', 'Zara', 'Bilal'],
    'Score': [85, 92, 78, 95, 60],
    'Age':   [20, 22, 21, 23, 19]
}

df = pd.DataFrame(data)

print(df.describe())

# ### 🔍 Output Explained:
# | Row | Meaning |
# |---|---|
# | `count` | Total non-missing values |
# | `mean` | Average of all values |
# | `std` | How spread out values are |
# | `min` | Lowest value |
# | `25%` | 25% of data falls below this |
# | `50%` | Middle value (median) |
# | `75%` | 75% of data falls below this |
# | `max` | Highest value |

# > 📌 `Name` is not shown — `describe()` only works on **numeric columns** by default.

### 🔨 Syntax Breakdown:
# ```
# df  .describe()
# ↑       ↑
# table   gives you the full statistical summary


# 📌 Concept 2 — df.mean(), df.min(), df.max() — Individual Stats

print(df["Score"].mean())   # Average 
print(df['Score'].min())   # Lowest number 
print(df['Score'].max())   # Highest number 

# ### 🔍 Output Explained:
# - `82.0` → The average of all 5 scores
# - `60` → Bilal had the lowest score
# - `95` → Zara had the highest score

### 🔨 Syntax Breakdown:
# ```
# df  ['Score']  .mean()
# ↑       ↑          ↑
# table  column    calculation you want



# 📌 Concept 3 — df.median() and df.std() — Median & Spread
# Median = the middle value when sorted. Better than mean when data has extreme values.
# std (Standard Deviation) = how far values typically are from the average.

# 💡 Real-life analogy: If 4 students scored 80 and 1 student scored 5, 
# the mean drops to 65 — but median stays near 80. Median tells a truer story.

print(df['Score'].median())   # Middle value
print(df['Score'].std())    # how data is spread out 



# 📌 Concept 4 — df.value_counts() — Count Frequency

# For non-numeric (text) columns, describe() doesn't help.
# value_counts() counts how many times each value appears.

data2 = {
    'City': ['Lahore', 'Karachi', 'Lahore', 'Islamabad', 'Lahore', 'Karachi']
}

df2 = pd.DataFrame(data2)
print(df2["City"].value_counts())

# ### 🔍 Output Explained:
# - Lahore appears 3 times — most frequent city
# - Islamabad appears only once — least frequent
# - Values are sorted from most to least automatically

### 🔨 Syntax Breakdown:
# ```
# df2  ['City']   .value_counts()
#  ↑      ↑             ↑
# table  column    count each unique value



# 📌 Concept 5 — df.isnull().sum() — Find Missing Values
# Real datasets always have missing data. 
# This command tells you exactly which columns have gaps and how many.

data3 = {
    'Name':  ['Ali', 'Sara', None, 'Zara'],
    'Score': [85, None, 78, 95],
    'Age':   [20, 22, 21, 23]
}

df3 = pd.DataFrame(data3)

print(df3.isnull().sum())

# ### 🔍 Output Explained:
# - `Name` has 1 missing value (the `None` we put)
# - `Score` has 1 missing value
# - `Age` has 0 — completely filled

### 🔨 Syntax Breakdown:
# ```
# df3  .isnull()   .sum()
#  ↑       ↑          ↑
# table  mark True   count all
#        where empty  the Trues


# 📌 Concept 6 — df.info() — Dataset Overview

# Before any analysis, always run df.info() first. 
# It tells you column names, data types, and missing value counts — all at once.

print(df3.info())

# ### 🔍 Output Explained:
# - `4 entries` → 4 rows total
# - `Non-Null Count` → how many values are filled (not missing)
# - `Dtype` → object = text, int64 = whole numbers, float64 = decimals
# - Memory usage → how much RAM your dataset is using

### 🔨 Syntax Breakdown:
# ```
# df3  .info()
#  ↑      ↑
# table   gives structural overview — not the values, but the shape


