def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i 
    return -1

arr = [4,7,90,45,32,88]
target = 90
print(linear_search(arr,target))