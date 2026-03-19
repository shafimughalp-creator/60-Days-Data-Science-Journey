

# 🔴 LEVEL 3 — Thinking Questions (Understand, don't just copy)
# Q7. You have this data:
# [10, 10, 10, 10, 50, 50, 90, 90, 90, 90, 90]

# First plot with bins=3
# Then plot with bins=10
# Write in words: what story does each chart tell? Which is more useful?

import matplotlib.pyplot as plt 

marks = [10, 10, 10, 10, 50, 50, 90, 90, 90, 90, 90]

plt.hist( marks , bins=3 , color="blue" , edgecolor = "black")

plt.show()

# bins=3 → Shows 3 broad buckets: low (10s), mid (50s), high (90s). You see the pattern but lose exact counts.
# bins=10 → Shows each value separately. You clearly see 4 people scored 10, 2 scored 50, 5 scored 90.
