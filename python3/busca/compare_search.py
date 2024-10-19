import matplotlib.pyplot as plt
from binary_search import BinarySearch
from linear_search import LinearSearch
import numpy as np

# List sizes to test
list_sizes = [100, 1000, 10000, 100000, 1000000]

# Store execution times and operations
binary_times = []
linear_times = []
binary_operations = []
linear_operations = []

# Target item for search (middle value in sorted array)
for size in list_sizes:
    sorted_list = list(range(size))
    target_item = size // 2

    # Binary Search
    binary_search = BinarySearch(sorted_list, target_item)
    exec_time, operations = binary_search.search()
    binary_times.append(exec_time)
    binary_operations.append(operations)

    # Linear Search
    linear_search = LinearSearch(sorted_list, target_item)
    exec_time, operations = linear_search.search()
    linear_times.append(exec_time)
    linear_operations.append(operations)

# Plotting the results
plt.figure(figsize=(12, 6))

# Plot Execution Time
plt.subplot(1, 2, 1)
plt.plot(list_sizes, binary_times, label='Binary Search', marker='o')
plt.plot(list_sizes, linear_times, label='Linear Search', marker='o')
plt.xscale('log')
plt.yscale('log')
plt.title('Execution Time Comparison')
plt.xlabel('List Size (log scale)')
plt.ylabel('Execution Time (seconds, log scale)')
plt.legend()

# Plot Number of Operations
plt.subplot(1, 2, 2)
plt.plot(list_sizes, binary_operations, label='Binary Search', marker='o')
plt.plot(list_sizes, linear_operations, label='Linear Search', marker='o')
plt.xscale('log')
plt.title('Operations Comparison')
plt.xlabel('List Size (log scale)')
plt.ylabel('Number of Operations')
plt.legend()

plt.tight_layout()
plt.savefig("busca/search_comparison.png")
plt.show()

plt.close()