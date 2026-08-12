# Recursion:

# Head Recursion:
# Q1 Print "Vasu" for 4 times using recursion:

count = 0
def func():
    global count

    if count == 4:
        return
    print("Vasu")
    count += 1
    func()

func()


# Tail Recursion:

#Q2 print "Vasu" N times

n = 10
count = 0

def func():
    global count

    if count == n:
        return
    count += 1
    func()
    print("Vasu")

func()

# Tc = O(N + 1) -> O(N)
# Sc = O(N + 1) -> O(N)