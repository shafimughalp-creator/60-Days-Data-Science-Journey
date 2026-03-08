
# 📊 Day 2 — Standard Deviation, Correlation & NumPy Operations

# 1️⃣ Standard Deviation

# Standard deviation measures how spread out the data is from the mean.

# If the values are close to the mean → Low standard deviation
# If the values are far from the mean → High standard deviation

# FIRST FINDING MEAN 

import numpy as np 

data = np.array([10,20,30])

print("MEAN = " , np.mean(data))

# NOW STANDARD DEVIATION 

print("STANDARD DEVIATION = ", np.std(data))

# 📊 Interpretation
#The standard deviation is small, which means the values are close to the mean.


# 2️⃣ Understanding Data Spread

import numpy as np 

# COMPARING 2 DATASETS 

A = np.array([10,11,12,13,14,15])
print("STANDARD DEVIATION =" ,np.std(A))

# Values are close together → low spread

B = np.array([2,10,20,32,45])
print("STANDARD DEVIATION OF B = " ,np.std(B))

# Values are far apart → high spread


# 3️⃣ Correlation
# What is Correlation?

# Correlation measures how two variables move together

import numpy as np 

study_hours = np.array([1,2,3,4,5])
scores = np.array([40,50,60,70,80])

Correlation = np.corrcoef( study_hours , scores )

print("Correlation Matrix : ")
print(Correlation)

# The value 1 means perfect positive correlation.


# 4️⃣ NumPy Array Operations

# NumPy allows fast mathematical operations on arrays

import numpy as np 

a = np.array([1,2,3])
b = np.array([4,5,6])

# ADDITION 
print( a + b )

# MULTIPLICATION 
print( a * b )

# DIVISION 
print( a/b )


# 5️⃣ NumPy Broadcasting
# What is Broadcasting?

# Broadcasting allows NumPy to apply operations between 
# arrays of different sizes automatically.

import numpy as np 

a = np.array([1,2,3])
print( a + 10 )

# NumPy adds 10 to every element automatically.
# OUTPUT = [11 12 13]

# ANOTHER EXAMPLE 
a = np.array([1,2,3])
b = 5 

print( a * 5 )
# OUTPUT = [5 10 15]


# REAL LIFE DATA SCIENCE EXAMPLE 


import numpy as np 

# SALES DATA 
sales = np.array([200,220,250,260,300])

# PROMOTION DATA ( # 1 = PROMOTION AND 0 = NO PROMOTION )
promotion = np.array([1,0,1,0,1])

# STANDARD DEVIATION OF SALES 
print("STANDARD DEVIATION = " , np.std(sales))

# CORRELATION STATUS 
print("CORRELATION MATRIX  :")
print(np.corrcoef( sales , promotion ))


# 💻 Mini Practice
import numpy as np

data = np.array([5,7,9,11,13])

# 1 Print mean

# 2 Print standard deviation

# 3 Add 5 to all elements

# 4 Multiply all elements by 2

print("MEAN = " , np.mean(data))

print("STANDARD DEVIATION = " , np.std(data))

print( data + 5 )

b = 2 
print( data * b)


# Mini Practice — NumPy Basics

# Concepts practiced:
# • Mean
# • Standard Deviation
# • Array operations
# • Broadcasting



# CONCEPTUAL QUESTIONS FOR TODAY

# Q1
# Which dataset has higher standard deviation?

# Dataset A = [10,11,12,13,14]
# Dataset B = [2,10,20,30,50]

# Answer:

# Dataset B has the higher standard deviation.

# Explanation:
# The values in Dataset B are much more spread out compared to Dataset A.
# They are far from the mean and vary greatly.

# Dataset A values are close to each other and close to the mean,
# so its standard deviation is small.

# Dataset B contains values that are widely spread,
# which increases the standard deviation.




# Q2
# If correlation between two variables is -0.9, what does it mean?

# A) Strong positive
# B) Strong negative
# C) No relation

# Answer: B) Strong negative

# Explanation:
# A correlation value of -0.9 indicates a strong negative relationship
# between the two variables.

# This means when one variable increases, the other variable tends
# to decrease significantly.

# The closer the correlation value is to -1, the stronger the
# negative relationship between the variables.




# Q3
# Study hours increase and exam scores increase.
# What type of correlation?

# Answer: Positive Correlation

# Explanation:
# When study hours increase, exam scores also increase.
# This means both variables move in the same direction.

# Therefore, this is a positive correlation.

# In a correlation matrix, the value will be close to +1
# if the relationship is very strong.





# Q4
# If standard deviation is very small, what does it say about the dataset?

# Answer:

# If the standard deviation is very small, it means the data points
# are very close to the mean (average value).

# This indicates that the dataset has low variability and the
# values are tightly clustered around the mean.




# Q5
# Dataset

import numpy as np

dataset = np.array([100,105,98,102,500])

# Calculate standard deviation
print("Standard Deviation:", np.std(dataset))

# Explanation:
# Yes, there is likely an outlier in this dataset.
# The value 500 is extremely large compared to the other values,
# which are around 100.

# Because of this large difference, the dataset becomes highly spread out.
# This increases the standard deviation significantly.

# Therefore, 500 is likely an outlier.
