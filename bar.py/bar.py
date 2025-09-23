import matplotlib.pyplot as plt

categories = ['Food', 'Travel', 'Entertainment']
values = [200, 150, 100]

# Create bar chart with customization
plt.bar(categories, values, color=['red', 'blue', 'green'], edgecolor='black')
plt.title("Monthly Expenses Comparison", fontsize=14)
plt.xlabel("Expense Categories", fontsize=12)
plt.ylabel("Amount ($)", fontsize=12)
plt.grid(axis='y', alpha=0.3)  # Add horizontal grid lines

# Add value labels on top of bars
for i, value in enumerate(values):
    plt.text(i, value + 5, f'${value}', ha='center')

plt.show()