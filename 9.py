

import pandas as pd

# ADDING SCORE COLOUMN AND DROPPING IT 

# Step 1: Create the DataFrame
data = {
    "Name": ["Ali", "Sara", "John", "Mia", "Tom"],
    "Age": [25, 30, 22, 35, 28],
    "City": ["Dubai", "London", "Paris", "NY", "Berlin"]
}

df = pd.DataFrame(data)
print("=== Original DataFrame ===")
print(df)

# Step 2: Add a "Score" column
df["Score"] = [88, 92, 75, 95, 80]
print("\n=== After Adding Score Column ===")
print(df)

# Step 3: Drop the "Score" column
df = df.drop("Score", axis=1)
print("\n=== After Dropping Score Column ===")
print(df)

# axis = 1 means left to right 
# axis = 0 means top to bottom 