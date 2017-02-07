def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    low = []
    high = []
    for val in arr:
        if val < pivot:
            low.append(val)
        else:
            high.append(val)
    del high[0]

    quicksort(low)
    quicksort(high)
    print("---")
    print(low)
    print(high)
    return low.append(high)

print(quicksort([3, 5, 2, 8]))