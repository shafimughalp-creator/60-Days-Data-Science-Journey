

# **Q17.** Write a lambda function using apply() that labels a score column:
# - A if score >= 85
# - B if score >= 70
# - C if below 70

import pandas as pd 

data = pd.DataFrame({
    "scores" : [60,70,80,90,85]
})

grades = data["scores"].apply(lambda x : "A" if x >= 85 else "B" if x >= 70 else "C")
print(grades)

