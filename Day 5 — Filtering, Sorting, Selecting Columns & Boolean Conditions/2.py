
## 🧠 Practice Questions

# Try these before uploading to GitHub.

# **Q1** — Select only the `Name` and `City` columns from the DataFrame.

# **Q2** — Filter all people aged 25 or above.

# **Q3** — Filter people from Karachi OR Multan.

# **Q4** — Filter people with Salary between 45000 and 65000 (use `&`).

# **Q5** — Sort the DataFrame by Age from oldest to youngest.

# **Q6 (Challenge)** — Filter people with Salary > 50000, select only Name and
#  Salary, sort by Salary descending. Do it in one line



import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Zara'],
    'Age': [25, 30, 22, 28],
    'Salary': [50000, 70000, 45000, 60000],
    'City': ['Lahore', 'Karachi', 'Islamabad', 'Multan']
}

df = pd.DataFrame(data)

# **Q1** — Select only the `Name` and `City` columns from the DataFrame.
print(df[["Name","City"]])

# **Q2** — Filter all people aged 25 or above.
print(df[df["Age"] >= 25] )

# **Q3** — Filter people from Karachi OR Multan.
filtering_city = df[(df["City"] == "Karachi" ) | (df['City'] == "Multan")]
print(filtering_city)

# # **Q4** — Filter people with Salary between 45000 and 65000 (use `&`).
filtering_salary = df[(df["Salary"] >= 45000 ) & (df["Salary"] <= 65000)]
print(filtering_salary)

# **Q5** — Sort the DataFrame by Age from oldest to youngest.
sorting_data = df.sort_values("Age",ascending=False)
print(sorting_data)

# *Q6 (Challenge)** — Filter people with Salary > 50000, select only Name and
#  Salary, sort by Salary descending. Do it in one line

challenge = df[df["Salary"] > 50000][["Name","Salary"]].sort_values("Salary",ascending=False)
print(challenge)