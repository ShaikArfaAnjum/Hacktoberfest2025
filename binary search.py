def binarysearch(arr, k):
    low, high = 0, len(arr) - 1
    result = -1  # to store index if found
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            result = mid  # record this index
            high = mid - 1  # continue searching left for smaller index
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    return result
