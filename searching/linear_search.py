def linear_search(arr,target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1

arr = [88,90,101,190]
target = 90
print(linear_search(arr,target))
