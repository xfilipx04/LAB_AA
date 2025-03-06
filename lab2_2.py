import time
import random
import matplotlib.pyplot as plt

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def measure_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr.copy())
    return time.time() - start_time, sorted_arr

test_arrays = [
    [5, 3, 8, 6, 2, 7, 4, 1],#1
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],#2
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],#3
    [random.randint(0, 100) for _ in range(10)],#4
    [random.randint(0, 200) for _ in range(50)],#5
    [random.randint(0, 500) for _ in range(100)],#6
    [random.randint(0, 700) for _ in range(150)],#7
    [random.randint(0, 1000) for _ in range(200)],#8
    [random.randint(0, 1300) for _ in range(250)],#9
    [random.randint(0, 1500) for _ in range(300)],#10
    [random.randint(0, 1700) for _ in range(350)],#11
    [random.randint(0, 100) for _ in range(400)],#12
    [random.randint(0, 10) for _ in range(400)]#13
]

sorting_algorithms = [quicksort, merge_sort, heap_sort, bubble_sort]
labels = ['QuickSort', 'MergeSort', 'HeapSort', 'BubbleSort']

time_results = {label: [] for label in labels}

for i, arr in enumerate(test_arrays):
    print(f"Test Array {i+1}: {arr}")
    for func, label in zip(sorting_algorithms, labels):
        time_taken, sorted_arr = measure_time(func, arr)
        time_results[label].append(time_taken)
        print(f"{label}: {sorted_arr} (Time: {time_taken:.6f} sec)")
    print("-" * 50)

# Generate plots
x_labels = [f"Array {i+1}" for i in range(len(test_arrays))]
fig, ax = plt.subplots()

for label in labels:
    ax.plot(x_labels, time_results[label], marker='o', label=label)

ax.set_xlabel("Test Arrays")
ax.set_ylabel("Execution Time (seconds)")
ax.set_title("Sorting Algorithm Performance")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
