

# 🐼 SECTION 2 — Pandas Basics (Day 4–6)
# Q8. Create this DataFrame from scratch using a dictionary:

# Name     Age   City
# Ali      25    Lahore
# Sara     30    Karachi
# Ahmed    22    Islamabad

import pandas as pd 

data = pd.DataFrame({
    "Name" : ["Ali","Sara","Ahmed"] ,
    "Age" : [25,30,22] ,
    "City" : ["Lahore","Karachi","Islamabad"]
})

print(data)

# Q9. From the DataFrame above — how do you select only the Name and City columns?

print(data[["Name","City"]])


# Q10. How do you filter only rows where Age is greater than 23?

print(data[data["Age"] > 23])

# Q11. How do you sort the DataFrame by Age in descending order?
print(data["Age"].sort_values(ascending=False))

