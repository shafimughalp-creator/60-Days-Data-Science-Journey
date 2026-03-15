
# PRACTICE QUESTIONS 

import pandas as pd
import numpy as np

data = {
    'student': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'math': [78, 92, 55, 88, 70],
    'english': [85, 76, 60, 95, 65],
    'attendance': [90, 95, 60, 88, 72]
}

df = pd.DataFrame(data)

#
import pandas as pd
import numpy as np

data = {
    'student': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Usman'],
    'math': [78, 92, 55, 88, 70],
    'english': [85, 76, 60, 95, 65],
    'attendance': [90, 95, 60, 88, 72]
}

df = pd.DataFrame(data)

# Task 1 — total_marks
df['total_marks'] = df['math'] + df['english']

# Task 2 — average
df['average'] = df['total_marks'] / 2

# Task 3 — grade using apply()
df['grade'] = df['average'].apply(lambda x: 'A' if x >= 85 else 'B' if x >= 70 else 'C')

# Task 4 — passed using np.where()
df['passed'] = np.where(df['attendance'] >= 75, True, False)

# Task 5 — attendance_group using pd.cut()
df['attendance_group'] = pd.cut(
    df['attendance'],
    bins=[0, 60, 80, 100],
    labels=['Low', 'Average', 'High']
)

# Task 6 — filter passed AND grade A or B
result = df[(df['passed'] == True) & (df['grade'].isin(['A', 'B']))]
print(result)


#**Expected output for Task 6:**
#```
#  student  math  english  total_marks  average grade  passed attendance_group
# 0     Ali    78       85          163     81.5     B    True            High
# 1    Sara    92       76          168     84.0     B    True            High
# 3  Fatima    88       95          183     91.5     A    True            High
