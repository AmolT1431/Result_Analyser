import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C']
counts = [10, 20, 15]

# Plotting
plt.bar(categories, counts, color='skyblue')

# Adding count labels on top of the bars
for i, count in enumerate(counts):
    plt.text(i, count + 0.5, str(count), ha='center')

plt.xlabel('Categories')
plt.ylabel('Counts')
plt.title('Bar Plot with Count Labels')
plt.show()
