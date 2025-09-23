import matplotlib.pyplot as plt

semesters = list(range(1, 3))
gpa = [2.72, 2.09,1.98]

plt.figure(figsize=(10, 6))  # Set graph size
plt.plot(semesters, gpa, marker='o', linestyle='-', color='Orange', linewidth=2, markersize=8)
plt.title("GPA Trend Across Semesters", fontsize=14)
plt.xlabel("Semester", fontsize=12)
plt.ylabel("GPA", fontsize=16)
plt.grid(True)  # Add grid lines
plt.xticks(semesters)  # Show all semester numbers

plt.show()