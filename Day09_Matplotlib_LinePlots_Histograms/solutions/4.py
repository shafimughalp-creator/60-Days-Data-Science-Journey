

# 🔵 CONCEPT 4 — Histogram (Basic)
# 🧠 Real-Life Analogy
# 100 students took an exam. You want to know — how many scored 50–60? How many scored 80–90? 
# Reading 100 numbers is painful. A histogram groups the scores into buckets and draws a bar for each bucket. 
# Taller bar = more students in that range. You instantly see where most people scored.


# Key difference from line plot:

# Line plot → shows change over time
# Histogram → shows how data is distributed


import matplotlib.pyplot as plt 

scores = [45, 55, 60, 62, 65, 65, 70, 72, 75, 75,
          78, 80, 80, 82, 85, 85, 88, 90, 92, 95]

plt.hist(scores)
plt.show()

