
# Generate 1000 normal distribution numbers and plot a histogram.

import numpy as np 
import matplotlib.pyplot as plt 

data = np.random.normal(0,1,1000)

plt.hist(data)

plt.title("1000 NORMAL DISTRIBUTION")

plt.show()