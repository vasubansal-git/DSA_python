# Merge sort: Divide and Merge technique used

arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]

def merge_arr(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while(i < n and j < m):
        if(left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        
    while(i < n):
        result.append(left[i])
        i += 1

    while(j < m):
        result.append(right[j])
        j += 1

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_arr(left, right)

print(f"After merge sort: \n{merge_sort(arr)}")

# Tc: O(log2 N X N) ≈ O(N log N)
# Sc: O(N)