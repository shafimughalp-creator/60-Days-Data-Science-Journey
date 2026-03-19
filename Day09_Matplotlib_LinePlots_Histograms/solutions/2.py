

# 🔵 CONCEPT 2 — Line Plot (Basic)
# 🧠 Real-Life Analogy
# You have sales numbers for 7 days. You could stare at the numbers — or you draw a line and instantly see 
# "sales went up Wednesday, dropped Friday." A line plot shows change over time. 
# Your brain reads a line in 1 second. Numbers take 10 seconds.

import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

sales = [100,150,200,250,300,350,400]

plt.plot( days , sales )

plt.show()


