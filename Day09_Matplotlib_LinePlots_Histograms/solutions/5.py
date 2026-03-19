

# 🔵 CONCEPT 5 — Customizing a Histogram
# 🧠 Real-Life Analogy
# By default, Matplotlib chooses bucket sizes automatically. But sometimes automatic isn't what you need.
#  Imagine sorting mangoes by weight — you might want buckets every 10g for precision, or every 100g for a broad overview.
#  bins gives you that control. More bins = more detail. Fewer bins = broader picture.

import matplotlib.pyplot as plt 

scores = [45, 55, 60, 62, 65, 65, 70, 72, 75, 75,
          78, 80, 80, 82, 85, 85, 88, 90, 92, 95]

plt.hist( scores , bins=5 , color = 'orange' , edgecolor = 'black')
plt.title("Student Score Distributions")

plt.xlabel("Score")
plt.ylabel("Number of Student")
plt.show()