# Print factors:

#Brute force:

num = int(input("Enter your number: "))

result = []
for i in range(1, num + 1):
    if (num % i == 0):
        result.append(i)

print(result)

#Tc = O(n)
#Sc = O(K)

#Better solution:
 
num = int(input("Enter your number: "))

result = []
for i in range(1,num // 2):
    if(num % i == 0):
        result.append(i)
result.append(num)

print(result)

# Tc = O(n/2) -> O(n)
# Sc = O(K)


# Optimal solution:

from math import sqrt

num = int(input("Enter your number: "))

result = []
for i in range(1,int(sqrt(num))):    # O(sqrt(n))
    if(num % i == 0):                #
        result.append(i)             #
    if(num // i != i):               #     O(1)
        result.append(num // i)      #   

result.sort()                        # O(n log n)
print(result)

# Tc = O(sqrt(n)) + O(n log n)
# Sc = O(K)