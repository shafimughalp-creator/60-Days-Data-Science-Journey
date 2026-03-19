

# Q9. Plot two separate charts one after the other in the same script:

# First: line plot of sales [100, 200, 150, 300, 250] over 5 days
# Second: histogram of scores [55, 60, 65, 70, 70, 75, 80, 85, 90]

# Both should have titles and axis labels. Hint: call plt.show() after each chart to display them separately.

import matplotlib.pyplot as plt

sales = [100, 200, 150, 300, 250]
days = ["mon","tues","wed","thurs","fri"]


scores = [55, 60, 65, 70, 70, 75, 80, 85, 90]

plt.plot(days, sales)
plt.title("Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()        # ← show first chart

plt.hist(scores)
plt.title("Scores")
plt.xlabel("Score")
plt.ylabel("Count")
plt.show()        # ← show second chart


