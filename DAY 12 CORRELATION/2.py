
# CORRELATION MATRIX

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


data = {
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000],
    "Experience": [1, 3, 5, 7, 9]
}

df = pd.DataFrame(data)

# Basic EDA

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.corr())

sns.heatmap(df.corr(),annot=True)

plt.show()







