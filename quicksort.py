def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    print(f"pivot: {pivot}")
    low = []
    high = []
    for val in arr:
        if val < pivot:
            low.append(val)
        else:
            high.append(val)
    del high[0]
    print(f"high: {high}")
    print(f"low: {low}")
    print("----")
    quicksort(low)
    quicksort(high)
    low.append(pivot)
    return low + high


print(quicksort([3, 5, 2, 8, 9, 1]))
print("done")
