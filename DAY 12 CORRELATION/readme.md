# 🧪 Day 12 — Correlation & Data Analysis

Welcome to **Day 12** of my Data Science journey 🚀

Today’s focus was understanding **correlation** and how different variables relate to each other using Pandas.

---

## 📌 Topics Covered

- 📊 What is Correlation?
- ➕ Positive Correlation
- ➖ Negative Correlation
- ⚖️ No Correlation
- 🐼 Using `pandas.DataFrame.corr()`

---

## 🧠 Key Concept

Correlation shows the **relationship between two variables**:

| Type                | Meaning                                      |
|--------------------|----------------------------------------------|
| Positive (+1)      | Both increase together                       |
| Negative (-1)      | One increases, other decreases               |
| Zero (0)           | No relationship                             |

---

## 💻 Code Example

```python
import pandas as pd

data = {
    "Exercise": [10, 20, 30, 40, 50],
    "Weight": [90, 85, 80, 75, 70]
}

df = pd.DataFrame(data)

print(df.corr())
