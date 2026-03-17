
# Day 1–7 Revision Notes — Mistakes and Corrections

---

## SECTION 1 — Math and NumPy

---

### Normal Distribution — CORRECTED

Definition:
A bell shaped curve where most values are near the mean
and fewer values appear at the extremes.

Wrong example I gave:
Everyone passing an exam — this is skewed not normal.

Correct real life example:
Heights of people.
Most people are average height.
Very few are extremely tall or extremely short.

Key properties:
- Symmetrical around the mean
- Mean = Median = Mode
- 68% of data falls within 1 standard deviation
- 95% within 2 standard deviations

---

### Correlation — CORRECTED

What correlation tells us:
How two variables move together.
If one increases does the other increase or decrease?

Correlation values:
+1   = perfect positive — both move up together
 0   = no relationship at all
-1   = perfect negative — one goes up, other goes down

Real life example of -1:
As price of a product increases → demand decreases.

What I said wrong:
I said -1 means standard deviation is at 65%.
That is completely wrong — that is a different concept entirely.

---

### Mean — CORRECTED

I forgot to print the answer in Q1.

data = [4, 8, 15, 16, 23]
Mean = (4 + 8 + 15 + 16 + 23) / 5 = 13.2

Always print your answer — do not just load the data.

---

## SECTION 2 — Pandas Basics

---

### Filtering Rows — CORRECTED

Wrong code I wrote:
Filtering_Age = data["Age"] > 23
print(Filtering_Age)
This prints True/False values — not the actual rows.

Correct code:
print(data[data["Age"] > 23])
Wrap the condition inside the DataFrame to get actual rows.

---

### sort_values — CORRECTED

Wrong code I wrote:
print(data["Age"].sort_values(ascending=True))
This sorts only the Age column and in wrong order.

Correct code:
print(data.sort_values("Age", ascending=False))
Always sort the full DataFrame not a single column.
ascending=False for descending order.

---

## SECTION 3 — Feature Engineering

---

### profit_margin Formula — CORRECTED

Wrong formula I used:
data["profit_margin"] = (data["profit"] / data["Cost"]) * 100

Correct formula:
data["profit_margin"] = (data["profit"] / data["Sales"]) * 100

Why:
Profit margin is always measured against revenue (Sales).
Not against what you spent (Cost).

Example:
Sales = 2000
Cost = 1200
Profit = 800
Profit Margin = (800 / 2000) * 100 = 40%

---

### np.where() Boolean — CORRECTED

Wrong code I wrote:
np.where(data["attendance"] >= 75, "True", "False")
This creates string values not actual booleans.

Correct code:
np.where(data["attendance"] >= 75, True, False)
Use actual True and False without quotes.

---

### axis=1 in apply() — CORRECTED

Wrong understanding:
I thought axis=1 means working on a column.

Correct understanding:
axis=0 = column by column (going down)
axis=1 = row by row (going across columns)

Use axis=1 when your function needs to look at
multiple columns in the same row at the same time.

Example:
def bonus(row):
    if row["sales"] > 1500 and row["profit"] > 40:
        return "Big Bonus"
    else:
        return "No Bonus"

df["bonus"] = df.apply(bonus, axis=1)

---

## SECTION 4 — Concept Understanding

---

### Feature Engineering — CORRECTED

What I said:
Feature engineering uses less lines of code.

Correct definition:
Feature engineering creates new meaningful columns from existing data.
It gives the model more useful information to learn from.

Example:
Extracting month from a date column helps predict seasonal sales.
Creating a profit_margin column gives more insight than raw profit alone.

---

### np.where() vs apply() — SUMMARY

Use np.where() when:
- Simple True/False condition on one column
- You want fast performance on large datasets

Use apply() when:
- Complex logic with multiple conditions
- Logic needs more than one column (use axis=1)
- You need a custom function

---

### 3 Ways to Handle Missing Values — COMPLETE ANSWER

1. fillna(mean)    fill with average — good for salary, scores
2. fillna(median)  fill with median — better when outliers exist
3. dropna()        remove rows — only when missing data is very small

Which to choose:
For salary column use fillna(mean) because
dropping rows loses data and mean gives a fair estimate.
Use median if there are very high or very low outliers in salary.

---

## QUICK REVISION TABLE

Topic                     Mistake               Fix
Normal distribution       Wrong example         Bell curve, heights of people
Correlation -1            Wrong definition      Perfect negative relationship
profit_margin             Divided by cost       Always divide by sales
axis=1                    Thought it was column Row by row across columns
sort_values               Sorted one column     Sort full DataFrame
np.where() booleans       Used strings          Use True False without quotes
Filtering rows            Printed True/False    Wrap condition in DataFrame
