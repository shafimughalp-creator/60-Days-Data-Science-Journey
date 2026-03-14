# Day 06 — Full Concept Notes

---

## Topic 1 — Missing Values

### What is NaN?
NaN means Not a Number. It is simply a blank cell in your data.
It appears when someone did not fill in a field.
Nothing scary — just an empty space.

### Step 1 — Find the blanks

df.isnull()
Shows True or False for every cell.
True means blank. False means data exists.

df.isnull().sum()
Counts how many blanks are in each column.
Always use this — much more useful than staring at True and False.

Example output:
Name          0
Department    0
Salary        2
Age           2

### Step 2 — Remove the blanks

df.dropna()
Removes every row that has even one blank anywhere.
Very aggressive — use carefully.

df.dropna(subset=['Age'])
Removes only rows where Age is blank.
Ignores blanks in other columns.
Much safer in real projects.

df.dropna(how='all')
Only removes a row if every single cell in that row is blank.
Rarely needed but good to know.

### Step 3 — Fill the blanks

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
Fills blank Salary cells with the average salary.

df['Age'] = df['Age'].fillna(df['Age'].mean())
Fills blank Age cells with the average age.

df['Name'] = df['Name'].fillna('Unknown')
Fills blank text columns with a placeholder word.

### The only decision you make

Found a NaN. Now what?

Can I afford to lose this row?
    YES — dropna()   — delete the row
    NO  — fillna()   — fill the blank with mean or median

### Rule of thumb

Numeric columns  → fill with mean or median
Text columns     → fill with mode or Unknown

---

## Topic 2 — GroupBy

### What problem does it solve?

Without GroupBy you filter each group manually.
That is painful with 5 rows. Impossible with 50,000 rows.
GroupBy does it automatically in one line.

### Mental model — Split Apply Combine

Step 1 — SPLIT    — Put each row into its group folder
Step 2 — APPLY    — Calculate something inside each folder
Step 3 — COMBINE  — Show all results together in one table

### Basic syntax

df.groupby('Department')['Salary'].mean().reset_index()

Breaking it down:
df                       — your DataFrame
.groupby('Department')   — group by this column
['Salary']               — look at this column
.mean()                  — calculate this
.reset_index()           — make it a clean table

Read it like English:
In df, group by Department, look at Salary, find the mean.

### Other calculations

df.groupby('Department')['Salary'].sum()     — total salary
df.groupby('Department')['Salary'].max()     — highest salary
df.groupby('Department')['Salary'].min()     — lowest salary
df.groupby('Department')['Salary'].count()   — number of rows

### Why reset_index() matters

After groupby the grouped column becomes the index not a normal column.
reset_index() turns it back into a proper column.
Always use it for a clean readable table.

---

## Topic 3 — Aggregations

### What problem does it solve?

Instead of writing one line per calculation,
.agg() gets everything in one clean table.

### Single column multiple calculations

df.groupby('Department')['Salary'].agg(['mean', 'max', 'min', 'count'])

Pass a list of calculation names inside .agg()

### Multiple columns different calculations

df.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'Age':    ['mean', 'min'],
    'Name':   ['count']
}).reset_index()

Pass a dictionary — column name as key, list of calculations as value.

### value_counts

df['Department'].value_counts()

Counts how many times each unique value appears in a column.
Use it on the column you want to count groups of.

Example output:
HR         3
IT         2
Finance    2

---

## Full Workflow — The Right Order

Step 1 — Check for missing values
df.isnull().sum()

Step 2 — Fill missing values
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Age']    = df['Age'].fillna(df['Age'].mean())

Step 3 — Group and aggregate
result = df.groupby('Department').agg({
    'Salary': ['mean', 'max', 'count'],
    'Age':    ['mean']
}).reset_index()

Always clean first. Then analyze.
Never run groupby on dirty data.

---

## Common Mistakes

Mistake 1 — isnull() without .sum()
Wrong:   df.isnull()
Correct: df.isnull().sum()

Mistake 2 — Forgetting reset_index()
Wrong:   df.groupby('Department')['Salary'].mean()
Correct: df.groupby('Department')['Salary'].mean().reset_index()

Mistake 3 — Running groupby before fillna
Wrong:   groupby first then fillna
Correct: fillna first then groupby

Mistake 4 — value_counts on wrong column
Wrong:   df['Name'].value_counts()
Correct: df['Department'].value_counts()

---

## Key Takeaways

NaN is just a blank cell. Nothing scary.
Always check for missing values before any analysis.
dropna() is aggressive. Use subset to be specific.
fillna() with mean keeps your data intact.
GroupBy always follows Split Apply Combine.
.agg() saves you from writing 5 separate lines.
Always use reset_index() after groupby.
Clean first. Analyze second. Always.
