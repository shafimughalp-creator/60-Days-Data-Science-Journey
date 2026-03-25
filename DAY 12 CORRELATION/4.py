
# ✅ Task 2

import pandas as pd 

data = {
    "Study": [1, 2, 3, 4, 5],
    "Marks": [35, 45, 55, 65, 75]
}

# 👉 Do:
# Find correlation
# ❓ Question:
# What value do you get?
# What does it mean?

df = pd.DataFrame(data)

print(df.corr())

# all are positive because more study = more marks 


