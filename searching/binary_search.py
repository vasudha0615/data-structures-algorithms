def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:   # continue until left and right meet
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid     # return index if found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1   # not found


# Example usage
arr = [22, 45, 78, 90, 95, 100]  # must be sorted
target = 90
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
