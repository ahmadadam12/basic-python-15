"""
In this exercise, the task is to write a function that picks 
a random word from a list of words from the SOWPODS dictionary. 
Download this file and save it in the same directory as your Python code. 
This file is Peter Norvig’s compilation of the dictionary of words used 
in professional Scrabble tournaments. 
Each line in the file contains a single word

CONTINUIE TO EXERCISE 31
"""

import random

with open (r'C:\Users\adamz\basic-python-15\Exercise\sowpods.txt') as words:
    sowpods = words.readlines()

pick_up = random.choice(sowpods)

print(pick_up)
