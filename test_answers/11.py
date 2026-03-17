

# **Q15.** Create a profit column and profit_margin column from this data:


# sales = 2000
# cost = 1200

import pandas as pd 

data = pd.DataFrame({
    "Sales" : [2000] ,
    "Cost" : [1200]
})

data["profit"] = data["Sales"] - data["Cost"]

data["profit_margin"] = (data["profit"]/data["Sales"])*100

print(data)


