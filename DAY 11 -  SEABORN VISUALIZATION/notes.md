

# Day 11 — Seaborn Basics · Heatmaps · Distribution Plots

**Phase 1 — Math + Core Tools (60-Day Data Science Roadmap)**

---

## What is Seaborn?

Seaborn is a Python data visualization library built on top of Matplotlib. It produces beautiful, professional-looking charts with less code. Best used for quickly understanding relationships and distributions in data.

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

---

## Concept 1 — Distribution Plot (histplot)

Used to visualize how values in a column are distributed. Shows the shape of data — whether it's a bell curve, skewed, or spread out.

### Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

heights = [150, 155, 158, 160, 162, 163, 165, 165, 166, 168,
           170, 170, 171, 172, 173, 175, 175, 178, 180, 185]

sns.histplot(heights, kde=True)
plt.title("Distribution of Heights")
plt.xlabel("Height (cm)")
plt.show()
```

### Syntax Breakdown

| Part | What it does |
|---|---|
| `sns.histplot(data)` | Draws a histogram of the data |
| `kde=True` | Adds a smooth curve showing overall data shape |
| `kde=False` | Shows only the bars, no smooth curve |

### Key Points

- Tall bars = most values fall in that range
- Short bars at edges = fewer extreme values
- The smooth KDE curve shows the overall "shape" of your data
- Bell-shaped curve = data is normally distributed

---

## Concept 2 — Heatmap

Used to visualize a correlation matrix — shows how strongly columns in a DataFrame are related to each other. Color represents the strength and direction of the relationship.

### Code

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'study_hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'exam_score':  [40, 45, 55, 60, 65, 75, 80, 90],
    'absences':    [8, 7, 6, 5, 4, 3, 2, 1],
    'shoe_size':   [40, 42, 39, 41, 43, 40, 42, 41]
}

df = pd.DataFrame(data)
correlation = df.corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
```

### Syntax Breakdown

| Part | What it does |
|---|---|
| `df.corr()` | Calculates correlation between all columns automatically |
| `sns.heatmap(data)` | Draws the heatmap grid |
| `annot=True` | Shows the actual numbers inside each cell |
| `cmap='coolwarm'` | Color scheme — red = positive, blue = negative |

### Reading Correlation Values

| Value | Meaning |
|---|---|
| `1.0` | Perfect positive relationship (always a column with itself) |
| `0.7 to 0.99` | Strong positive — both go up together |
| `0.0` | No relationship |
| `-0.7 to -0.99` | Strong negative — one goes up, other goes down |
| `-1.0` | Perfect negative relationship |

### Key Insight from Example

- `study_hours` vs `exam_score` → **0.99** — very strong positive
- `absences` vs `exam_score` → **-0.99** — very strong negative
- `shoe_size` vs `exam_score` → **~0.07** — no relationship (as expected!)

---

## Quick Reference — Seaborn vs Matplotlib

| Task | Use |
|---|---|
| Distribution of one column | `sns.histplot()` |
| Relationship between columns | `sns.heatmap()` |
| Correlation matrix | `df.corr()` + `sns.heatmap()` |
| Basic line/scatter/histogram | `matplotlib.pyplot` |

---

## What's Next — Day 12

Day 12 combines everything learned in Days 9–11:
- Matplotlib (line plots, histograms, scatter, boxplots)
- Seaborn (histplot, heatmap)
- Applied to **real data** for a full beginner EDA (Exploratory Data Analysis)

---

*60-Day Data Science Roadmap · Phase 1 · Day 11*
