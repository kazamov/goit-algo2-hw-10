import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = random.randint(0, len(arr)-1)
    pivot = arr[pivot_index]
    less = [x for i, x in enumerate(arr) if x < pivot or (x == pivot and i != pivot_index)]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + [pivot] + randomized_quick_sort(greater)

def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return deterministic_quick_sort(less) + [pivot] + deterministic_quick_sort(greater)

def run_task1():
    sizes = [10_000, 50_000, 100_000, 500_000]
    random_times = []
    deterministic_times = []
    
    for size in sizes:
        test_array = [random.randint(-1_000_000, 1_000_000) for _ in range(size)]
        rt = 0
        dt = 0
        for _ in range(5):
            arr_copy = test_array[:]
            start = time.perf_counter()
            randomized_quick_sort(arr_copy)
            rt += time.perf_counter() - start
            
            arr_copy = test_array[:]
            start = time.perf_counter()
            deterministic_quick_sort(arr_copy)
            dt += time.perf_counter() - start
        random_times.append(rt / 5)
        deterministic_times.append(dt / 5)

    print("Size\tRandomized_QS\tDeterministic_QS")
    for size, rt, dt in zip(sizes, random_times, deterministic_times):
        print(f"{size}\t{rt:.6f}\t{dt:.6f}")
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, random_times, marker='o', label='Randomized QuickSort')
    plt.plot(sizes, deterministic_times, marker='o', label='Deterministic QuickSort')
    plt.xlabel('Array Size')
    plt.ylabel('Average Time (s)')
    plt.title('QuickSort Algorithms Performance')
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Conclusion:")
    print("randomized_quick_sort demonstrates more stable performance due to the random selection of the pivot,")
    print("which ensures effective partitioning even for varied input data.")
    print("deterministic_quick_sort may be less efficient if the chosen pivot (first element)")
    print("does not partition the array into balanced subarrays, especially noticeable with certain ordered data.")

if __name__ == "__main__":
    run_task1()