def quicksort(ary):
    if len(ary) <= 1:
        return ary
    pivot = ary[0]
    low = []
    high = []
    for i in range(1, len(ary)):
        val = ary[i]
        if val < pivot:
            low.append(val)
        else:
            high.append(val)
    low = quicksort(low)
    high = quicksort(high)
    low.append(pivot)
    return low + high

print(quicksort([3, 5, 2, 8, 9, 1, 1, -1000]))
