

# Q12. You have this DataFrame:

# Name     Score
# Ali      85
# Sara     NaN
# Ahmed    90
# Fatima   NaN


# Write code to fill missing values with the mean score.

import pandas as pd 
import numpy as np 


data = pd.DataFrame({
    "Name" : ["Ali","Sara","Ahmed","Fatima"] ,
    "Scores" : [85,np.nan,90,np.nan]
})

data["Scores"] = data["Scores"].fillna(data["Scores"].mean())

print(data)

# Q13. What is the difference between groupby() and agg()?
#  Give one example of using both together.

group_agg = data.groupby("Name").agg({
    "Scores" : ["min","max","sum"]
})

print(group_agg)
# by using this example we can select the student "NAME" by groupby 
# by agg() we can tell the maximum , minimum , sum of student scores 

