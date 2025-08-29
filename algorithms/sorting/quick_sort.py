def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr, start, end):
    if start >= end:
        return

    pivot_index = partition(arr, start, end)

    # Recursive calls for left and right subarrays
    _quick_sort(arr, start, pivot_index - 1)
    _quick_sort(arr, pivot_index + 1, end)


def partition(arr, start, end):
    pivot = arr[end]   # take last element as pivot
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot at the correct position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


# Example
arr = [18, 7, 33, 45, 8]
print("Original:", arr)
print("Sorted:", quick_sort(arr))
