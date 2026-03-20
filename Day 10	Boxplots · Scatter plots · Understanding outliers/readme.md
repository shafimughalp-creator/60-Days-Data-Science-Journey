# Day 10 — Boxplots, Scatter Plots & Outlier Detection

Part of my 60-Day Data Science Journey | Phase 1: Math + Core Tools

---

## Topics Covered

- Boxplots — visualizing data distribution
- Scatter plots — visualizing relationships between variables
- Outlier detection — IQR method

---

## Files

day10_boxplot.py   →  Boxplot using Matplotlib
day10_scatter.py   →  Scatter plot using Matplotlib
day10_outliers.py  →  IQR outlier detection using NumPy
notes.md           →  Concept notes with code explanations

---

## Key Concepts

Boxplot:
Visualizes distribution using 5 values: min, Q1, median, Q3, max.
Dots outside the whiskers are outliers.
    plt.boxplot(scores)

Scatter Plot:
Shows relationship between two variables.
Dots going up-right = positive relationship.
    plt.scatter(hours, scores)

IQR Outlier Detection:
Uses a fence system. Anything outside the boundaries is an outlier.
    Q1    = np.percentile(data, 25)
    Q3    = np.percentile(data, 75)
    IQR   = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

---

## Tools Used

- Python
- Matplotlib
- NumPy

---

## Progress

Phase 1 — Math + Core Tools     Day 1–14   In Progress
Phase 2 — SQL + Data Workflow   Day 15–27  Upcoming
Phase 3 — Machine Learning      Day 28–45  Upcoming
Phase 4 — Portfolio Projects    Day 46–60  Upcoming

---

60 days. 4 phases. 3 projects. 1 goal — get hired.
