
# Day 8 — Descriptive Statistics in Pandas

60-Day Data Science Roadmap | Phase 1 — Math + Core Tools
Status: Complete

---

## Topic

Descriptive Statistics in Pandas — how to instantly understand
any dataset using summary functions before doing any analysis.

---

## What I Learned

Concept 1 — df.describe()
One command that gives count, mean, std, min, max,
and percentiles for all numeric columns at once.

Concept 2 — mean(), min(), max()
Pull one specific number from a column instead of
the full summary.

Concept 3 — median() vs mean()
median() = middle value when data is sorted
std()    = how spread out values are from the average
Key rule: when extreme values exist, use median not mean.

Concept 4 — value_counts()
Counts how many times each unique value appears.
Used for text columns where describe() does not work.

Concept 5 — isnull().sum()
Detects missing values column by column.
Always run this before starting any analysis.

Concept 6 — df.info()
Shows column names, data types, and non-null counts.
Always the first command to run on any new dataset.

---

## Key Rules

1. describe() only works on numeric columns
2. Use median over mean when extreme values exist
3. Always run df.info() first on any new dataset
4. value_counts() is for text columns
5. Always run isnull().sum() before any analysis
6. Pandas calls text columns "object" not "string"

---

## Files in This Folder

Day08_Notes.md       — full concept notes with code and output
Day08_Tasks.py       — all 7 practice tasks with my solutions

---

## Practice Tasks Completed

Task 1 — df.describe() on custom DataFrame         done
Task 2 — mean(), min(), max() individually          done
Task 3 — median vs mean with extreme value          done
Task 4 — value_counts() on text column              done
Task 5 — isnull().sum() to detect missing values    done
Task 6 — df.info() reading and interpretation       done
Task 7 — full mini summary using all 6 concepts     done

---



---

## Previous Day

Day 7 — Feature Creation · Apply Functions

## Next Day

Day 9 — Matplotlib Basics · Line Plots · Histograms

---

60 days. 4 phases. 3 projects. 1 goal — get hired.
