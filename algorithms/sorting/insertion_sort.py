def insertion_sort(arr):

    for i in range(1,len(arr)):
        key = arr[i]
        last = i-1

        while last >= 0 and key < arr[last]:
            arr[last+1] = arr[last]
            last = last-1
            arr[last+1]=key

arr = [45,7,18,8,93,33]
insertion_sort(arr)
print(arr)