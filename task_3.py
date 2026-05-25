import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timsort(arr):
    return sorted(arr)

def main():
    sizes = [100, 1000, 5000, 10000]

    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        t_merge = timeit.timeit(lambda: merge_sort(arr), number=10) / 10
        t_ins   = timeit.timeit(lambda: insertion_sort(arr), number=10) / 10
        t_tim   = timeit.timeit(lambda: timsort(arr), number=10) / 10

        print(f"Розмір: {size}")
        print(f"  Merge Sort:     {t_merge:.6f} секунд")
        print(f"  Insertion Sort: {t_ins:.6f} секунд")
        print(f"  Timsort:        {t_tim:.6f} секунд")
        print("-" * 40)

if __name__ == "__main__":
    main()
