
# Day 11 — Seaborn Visualization

> Part of my 60-Day Data Science Roadmap | Phase 1: Math + Core Tools

---

## What This Covers

This notebook covers Day 11 of my data science learning journey — Seaborn basics, distribution plots, and correlation heatmaps.

---

## Concepts Practiced

**1. Seaborn Introduction**
- What Seaborn is and how it differs from Matplotlib
- Why data scientists prefer it for quick visual analysis

**2. Distribution Plot**
- Visualizing how values are spread across a dataset
- Using `histplot` with KDE (smooth curve) enabled and disabled
- Reading the shape of data

**3. Correlation Heatmap**
- Building a correlation matrix using `df.corr()`
- Visualizing it with `sns.heatmap()`
- Reading correlation values and color mapping
- Understanding which columns have strong, weak, or no relationships

---

## Libraries Used

- `seaborn`
- `matplotlib`
- `pandas`

---

## Key Code Snippets

**Distribution Plot:**
```python
sns.histplot(data, kde=True)
plt.title("Distribution")
plt.show()
```

**Correlation Heatmap:**
```python
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.show()
```

---

## What I Learned

- Seaborn produces cleaner charts with less code compared to plain Matplotlib
- `kde=True` adds a smooth curve that shows the overall shape of data
- A correlation heatmap instantly shows which columns are related — no need to read raw numbers
- Shoe size and exam scores have zero correlation (obviously!) — this is a good sanity check for understanding the tool

---

## Progress

| Day | Topic | Status |
|-----|-------|--------|
| Day 9 | Matplotlib basics, line plots, histograms | Done |
| Day 10 | Boxplots, scatter plots, outliers | Done |
| **Day 11** | **Seaborn, heatmaps, distribution plots** | **Done** |
| Day 12 | Correlation matrix + full EDA on real data | Up Next |

---

## Roadmap

This is part of a focused 60-day plan to become a junior data scientist:

- **Phase 1 (Days 1–14):** Math + Core Tools (NumPy, Pandas, Matplotlib, Seaborn)
- **Phase 2 (Days 15–25):** SQL + Data Workflow
- **Phase 3 (Days 26–45):** Machine Learning Core
- **Phase 4 (Days 46–60):** Portfolio Projects

---

*Self-taught. Consistent. Building in public.*
