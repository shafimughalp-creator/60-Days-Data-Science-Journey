

# 🟡 LEVEL 2 — Customization (Apply what you learned)
# Q4. Plot the same temperature chart from Q1 but now add:

# Title: "5 Day Temperature Report"
# X label: "Day"
# Y label: "Temperature (C)"
# Color: red
# Marker: o
# Grid: on

import matplotlib.pyplot as plt 

Days = [1,2,3,4,5]

Temps = [30,32,28,35,33]

plt.plot(Days , Temps , color = "red" , marker = 'o')
plt.grid(True)

plt.title("5 day temprature report")
plt.xlabel("Day")
plt.ylabel("Temps")

plt.show()

