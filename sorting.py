import time

# ---------------- Selection Sort ----------------
def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    # Move through the array
    for i in range(n):

        # Assume current index is minimum
        min_index = i

        # Find smaller element
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        # Swap elements
        a[i], a[min_index] = a[min_index], a[i]

    return a


# ---------------- Bubble Sort ----------------
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)

    # Compare adjacent elements
    for i in range(n):
        for j in range(0, n - i - 1):

            # Swap if left element is bigger
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


# ---------------- Quick Sort ----------------
def quick_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Select first element as pivot
    pivot = arr[0]

    # Divide elements
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    # Recursive call
    return quick_sort(left) + [pivot] + quick_sort(right)


# ---------------- Merge Sort ----------------
def merge_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Divide array into halves
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge sorted halves
    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    # Compare and merge elements
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ---------------- Timing Function ----------------
def calculate_time(sort_function, arr):

    total = 0

    # Run 3 times
    for _ in range(3):

        start = time.time()

        sort_function(arr)

        end = time.time()

        total += (end - start)

    # Average time
    return total / 3


# ---------------- Test Arrays ----------------
sorted_5 = [1, 2, 3, 4, 5]
reverse_5 = [5, 4, 3, 2, 1]

sorted_100 = list(range(1, 101))
reverse_100 = list(range(100, 0, -1))


test_cases = [
    ("Sorted 5", sorted_5),
    ("Reverse 5", reverse_5),
    ("Sorted 100", sorted_100),
    ("Reverse 100", reverse_100)
]


algorithms = [
    ("Selection Sort", selection_sort),
    ("Bubble Sort", bubble_sort),
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort)
]


# ---------------- Display Results ----------------
for algo_name, algo_function in algorithms:

    print("\n", algo_name)

    for case_name, arr in test_cases:

        avg_time = calculate_time(algo_function, arr)

        print(f"{case_name}: {avg_time:.8f} seconds")