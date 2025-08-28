def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        last = i - 1
        while last >= 0 and key < arr[last]:
            arr[last+1] = arr[last]
            last = last - 1
            arr[last+1] = key

    return arr

arr = [66,75,32,45,8]
print(insertion_sort(arr))
