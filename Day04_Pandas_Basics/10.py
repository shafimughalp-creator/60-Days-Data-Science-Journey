

# 🔷 Practice Task for Day 4

# Create a DataFrame with 5 people — columns: Name, Age, Score
# Use .head(), .info(), .describe() on it
# Select only the "Name" column
# Use .loc to get row 2, column "Score"
# Use .iloc to get the first 3 rows, first 2 columns
# Add a new column called "Passed" with True/False values
# Drop the "Passed" column

import pandas as pd 

# # Create a DataFrame with 5 people — columns: Name, Age, Score
data = {
    "Name" : ["SHAFI","ALI","SHAFAY","ADNAN","ALIYAN"] ,
    "Age" : [18,19,20,21,22] ,
    "Score" : [90,92,94,96,100]
}

DATA_FRAME = pd.DataFrame(data)
print(DATA_FRAME)

# Use .head(), .info(), .describe() on it

print(DATA_FRAME.head()) 

print(DATA_FRAME.info())

print(DATA_FRAME.describe())

# Select only the "Name" column

print(DATA_FRAME["Name"])

# Use .loc to get row 2, column "Score"
print(DATA_FRAME.loc[2 , "Score"])


# # Use .iloc to get the first 3 rows, first 2 columns

print(DATA_FRAME.iloc[0:3 , 0:2])

# # Add a new column called "Passed" with True/False values
DATA_FRAME["Passed"] = [True,False,True,False,True]
print(DATA_FRAME)

# # Drop the "Passed" column
dropped =   DATA_FRAME.drop("Passed",axis = 1 )
print(dropped)