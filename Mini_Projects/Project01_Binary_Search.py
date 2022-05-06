"""
1. Generate 0 to 100 array or user input range
2. Search user input is in the list or not
3. Search the middle value first, 
then check user value is bigger or smaller than the middle
4. Continue searching until the number is found or the array size become 0.
"""

import math
import random

print("This programm will randomly generates number between 0 and 100.\nYou can enter a guessed number to check your number is there or not.\nSucceding number will have different 2 from the low number.")

low = random.randint(0,50)
high = random.randint(51,100)

print(f"low number: {low}\nhigh number: {high}")

arr = list(range(low, high, 2))
mid = math.ceil((len(arr)/2))
print(arr)
print(arr[mid])

x = int(input("Input your guessing value: "))

while len(arr)>2:
    if x == arr[mid] or x==arr[mid+1]:
        print("your number is here")
        break
    elif x > arr[mid]:
        low = arr[mid]
        arr = list(range(low, high, 2))
        mid = math.ceil((len(arr)/2))
        #print(arr)
        #print(arr[mid])
    elif x < arr[mid]:
        high = arr[mid]
        arr = list(range(low, high, 2))
        mid = math.ceil((len(arr)/2))
        #print(f"midd is: {mid}")
        #print(arr)
        #print(arr[mid])
else:
    print("your number is not here")

   



    
    