# Reverse an array using Recursion:

# arr = [1, 2, 3, 4, 5, 6, 7, 8]

# nums.reverse()
# print(nums)

# print(nums[::-1])

#Using recursion:

def func(arr, left, right):
    if left >= right:
        return
    arr[left],arr[right] = arr[right], arr[left]
    func(arr, left + 1, right - 1)

def revr_arr(arr):
    func(arr, 0, len(arr) - 1)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(revr_arr(arr))

#Tc = O(n)
#Sc = O(n) -> stack space