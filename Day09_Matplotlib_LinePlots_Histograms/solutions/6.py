
# 📅 Day 9 — Practice Questions

# 🟢 LEVEL 1 — Basic (Just run and observe)
# Q1. Import Matplotlib and plot a line chart of temperatures for 5 days:
# Days: [1, 2, 3, 4, 5]
# Temps: [30, 32, 28, 35, 33]
# Just plt.plot() and plt.show() — no customization yet.

import matplotlib.pyplot as plt 

Days = [1,2,3,4,5]

Temps = [30,32,28,35,33]

plt.plot(Days , Temps)

plt.xlabel("Days")
plt.ylabel("Temps")
plt.show()

