


#  🟡 LEVEL 2 — Correlation Matrix
#  ✅ Task 3


import pandas as pd 

import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Age": [18, 20, 22, 24, 26],
    "Salary": [15000, 20000, 25000, 30000, 35000],
    "Experience": [0, 1, 2, 3, 4],
    "IQ" : [5, 1, 8, 3, 7]
}

df = pd.DataFrame(data)



# ❓ Question:
# Which 2 columns are most related?
# Why do you think that is?

# i believe salary and experience is the most related ones 
# more experience = more salary



print(df.corr())

# ❓ Question:
# Which column has weakest correlation now?

# THE IQ one has weakest correlation now because of random numbers 
# no symmetry

# 🔵 LEVEL 3 — Heatmap Practice
# ✅ Task 5

sns.heatmap(df.corr(), annot=True)
plt.show()

sns.heatmap(df.corr())
plt.show()

# Question:
# Which color shows strong correlation?
# Which shows weak?

# white shows the strongest correlation 
# black shows the weakest correlation

# Question:
# Which version is easier to understand? Why?

# the one with numbers on it is easier to understand 

