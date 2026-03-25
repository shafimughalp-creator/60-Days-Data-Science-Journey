import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns

data = {
    "Study": [2, 4, 6, 8, 10],
    "Sleep": [8, 7, 6, 5, 4],
    "Marks": [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

print(df.head())
print(df.describe())
print(df.corr())

sns.heatmap(df.corr(),annot=True)

plt.show()

# Questions:
# Study vs Marks → ?
# Sleep vs Marks → ?
# Which factor affects marks more?

# more study = more marks 
# less sleep = more marks 

# more study affects more because it is logically the healthier way 

