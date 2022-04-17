"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
"""

import random

a = int(input("insert your first number: "))
b = int(input("insert your second number: "))
trial = int(input("how many times do you want to try? "))
i = 0
num = random.randint(a, b)
print(f"your number is: {num}")

while i<trial:
    guess = int(input("please input your guess: "))
    i = i+1
    if guess < num:
        print("your number is too small.")
        continue
    elif guess > num:
        print("your number is too big: ")
        continue
    else:
        print("yes you are correct")
        break
    """
    if guess < num:
        guess = int(input("your number is too small, try again: "))
    elif guess > num:
        guess = int(input("your number is too small, try again: "))
    elif guess == num:
        print("your are correct!")
    """
if i == trial:
    print("you are failed")
else: 
    print ("your are success!")





