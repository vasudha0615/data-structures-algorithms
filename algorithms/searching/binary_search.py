def binary_search(arr,target):
    left,right = 0,len(arr)-1

    while left<=right:
        mid = (left + right)//2

        if  arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid+1

        else:
            right = mid-1
    return -1


print(binary_search([34,56,90,98,111,179],111))   