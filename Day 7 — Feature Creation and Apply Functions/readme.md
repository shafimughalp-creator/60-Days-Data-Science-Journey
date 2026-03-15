
# Day 7 — Feature Creation & Apply Functions

Part of my 60-Day Data Science Journey

---

## Topics Covered

- Feature engineering — creating new columns from existing data
- Extracting date features with .dt (month, day, weekday)
- np.where() — fast conditional columns
- pd.cut() — binning numbers into labeled groups
- map() — simple value substitution
- apply() with lambda — complex single-column logic
- apply(axis=1) — logic across multiple columns
- When to use each tool

---

## Files in This Folder

- README.md — this file
- notes.md — key concepts and quick reference
- day7_feature_creation.py — full practice code

---

## Quick Reference

Situation                        Tool
Simple math on columns           df['a'] + df['b']
Simple True/False condition      np.where()
Replace values in a column       map()
Group numbers into categories    pd.cut()
Complex logic on one column      apply() with lambda
Logic using multiple columns     apply(axis=1)

---

## Key Insight

np.where() and vectorized operations are much faster than apply() on large datasets.
Use apply() for learning and small data — switch to vectorized for production.

---

Next Up — Day 8: Descriptive Statistics in Pandas & Summary Analysis
