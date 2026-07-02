# ==========================================================
# GRRAS Solutions - DSML with AI
# Author : Sujaan Bhalla
# Day 13 - Matplotlib Basics
# ==========================================================

import matplotlib.pyplot as plt
import numpy as np

# ==========================================================
# 1. Basic Line Chart
# ==========================================================

x = [2010, 2015, 2020, 2025]
y = [100, 200, 250, 300]

plt.plot(x, y)

plt.xlabel("Years")
plt.ylabel("Sales")
plt.title("Sales Report")

plt.show()


# ==========================================================
# 2. Customized Line Chart
# ==========================================================

plt.figure(figsize=(6, 3))

plt.plot(
    x,
    y,
    color="green",
    marker="o",
    linestyle="--",
    linewidth=3,
    markersize=10
)

plt.xlabel("Years")
plt.ylabel("Sales")
plt.title("Customized Sales Report")

plt.show()


# ==========================================================
# 3. Multiple Line Chart
# ==========================================================

x = [2010, 2015, 2020, 2025]

jeans = [100, 200, 300, 400]
shirts = [80, 90, 100, 110]

plt.plot(x, jeans, label="Jeans")
plt.plot(x, shirts, label="Shirts")

plt.xlabel("Years")
plt.ylabel("Sales")
plt.title("Jeans vs Shirts Sales")

plt.legend()

plt.show()


# ==========================================================
# 4. Student Marks Comparison
# ==========================================================

students = ["Arun", "Priya", "Raj", "Neha", "Riya"]

maths = [80, 79, 89, 76, 87]
physics = [90, 79, 98, 97, 94]

plt.plot(students, maths, marker="o", label="Maths")
plt.plot(students, physics, marker="s", label="Physics")

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()
plt.grid(True)

plt.show()


# ==========================================================
# 5. Simple Bar Chart
# ==========================================================

x = [2015, 2020, 2025, 2030]
y = [100, 150, 200, 290]

plt.bar(x, y)

plt.xlabel("Year")
plt.ylabel("Sales")

plt.title("Sales Growth")

plt.show()


# ==========================================================
# 6. Multiple Bar Chart
# ==========================================================

groups = ["Group A", "Group B", "Group C", "Group D"]

x = np.arange(len(groups))

boys = [10, 20, 30, 40]
girls = [20, 30, 25, 30]

w = 0.40

plt.bar(x - w/2, boys, width=w, label="Boys")
plt.bar(x + w/2, girls, width=w, label="Girls")

plt.xlabel("Groups")
plt.ylabel("Students")

plt.title("Students in Groups")

plt.legend()

plt.show()


# ==========================================================
# 7. Triple Bar Chart
# ==========================================================

x = np.array([1, 2, 3, 4])

boys = [10, 20, 20, 40]
girls = [20, 30, 25, 30]
others = [30, 40, 35, 20]

w = 0.90

plt.bar(x - w/3, boys, width=w/3, label="Boys")
plt.bar(x, girls, width=w/3, label="Girls")
plt.bar(x + w/3, others, width=w/3, label="Others")

plt.xlabel("Groups")
plt.ylabel("No. of Students")

plt.title("Students in Each Group")

plt.legend()

plt.show()


# ==========================================================
# 8. Histogram
# ==========================================================

marks = [40, 55, 60, 70, 78, 80, 44, 50]

plt.hist(
    marks,
    bins=5,
    color="green"
)

plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.title("Marks Distribution")

plt.show()


# ==========================================================
# 9. Scatter Plot
# ==========================================================

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.scatter(x, y, color="red")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title("Scatter Plot")

plt.show()


# ==========================================================
# 10. Pie Chart
# ==========================================================

fruits = ["Apple", "Banana", "Orange", "Litchi"]
count = [40, 30, 15, 70]

colors = ["red", "yellow", "orange", "green"]

plt.pie(
    count,
    labels=fruits,
    colors=colors,
    startangle=90,
    autopct="%1.1f%%"
)

plt.title("Fruit Distribution")

plt.show()