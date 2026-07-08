# Recursion: Check if a string is palindrome or not.

s = "anbcddcbna"

# Iterative approach:

n = len(s)
left = 0
right = n - 1

while left < right:
    if s[left] != s[right]:
        print(False)
        break

    left += 1
    right -= 1
else:
    print(True)

#Tc = O(n/2) -> O(n)
#Sc = O(1)

# By Recursion:

def func(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    
    return func(s, left + 1, right - 1)

n = len(s)
print(func(s, 0, n - 1))

#Tc: O(n)
#SC: O(n/2)