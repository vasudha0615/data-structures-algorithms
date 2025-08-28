def merge_sort(arr):
    if len(arr)==0:
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left_result = merge_sort(left)
    right_result = merge_sort(right)
