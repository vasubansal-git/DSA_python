# Fibonacci Numbers:
def func(n):
    if n == 0 or n == 1:
        return n
    return func(n - 1) + func(n - 2)

def fibonacci(n):
    answer = func(n)
    return answer

n = int(input("Enter your number: "))
print(f"fibonacci number of {n}: {fibonacci(n)}")

#Tc: O(2^n)
#Sc: O(2^n)