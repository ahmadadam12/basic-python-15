"""
Write a program (function!) that takes a list and returns 
a new list that contains all the elements of the first list minus all the duplicates.
"""

import random

print(f"this program is for removing duplicates in two randomly generated lists.")
num1 = random.randint(int(input("min value list1: ")), int(input("max value list1: ")))
num2 = random.randint(int(input("min value list2: ")), int(input("max value list2: ")))

print(num1)
print(num2)

a = set()
b = set()

for i in range(0, num1):
    a.add(i)
print(f"num1 list: {a}")

for j in range(0, num2):
    b.add(j)
print(f"num2 list: {b}")

if len(a) > len(b): 
    z = a.difference(b)
    print(z)
elif len(a) < len(b):
    z = b.difference(a)
    print(z)
elif len(a) == len(b):
    z = b.difference(a)
    print(f"your two lists are the same content.")

