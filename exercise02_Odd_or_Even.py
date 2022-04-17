"""
Ask the user for a number. 
Depending on whether the number 
is even or odd, 
print out an appropriate 
message to the user. 

Hint: how does an even / odd 
number react differently w
hen divided by 2?
"""

num = int(input("insert your number: "))

if num%2==0:
    print("your number is even")
else:
    print("your number is odd")s