# Bubble Sort

nums = [5, 8, 1, 6, 9, 2, 4]
nums2 = [1, 2, 4, 5, 9, 10, 12, 14]

n = len(nums)
for i in range(n-2, -1, -1):
    for j in range(0, i + 1):
        if nums[j] > nums[j + 1]:
            nums[j],nums[j + 1] = nums[j + 1],nums[j]

print(nums)

# Tc and Sc in average and worst case:
# Tc = O(N^2)
# Sc = O(1)

m = len(nums2)
for i in range(m - 2 ,-1, -1):
    is_swap = False
    for j in range(0, i + 1):
        if nums2[j] > nums2[j + 1]:
            nums2[j],nums2[j + 1] = nums2[j + 1], nums2[j]
            is_swap = True

    if is_swap == False:
        break

print(nums2)

#Tc and Sc in best case:
#Tc = O(N)
#SC = O(1)