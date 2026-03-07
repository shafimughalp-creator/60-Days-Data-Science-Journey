

# MANUAL VARIANCE + MEAN 

data = [2,4,6]

Mean = sum(data)/len(data)

Variance = sum((x-Mean)**2 for x in data)/len(data)

print("MEAN = ",Mean)
print("VARIANCE = ",Variance)


# Using Numpy for it 

import numpy as np 

data = np.array([2,4,6])

print("MEAN = ",np.mean(data))
print("VARIANCE = ",np.var(data))



# ARRAY IN NUMPY 

import numpy as np 

data = np.array([2,4,6,8,10])
print(data)



# PRACTICE QUESTIONS 

# Q1

# Dataset:

# 5,10,15

# Find:

# Mean

# Variance

import numpy as np 


data = np.array([5,10,15])

print("MEAN = ",np.mean(data))
print("VARIANCE = ",np.var(data))




# Q2

# Which dataset has higher variance?

# A

# 4,5,6

# B

# 1,5,9

# Explain why.

import numpy as np 

data_A = np.array([4,5,6])

print("VARIANCE OF A = ",np.var(data_A))

data_B = np.array([1,5,9])

print("VARIANCE OF B = ",np.var(data_B))


# DATA_B HAS HIGHER VARIANCE BECAUSE ITS VALUES ARE MORE SPREAD OUT IN DATASET 
# SO BY SQUARING ITS DIFFRENCES THE VARIANCE BECOMES HIGHER 




# Q3

# Write Python code to calculate mean without NumPy

data = [1,2,3,4,5,6,7,8,9,10]

mean = sum(data)/len(data)

variance = sum((x - mean)** 2 for x in data)/len(data)

print("MEAN = ", mean)
print("VARIANCE = ", variance)




# Q4

# Using NumPy calculate:

# 10,20,30,40

# Find

# mean

# variance

import numpy as np 

data = np.array([10,20,30,40])

print("MEAN = ", np.mean(data))

print("VARIANCE =" , np.var(data))





# Q5 (Concept)

# If all numbers in dataset are multiplied by 3, what happens to:

# mean

# variance

# A DATA SET 

import numpy as np 

Data = np.array([1,2,3,4,5]) * 3 

print("MEAN = ", np.mean(Data))
# THE MEAN RESULT AUTOMATICALLY BECOMES MULTIPLE OF 3 
print("VARIANCE = " , np.var(Data))
# THE VARIANCE BECOMES LIKE (3)2 = 9 




# Q6 (Data Science Thinking)

#  Dataset
data = [100,102,101,99,98]

# Is variance likely:

# A) High
# B ) Low

# Explain.

# THE VARIANCE IS LIKELY LOW BECAUSE THE DATASET VALUES ARE NOT SPREAD OUT AND ARE MOST LIKELY CLOSE TO 
# EACH OTHER AND ARE CLOSER TO MEAN 
