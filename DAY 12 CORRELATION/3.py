

# 🧪 🔥 DAY 12 — FULL PRACTICE SET

import pandas as pd

data = {
    "Exercise": [10, 20, 30, 40, 50],
    "Weight": [90, 85, 80, 75, 70]
}

# 👉 Do:
# Create DataFrame
# Run .corr()
# ❓ Question:
# Is correlation positive or negative?
# Why?

df = pd.DataFrame(data)

print(df.corr())

# the correlation is both positive and negative 
# at first less exerice is more weight 
# then more exercise helps in lesser or balanced weight

