
# Day 7 Notes — Feature Creation & Apply Functions

---

## What is Feature Creation?

Feature creation means making new columns from existing ones.
This gives your model or analysis more useful information.
It is called feature engineering — one of the most important real-world skills.

Example:
df['profit'] = df['sales'] - df['cost']
df['profit_margin'] = (df['profit'] / df['sales']) * 100

---

## Extracting Date Features

Use .dt to extract parts from a date column.

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()

You will use this directly in your portfolio projects.

---

## np.where() — Fastest Way for Simple Conditions

Syntax:
np.where(condition, value_if_true, value_if_false)

Example:
df['sales_category'] = np.where(df['sales'] >= 1500, 'High', 'Low')

When to use:
- Simple True/False conditions on one column
- Much faster than apply() on large datasets

---

## pd.cut() — Grouping Numbers into Bins

Example:
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 18, 35, 60, 100],
    labels=['Young', 'Adult', 'Middle-Aged', 'Senior']
)

When to use:
- When you want to turn a continuous number into meaningful groups
- Age, salary, score, attendance — anything numeric

---

## map() vs apply()

map()
- Works on a single Series only
- Best for simple value substitution
- Faster

apply()
- Works on a Series or entire rows
- Best for complex custom logic
- Slightly slower

map() example:
df['product_full'] = df['product'].map({'A': 'Apple', 'B': 'Banana'})

Rule:
Use map() when replacing values in one column.
Use apply() when you need logic or multiple columns.

---

## apply() with Lambda

df['margin_category'] = df['profit_margin'].apply(
    lambda x: 'High' if x >= 45 else 'Medium' if x >= 40 else 'Low'
)

---

## apply() with a Custom Function

def profit_label(margin):
    if margin >= 45:
        return 'Excellent'
    elif margin >= 40:
        return 'Good'
    else:
        return 'Average'

df['margin_label'] = df['profit_margin'].apply(profit_label)

---

## apply(axis=1) — Logic Across Multiple Columns

def bonus(row):
    if row['sales'] > 1500 and row['profit_margin'] > 40:
        return 'Big Bonus'
    elif row['sales'] > 1000:
        return 'Small Bonus'
    else:
        return 'No Bonus'

df['bonus'] = df.apply(bonus, axis=1)

axis=1 means row by row.
Use this when your logic needs more than one column at a time.

---

## Important Warning

apply() is great for learning and small datasets.
On millions of rows, use vectorized operations like np.where() or arithmetic.
They are much faster. Build this habit early.

---

## Quick Reference Table

Situation                        Tool
Simple math on columns           df['a'] + df['b']
Simple True/False condition      np.where()
Replace values in a column       map()
Group numbers into categories    pd.cut()
Complex logic on one column      apply() with lambda or function
Logic using multiple columns     apply(axis=1)
