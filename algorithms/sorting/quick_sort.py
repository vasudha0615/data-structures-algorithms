def quick_sort(arr):
    partition(arr,0,len(arr)-1)
    return arr

def partition(arr,start,end):
    if start >= end:
        return

    pivot = start
    i = start+1
    j = end

    while i <= j :
        if arr[i] > arr[pivot] and arr[j] < arr[pivot]:
            arr[i],arr[j] = arr[j],arr[i]  
        if arr[i] <= arr[pivot]:
            i+=1
        if arr[j] >=arr[pivot]:
            j-=1
        
    arr[j],arr[pivot]=arr[pivot],arr[j]

    partition(arr,start,j-1)
    partition(arr,j+1,end)

arr = [3,7,9,4,2,5]
quick_sort(arr)
print(arr)