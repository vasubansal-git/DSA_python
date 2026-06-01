# Number is palindrome or not.

n = int(input("Enter a number: "))

num = n
result = 0
while num > 0:
    ld = num % 10
    result = (result * 10) + ld
    num = num // 10

if(result == n):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


# Tc = O(log(n))
# Sc = O(1)