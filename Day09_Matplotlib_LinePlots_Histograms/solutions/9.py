

# Q5. Plot the age histogram from Q2 but now add:

# bins=5
# color='purple'
# edgecolor='white'
# Title: "Age Distribution"
# X label: "Age"
# Y label: "Count"

import matplotlib.pyplot as plt 

ages = [22, 25, 25, 28, 30, 30, 30, 35, 38, 40, 40, 45, 50, 55, 60]

plt.hist(ages , bins=5 , color='purple' , edgecolor = 'white')

plt.title("Age Distribution")

plt.xlabel("Age")
plt.ylabel("Count")

plt.show()



