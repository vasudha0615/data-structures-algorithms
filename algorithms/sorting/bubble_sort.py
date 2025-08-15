def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for index in range(0,n-i-1):
            if arr[index]>arr[index+1]:
                arr[index],arr[index+1]=arr[index+1],arr[index]

arr = [22,90,67,89,15,43]
bubble_sort(arr)
print(arr)