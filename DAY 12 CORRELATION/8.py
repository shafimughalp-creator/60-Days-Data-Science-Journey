

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = {
    "Study": [2, 4, 6, 8, 10],
    "Sleep": [5, 6, 7, 8, 9],
    "Marks": [50, 55, 65, 60, 70]
}

df = pd.DataFrame(data)

sns.heatmap(df.corr(),annot=True)
plt.show()

# it is not 100 % perfect 
# it changed due to sleep hours 
