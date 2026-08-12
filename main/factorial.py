# Find Factorial of a number using recursion:

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter your number: "))
factorial_num = factorial(num)
print(f"Factorial of {num}: {factorial_num}")

#Tc = O(n)
#Sc = O(n) -> Stack space