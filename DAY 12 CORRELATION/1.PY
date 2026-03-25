

# 🧠 DAY 12 — Correlation Matrix + Basic EDA + Heatmap

import pandas as pd

data = {
    "Hours_Study": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80]
}

df = pd.DataFrame(data)

print(df.corr())