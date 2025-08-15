def selection_sort(arr):
    for i in range(len(arr)):
        min = i

        for item in range(i+1,len(arr)):
            if arr[item] < arr[min]:
                min = item

        arr[i],arr[min] = arr[min],arr[i]

arr = [45,98,66,3,22,19]
selection_sort(arr)
print(arr)