
# ## 💡 SECTION 4 — Concept Understanding (All Days)

# **Q21.** What is the difference between a Pandas Series and a DataFrame?

# **Q22.** If a dataset has high variance what does that tell you?

# **Q23.** Why is feature engineering important in data science?

# **Q24.** When should you use np.where() instead of apply()? Why?

# **Q25.** You have a dataset with missing values in a salary column. 
# What are 3 ways to handle them? Which would you choose and why?




# # **Q21.** What is the difference between a Pandas Series and a DataFrame?

#Series = one column only (1D)
#DataFrame = multiple rows and columns (2D table)

# A DataFrame is made up of multiple Series. 



# **Q22.** If a dataset has high variance what does that tell you?

# high variance means the data is inordered 
# its value is far from mean 



# **Q23.** Why is feature engineering important in data science?

# Feature engineering creates new useful columns from existing data.
# It gives the model more meaningful information to learn from.
# Example: extracting month from a date column helps predict seasonal sales



# # **Q24.** When should you use np.where() instead of apply()? Why?
# in one word use np.where when we want to use boolean conditions 
# and apply if we want to see data in numeric or in number form 




#  **Q25.** You have a dataset with missing values in a salary column. 
# What are 3 ways to handle them? Which would you choose and why?

# 1. fillna(mean) — fill with average value
# 2. dropna() — remove rows with missing values
# 3. fillna(median) — fill with median (better for outliers)