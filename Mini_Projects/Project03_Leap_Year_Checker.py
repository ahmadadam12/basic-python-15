"""
 input a year and check whether it is a leap year or not. 
 For this, you’ll have to create a function that recognizes the pattern of leap years 
 and can try fitting the inputted year into the pattern. 
 In the end, you can print the result using a boolean expression.
"""

print("This program is to check whether entered year is leap year or not.")

while True:
    year = int(input("Insert your year: "))
    a = year%400
    b = year%100
    c = year%4
    if a == 0:
        print("your year is a leap year.")
    elif a != 0 and c == 0 and b != 0:
        print("your year is a leap year.")
    else:
        print("your year is not a leap year.")
