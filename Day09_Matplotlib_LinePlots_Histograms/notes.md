

# 📝 Day 9 Notes — Matplotlib Basics

---

## CONCEPT 1 — Importing Matplotlib

### Real-Life Analogy
Before you draw anything you need to open your sketchbook.
Importing Matplotlib is exactly that — you are not drawing yet,
just getting your tools ready.

### Code
import matplotlib.pyplot as plt
print("Matplotlib is ready!")

### Syntax Breakdown
| Part | Meaning |
|---|---|
| import | Load an external library |
| matplotlib.pyplot | The drawing module inside Matplotlib |
| as plt | Short nickname so you type plt instead of matplotlib.pyplot |

---

## CONCEPT 2 — Line Plot (Basic)

### Real-Life Analogy
You have sales numbers for 7 days. You could stare at the numbers —
or draw a line and instantly see the trend.
Your brain reads a line in 1 second. Numbers take 10 seconds.

### Code
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
sales = [100, 120, 90, 150, 130, 170, 160]

plt.plot(days, sales)
plt.show()

### Syntax Breakdown
| Part | Meaning |
|---|---|
| days | X-axis values (horizontal) |
| sales | Y-axis values (vertical) |
| plt.plot(days, sales) | Draws the line connecting all points |
| plt.show() | Displays the chart on screen |

---

## CONCEPT 3 — Customizing a Line Plot

### Real-Life Analogy
A plain chart with no title is like a document with no heading.
Nobody knows what they are looking at.
Adding labels and color makes it professional and readable.

### Code
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
sales = [100, 120, 90, 150, 130, 170, 160]

plt.plot(days, sales, color='blue', linewidth=2, marker='o')
plt.title("Weekly Sales")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

### Syntax Breakdown
| Part | Meaning |
|---|---|
| color='blue' | Line color |
| linewidth=2 | Makes line thicker |
| marker='o' | Circle dot at each data point |
| plt.title() | Title above the chart |
| plt.xlabel() | Label on the X-axis |
| plt.ylabel() | Label on the Y-axis |
| plt.grid(True) | Turns on background grid |

---

## CONCEPT 4 — Histogram (Basic)

### Real-Life Analogy
100 students took an exam. Reading 100 numbers is painful.
A histogram groups them into buckets and shows a bar for each bucket.
Taller bar = more students in that range.

### Key Difference
Line plot = shows change over TIME
Histogram = shows how data is DISTRIBUTED

### Code
import matplotlib.pyplot as plt

scores = [45, 55, 60, 62, 65, 65, 70, 72, 75, 75,
          78, 80, 80, 82, 85, 85, 88, 90, 92, 95]

plt.hist(scores)
plt.show()

### Syntax Breakdown
| Part | Meaning |
|---|---|
| scores | Your data list |
| plt.hist(scores) | Auto-groups into buckets and draws bars |

---

## CONCEPT 5 — Customizing a Histogram

### Real-Life Analogy
bins is like choosing your bucket size.
Sorting mangoes every 10g gives more detail than every 100g.
More bins = more detail. Fewer bins = broader picture.

### Code
import matplotlib.pyplot as plt

scores = [45, 55, 60, 62, 65, 65, 70, 72, 75, 75,
          78, 80, 80, 82, 85, 85, 88, 90, 92, 95]

plt.hist(scores, bins=5, color='orange', edgecolor='black')
plt.title("Student Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.show()

### Syntax Breakdown
| Part | Meaning |
|---|---|
| bins=5 | Divide data into exactly 5 buckets |
| color='orange' | Fill color of bars |
| edgecolor='black' | Border color around each bar |

---

## KEY RULES TO REMEMBER

1. plt.plot(X, Y) — X is always horizontal, Y is always vertical
2. Days go on X. Values go on Y. Never swap them.
3. plt.show() must come AFTER savefig() if saving
4. plt.show() must be called after each chart to show them separately
5. xlabel and ylabel take STRINGS not lists
