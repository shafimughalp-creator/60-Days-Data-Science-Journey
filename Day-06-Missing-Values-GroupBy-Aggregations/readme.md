# Day 06 — Pandas: Missing Values, GroupBy and Aggregations

Part of my 60-Day Data Science Roadmap — working towards a Junior Data Scientist role.
Phase 1 · Day 6 of 60

---

## Overview

On Day 6 I learned how to handle real-world messy data using Pandas.
Real datasets are never clean — they always have missing values and
incomplete rows. Today's topics are the foundation of every data
cleaning and analysis workflow.

---

## Topics Covered

Topic 1 — Missing Values
What I learned: How to find, remove, and fill NaN values

Topic 2 — GroupBy
What I learned: How to split data into groups and calculate stats

Topic 3 — Aggregations
What I learned: How to get multiple calculations in one clean table

---

## Key Concepts

1. Missing Values
Real data always has blanks. Pandas shows them as NaN.
Two decisions: drop the row or fill the blank with mean or median.

2. GroupBy
Follows Split → Apply → Combine.
Split data into groups, apply a calculation, combine into one table.

3. Aggregations
.agg() runs multiple calculations at once.
No need to write separate lines for each calculation.

---

## Quick Code Reference

# Find missing values
df.isnull().sum()

# Remove missing values
df.dropna()
df.dropna(subset=['Age'])

# Fill missing values
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# GroupBy
df.groupby('Department')['Salary'].mean().reset_index()

# Aggregations
df.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'Age':    ['mean', 'min']
}).reset_index()

---

## What I Can Do After Today

- Find and count missing values in any dataset
- Decide whether to drop or fill missing values
- Group data by any category
- Calculate stats per group using groupby
- Produce clean summary tables using .agg()
- Build a full clean → analyze pipeline

---

## Roadmap Progress

Day 1  — NumPy basics              — Done
Day 2  — NumPy operations          — Done
Day 3  — Distributions             — Done
Day 4  — Pandas basics             — Done
Day 5  — Filtering and Sorting     — Done
Day 6  — Missing Values GroupBy Aggregations — Done
Day 7  — Feature Creation Apply Functions    — Next

---

60 days. 4 phases. 3 projects. 1 goal — get hired.
