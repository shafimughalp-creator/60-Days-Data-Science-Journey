
# Q2. Plot a histogram of these ages:
# [22, 25, 25, 28, 30, 30, 30, 35, 38, 40, 40, 45, 50, 55, 60]
# No customization — just plt.hist() and plt.show().

import matplotlib.pyplot as plt 

ages = [22, 25, 25, 28, 30, 30, 30, 35, 38, 40, 40, 45, 50, 55, 60]

plt.hist(ages)
plt.show()

# Q3. What happens if you run plt.show() without calling plt.plot() first? Try it and write what you see.

# Observation 
# No diagram appears 