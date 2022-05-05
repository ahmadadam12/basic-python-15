"""
1. Generate 0 to 100 array or user input range
2. Search user input is in the list or not
3. Search the middle value first, 
then check user value is bigger or smaller than the middle
4. Continue searching until the number is found or the array size become 0.
"""

import math


low = int(input("Input lower value: "))
high = int(input("Input high value: "))

arr = list(range(low, high+2, 2))
mid = math.ceil((len(arr)/2))-1
print(arr)
#print(mid)

x = int(input("Input your guessing value: "))

while len(arr)>2:
    if x == arr[mid]:
        print("your number is here")
        break
    elif x > arr[mid]:
        low = arr[mid+1]
        arr = list(range(low, high+2, 2))
        #print(arr)
        mid = math.ceil((len(arr)/2))-1
    elif x < arr[mid]:
        high = arr[mid-1]
        arr = list(range(low, high, 2))
        #print(arr)
        mid = math.ceil((len(arr)/2))-1
else:
    print("your number is not here")

   



    
    