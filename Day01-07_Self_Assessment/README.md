
# Day 1–7 — Self Assessment & Review

Part of my 60-Day Data Science Journey

---

## What This Folder Is

After completing Day 1 to Day 7 I tested myself with 25 questions
across all topics before moving forward.
This folder contains my test answers, mistakes, and corrections.

---

## Topics Tested

- Mean, Variance, Standard Deviation (Day 1–2)
- Normal Distribution, Correlation (Day 2–3)
- NumPy operations and random numbers (Day 1–3)
- Pandas DataFrame, Series, Indexing (Day 4)
- Filtering, Sorting, Boolean conditions (Day 5)
- Missing values, GroupBy, Aggregations (Day 6)
- Feature Engineering, apply(), np.where(), pd.cut() (Day 7)

---

## My Score

Total: 16 out of 25

Section Breakdown:

Math and NumPy         4 out of 7
Pandas Basics          5 out of 7
Feature Engineering    4 out of 6
Concept Understanding  3 out of 5

---

## Key Mistakes I Made and Fixed

Mistake 1 — Normal Distribution
Wrong:   Everyone passing an exam = normal distribution
Correct: Bell shaped curve — most values near mean, few at extremes
Example: Heights of people

Mistake 2 — Correlation value of -1
Wrong:   Standard deviation is at 65%
Correct: Perfect negative correlation — when one variable goes up
         the other goes down perfectly
Example: Price increases → demand decreases

Mistake 3 — profit_margin formula
Wrong:   (profit / cost) * 100
Correct: (profit / sales) * 100
Reason:  Margin is always calculated against sales not cost

Mistake 4 — axis=1 in apply()
Wrong:   axis=1 means working on a column
Correct: axis=1 means row by row — across columns
         Use it when your function needs multiple columns at once

Mistake 5 — sort_values
Wrong:   data["Age"].sort_values(ascending=True)
Correct: data.sort_values("Age", ascending=False)
Reason:  Sort the full DataFrame not just one column

Mistake 6 — np.where() boolean
Wrong:   np.where(condition, "True", "False")
Correct: np.where(condition, True, False)
Reason:  Use actual booleans not strings

---

## Files in This Folder

- README.md          this file
- notes.md           all mistakes, corrections and concept clarifications
- test_answers/      folder with all 17 Python files (Q1 to Q25)

---

## Verdict

16 out of 25 — Revised weak topics before moving to Day 8

Topics revised:
- Correlation values
- Normal distribution
- axis=0 vs axis=1
- profit_margin formula
- sort_values on full DataFrame

---

Next Up — Day 8: Descriptive Statistics in Pandas and Summary Analysis
