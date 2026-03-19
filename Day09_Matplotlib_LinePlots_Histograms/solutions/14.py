
# Q10. Create a line plot of your own made-up data — something from real life that changes over time. Examples:

# Your study hours per day this week 

# Add full customization: title, labels, color, marker, grid.
# Make it yours.


import matplotlib.pyplot as plt 

study_hours = [5,2,7,4,1,9,0]

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

plt.plot( days , study_hours ,  color = "yellow" , marker = "x" , linewidth = 2 )

plt.title("Study hours this week")
plt.xlabel("studyhours")
plt.ylabel("days")

plt.show()


