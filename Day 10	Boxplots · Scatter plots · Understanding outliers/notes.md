# Day 10 — Boxplots, Scatter Plots & Outliers

## What I Learned

Today I learned how to visualize data distributions and relationships
using Matplotlib, and how to detect outliers using the IQR method.

---

## 1. Boxplot

A boxplot shows the distribution of data using 5 key values:
minimum, Q1, median, Q3, and maximum.
Values outside the whiskers are outliers.

import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 98]

plt.figure(figsize=(6, 4))
plt.boxplot(scores)
plt.title("Student Scores")
plt.ylabel("Scores")
plt.show()

What each part means:
- plt.figure(figsize=(6, 4))  →  creates a blank canvas, 6 wide and 4 tall
- plt.boxplot(scores)         →  draws the boxplot using the data
- plt.title("...")            →  adds a title at the top
- plt.ylabel("...")           →  labels the vertical axis
- plt.show()                  →  displays the plot

What to look for in the output:
- The box          =  middle 50% of data
- Line inside box  =  median
- The whiskers     =  spread beyond the box
- Dots outside     =  outliers

---

## 2. Scatter Plot

A scatter plot shows the relationship between two variables
by placing dots on a graph.

import matplotlib.pyplot as plt

hours  = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]
scores = [45, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 98]

plt.figure(figsize=(7, 5))
plt.scatter(hours, scores, color='steelblue', s=80)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()

What each part means:
- plt.scatter(x, y)       →  first list = X axis, second list = Y axis
- color='steelblue'       →  color of the dots
- s=80                    →  size of the dots
- plt.grid(True)          →  adds background grid lines

3 patterns to recognize:
- Dots go up-right    →  positive relationship (more X = more Y)
- Dots go down-right  →  negative relationship (more X = less Y)
- Random dots         →  no relationship

---

## 3. Outlier Detection — IQR Method

The IQR method uses a fence system to find values that are
too far from the rest of the data.

import numpy as np

scores = [45, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 98]

Q1 = np.percentile(scores, 25)
Q3 = np.percentile(scores, 75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

for x in scores:
    if x < lower or x > upper:
        print(x, "is an outlier")

What each part means:
- np.percentile(scores, 25)  →  finds Q1 (value at 25% mark)
- np.percentile(scores, 75)  →  finds Q3 (value at 75% mark)
- IQR = Q3 - Q1              →  spread of the middle 50% of data
- lower = Q1 - 1.5 * IQR    →  left side of the fence
- upper = Q3 + 1.5 * IQR    →  right side of the fence
- 1.5 is a fixed rule        →  always use 1.5, never change it

Output:
98 is an outlier

---

## Key Syntax Rules

plt.title("...")   →  always a string in quotes, never a list
plt.xlabel("...")  →  always a string in quotes, never a list
plt.ylabel("...")  →  always a string in quotes, never a list
plt.scatter(x, y)  →  cause/hours goes first, effect/scores goes second
plt.show()         →  always end with this, without it nothing appears

---

## Mistakes I Made and Fixed

WRONG  →  plt.ylabel(scores)         passed a list
RIGHT  →  plt.ylabel("Scores")       use text in quotes

WRONG  →  plt.scatter(scores, hours) swapped X and Y
RIGHT  →  plt.scatter(hours, scores) cause first, effect second

---

## Summary

- Boxplot      =  shows data spread and outliers visually
- Scatter plot =  shows relationship between two variables
- IQR method   =  finds outliers using math (fence system)
- All three are used together in real data science projects
