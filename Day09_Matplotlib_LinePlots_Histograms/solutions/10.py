

# Q6. Plot a line chart of monthly profits:
# Months: [1, 2, 3, 4, 5, 6]
# Profit: [2000, 1500, 3000, 2500, 4000, 3500]

# Color: green
# Linewidth: 3
# Marker: s
# Title: "Monthly Profit"
# Grid: on


import matplotlib.pyplot as plt 

Months = [1, 2, 3, 4, 5, 6]
Profit = [2000, 1500, 3000, 2500, 4000, 3500]

plt.plot( Months , Profit , color = "green" , linewidth = 3 , marker = "s")

plt.title("Monthly Profit")

plt.xlabel("Month")
plt.ylabel("Profit")

plt.grid(True)

plt.show()

