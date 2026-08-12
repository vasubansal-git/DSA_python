arr = [4, 1, 7, 6, 3, 2, 8]

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while(arr[i] <= pivot and i <= high - 1):
            i += 1
        while(arr[j] > pivot and j >= low + 1):
            j -= 1

        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j

def quickSort(arr, low, high):
    if low < high:
        p_idx = partition(arr, low, high)
        quickSort(arr, low, p_idx - 1)
        quickSort(arr, p_idx + 1, high)

n = len(arr)
quickSort(arr, 0, n - 1)
print(f"Sorted Array: {arr}")

# Tc: O(N log N) in best and average case
# SC: O(1)

# Tc: O(N^2) in worst case when arr = [5, 5, 5, 5, 5, 5, 5, 5, 5] something like this
# Sc: o(1)