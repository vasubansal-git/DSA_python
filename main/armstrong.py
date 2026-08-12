# Armstrong number:
def count(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10

    return count


n = int(input("Enter your number: "))

digits = count(n)
num = n
total = 0

while num > 0:
    ld = num % 10
    total = total + (ld ** digits)
    num = num // 10

if(total == n):
    print("Yes this number is armstrong.")
else:
    print("No it is not a armstrong number.")

# Tc = O(log(n))
#Sc = O(1)
