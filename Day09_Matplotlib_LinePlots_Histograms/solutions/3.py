

# 🔵 CONCEPT 3 — Customizing a Line Plot

# 🧠 Real-Life Analogy

# A plain chart with no title and no labels is like handing someone a document with no heading.
#  They don't know what they're looking at. Adding a title, axis labels, color, and a grid is like putting proper headings on your report 
# — it makes it professional and readable.

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
sales = [100, 120, 90, 150, 130, 170, 160]

plt.plot( days , sales , color = "blue" , linewidth = 2 , marker = 'o')
plt.title("Weekly sales")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.grid(True)
plt.show()

