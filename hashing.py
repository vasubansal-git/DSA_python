# hashing: prestoring values into same datastructure like List/Dictionary/Set and the fetching it.

#Q1: n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10], m = [10, 111, 1, 9, 5, 67, 2]
# Constraints:
#1. 1 <= n[i] <= 10
#2. n can have 10^8 elements
#3. mcan have 10^8 elements

# Solution using hash_list

# Brute force: Tc: O(n X m), Sc: O(1)
""" 
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(count)

# Optimal approach: Tc = O(n * m), Sc = O(11) -> O(1)

hash_list = [0] * 11

for num in n:
    hash_list[num] += 1

for x in m:
    if x < 1 or x > 10:
        print(0)
    else:
        print(hash_list[x])
"""

# solution using Dictionary:
""" 
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
"""

#Q2: Character hashing:

