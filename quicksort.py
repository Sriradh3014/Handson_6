import timeit
import random
import numpy as np
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def generate_input(n, case):
    if case == "best":
        return list(range(n))
    elif case == "worst":
        return list(range(n, 0, -1))
    elif case == "average":
        return list(np.random.randint(1, 1000, n))

def benchmark(arr):
    execution_times = []
    setup_code = "from __main__ import quicksort"

    execution_time = timeit.timeit(stmt="quicksort(arr)", setup=setup_code, globals=globals(), number=10)
    execution_times.append(execution_time)

    return execution_times

# Benchmarking for best case
best_execution_times = []
input_sizes = [100, 500, 1000, 2000, 5000]
for n in input_sizes:
    arr = generate_input(n, "best")
    best_execution_times.extend(benchmark(arr))

# Benchmarking for worst case
worst_execution_times = []
for n in input_sizes:
    arr = generate_input(n, "worst")
    worst_execution_times.extend(benchmark(arr))

# Benchmarking for average case
average_execution_times = []
for n in input_sizes:
    arr = generate_input(n, "average")
    average_execution_times.extend(benchmark(arr))

# Plotting the results
plt.plot(input_sizes, best_execution_times, label='Best Case')
plt.plot(input_sizes, worst_execution_times, label='Worst Case')
plt.plot(input_sizes, average_execution_times, label='Average Case')

plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Quicksort Benchmark')
plt.legend()
plt.grid(True)
plt.show()
