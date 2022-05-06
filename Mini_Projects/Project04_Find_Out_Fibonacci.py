"""
You input a number and the function created checks 
whether the number belongs to the Fibonacci sequence or not. 
"""

#num = int(input("This is fibonacci checker.\nInput your number: "))

def generator(num):
    b = range(0, num-1)
    for i in b:
        f = a[i] + a[i-1]
        a.append(f)
        z.append(a[i])
    #print(a)
    print(f"{z}\n")

def checker(num):
    b = range(0, num-1)
    for i in b:
        f = a[i] + a[i-1]
        a.append(f)
        z.append(a[i+1])
        if num == f:
            print("Your number is fibonacci.")
            break
        elif f < num:
            continue
        else:
            print("Your number is NOT fibonacci.")
            break
    print(f"The fibonacci number list: {z}\n")

while True:
    a = [1]
    z = [1]
    start = int(input("This is fibonacci generator and checker.\nSelect Menu:\n1. Generate Fibonacci\n2. Check your number is Fibonacci or not\n3. Quit Program\n"))
    if start == 1:
        num = int(input("How many number of fibonacci do you want? "))
        generator(num)
    elif start == 2:
        num = int(input("Input your number: "))
        checker(num)
    elif start == 3:
        print("Thank you")
        break 
    else: 
        print("Select 1 or 2.")
