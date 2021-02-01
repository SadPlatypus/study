def binary_search(sorted_array, n):
    left = 0
    right = len(sorted_array) - 1
    while left < right:
        mid = (left + right) // 2
        if sorted_array[mid] < n:
            left = mid + 1
        else:
            right = mid
    return left if sorted_array[left] == n else -1
