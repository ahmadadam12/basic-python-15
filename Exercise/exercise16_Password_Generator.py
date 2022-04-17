"""
Write a password generator in Python. 
Be creative with how you generate passwords - strong passwords have a mix of 
lowercase letters, 
uppercase letters, 
numbers, and 
symbols. 

The passwords should be random, 
generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. 
For weak passwords, pick a word or two from a list.

"""

import random
import string
from traceback import print_list

#print(string.ascii_lowercase)
#print(string.ascii_uppercase)
#print(string.digits)
#print(string.punctuation)

strength = int(input("how many characters your password is? "))

def generator(strength):
    rndmpassword = ""
    password = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    for i in range(strength):
        rndmpassword = rndmpassword + random.choice(password)
    print(f"your password is: {rndmpassword}")


def password(strength):
    if strength <= 4:
        while strength <=4:
            print(f"your password is too short.")
            strength = int(input("please re-input: "))
            #print(strength)
            if strength > 4:
                generator(strength)
                break
            else:
                continue
    else:
        generator(strength)

password(strength)
            



