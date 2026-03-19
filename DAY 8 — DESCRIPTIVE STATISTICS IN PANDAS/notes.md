

DAY 8 — DESCRIPTIVE STATISTICS IN PANDAS
60-Day Data Science Roadmap | Phase 1 | Math + Core Tools
==========================================================

WHAT PROBLEM DOES THIS SOLVE?
When you get a dataset with thousands of rows, you cannot read every value.
Descriptive statistics gives you an instant summary in seconds.

----------------------------------------------------------
CONCEPT 1 — df.describe()
----------------------------------------------------------

One command that summarizes all numeric columns at once.

CODE:
import pandas as pd

data = {
    'Name':  ['Ali', 'Sara', 'Umar', 'Zara', 'Bilal'],
    'Score': [85, 92, 78, 95, 60],
    'Age':   [20, 22, 21, 23, 19]
}

df = pd.DataFrame(data)
print(df.describe())

OUTPUT:
           Score        Age
count   5.000000   5.000000
mean   82.000000  21.000000
std    13.341664   1.581139
min    60.000000  19.000000
25%    78.000000  20.000000
50%    85.000000  21.000000
75%    92.000000  22.000000
max    95.000000  23.000000

WHAT EACH ROW MEANS:
count  = Total non-missing values
mean   = Average of all values
std    = How spread out the values are
min    = Lowest value
25%    = 25% of values fall below this
50%    = Middle value (median)
75%    = 75% of values fall below this
max    = Highest value

NOTE: Text columns like Name are not shown.
      describe() only works on numeric columns.

----------------------------------------------------------
CONCEPT 2 — mean(), min(), max()
----------------------------------------------------------

Pull one specific number instead of the full summary.

CODE:
print(df['Score'].mean())   # Average
print(df['Score'].min())    # Lowest
print(df['Score'].max())    # Highest

OUTPUT:
82.0
60
95

SYNTAX:
df['Score'].mean()
↑    ↑        ↑
table column  calculation

----------------------------------------------------------
CONCEPT 3 — median() and std()
----------------------------------------------------------

median() = the middle value when data is sorted
std()    = how far values typically are from the average

CODE:
print(df['Score'].median())
print(df['Score'].std())

OUTPUT:
85.0
13.341664064126335

KEY RULE:
When extreme values exist, use median instead of mean.
Example: if one student scored 5 and four scored 80,
mean drops to 65 — but median stays near 80.
Median is more honest.

----------------------------------------------------------
CONCEPT 4 — value_counts()
----------------------------------------------------------

Counts how many times each value appears.
Used for text columns where describe() does not work.

CODE:
data2 = {
    'City': ['Lahore', 'Karachi', 'Lahore', 'Islamabad', 'Lahore', 'Karachi']
}

df2 = pd.DataFrame(data2)
print(df2['City'].value_counts())

OUTPUT:
Lahore       3
Karachi      2
Islamabad    1

----------------------------------------------------------
CONCEPT 5 — isnull().sum()
----------------------------------------------------------

Finds which columns have missing values and how many.

CODE:
data3 = {
    'Name':  ['Ali', 'Sara', None, 'Zara'],
    'Score': [85, None, 78, 95],
    'Age':   [20, 22, 21, 23]
}

df3 = pd.DataFrame(data3)
print(df3.isnull().sum())

OUTPUT:
Name     1
Score    1
Age      0

SYNTAX:
df3.isnull().sum()
    ↑           ↑
mark empty    count them

----------------------------------------------------------
CONCEPT 6 — df.info()
----------------------------------------------------------

Shows column names, data types, and non-null counts.
Always run this FIRST when you open any new dataset.

CODE:
print(df3.info())

OUTPUT:
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
 0   Name    3 non-null      object
 1   Score   3 non-null      float64
 2   Age     4 non-null      int64

WHAT DTYPE MEANS:
object  = text column
int64   = whole numbers
float64 = decimal numbers

NOTE: Pandas calls text columns "object" not "string".
      Same thing, different name.

----------------------------------------------------------
KEY RULES TO REMEMBER
----------------------------------------------------------

1. describe() only works on numeric columns
2. Use median over mean when extreme values exist
3. Always run df.info() first on any new dataset
4. value_counts() is for text columns
5. Always run isnull().sum() before any analysis

==========================================================
NEXT: Day 9 — Matplotlib Basics · Line Plots · Histograms
==========================================================
