def merge_sort(arr):
    if len(arr) <= 1:   # base case
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_result = merge_sort(left)
    right_result = merge_sort(right)

    return merge(left_result, right_result)


def merge(left_result, right_result):
    result = []
    i = j = 0

    # Merge two sorted halves
    while i < len(left_result) and j < len(right_result):
        if left_result[i] < right_result[j]:
            result.append(left_result[i])
            i += 1
        else:
            result.append(right_result[j])
            j += 1

    # Add remaining elements
    while i < len(left_result):
        result.append(left_result[i])
        i += 1

    while j < len(right_result):
        result.append(right_result[j])
        j += 1

    return result


# Example
arr = [18, 7, 33, 45, 8]
print("Original:", arr)
print("Sorted:", merge_sort(arr))
