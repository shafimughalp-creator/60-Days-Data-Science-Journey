
# Q2. Calculate variance manually for this dataset:


data = [2, 4, 6]

mean = sum(data)/len(data)

variance = sum(( x - mean)** 2 for x in data)/len(data)

print("Mean : " , mean)

print("Variance : " , variance)




