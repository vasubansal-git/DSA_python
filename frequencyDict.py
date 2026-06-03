# Hashing Basics: Store the frequency of every element in a Dictionary.

# Method 1:

nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]

freq_map = {}
for i in range(0, len(nums)):
    if(nums[i] in freq_map):
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)
print(freq_map[1])

# Tc = O(n)
# Sc = O(n)

# Method 2:

nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]

hash_map = {}
n = len(nums)

for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

print(hash_map)

# Tc = O(n)
# Sc = O(1)