

# **Q19.** Write pd.cut() code to group ages into:
# - Young: 0–18
# - Adult: 18–35
# - Senior: 35+

import pandas as pd

data = pd.DataFrame({
    "age": [18, 35, 50]
})

data["age_group"] = pd.cut(
    data["age"],
    bins=[0, 18, 35, 100],
    labels=["Young", "Adult", "Senior"]
)

print(data)





