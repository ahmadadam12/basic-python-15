"""
Let’s continue building Hangman. In the game of Hangman, 
a clue word is given by the program that the player has to guess, letter by letter. 
The player guesses one letter at a time until the entire word has been guessed. 
(In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. 
For this exercise, write the logic that asks a player to guess a letter and displays 
letters in the clue word that were guessed correctly. 

For now, let the player guess an infinite number of times until they get the entire word. 
As a bonus, keep track of the letters the player guessed and display a different message 
if the player tries to guess that letter again. 

Remember to stop the game when all the letters have been guessed correctly! 
Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining 
- we will deal with those in a future exercise.
"""
from operator import length_hint
import random

start = input(">>> Welcome to Hangman!\n_ _ _ _ _ _ _ _ _\nPush Enter!")

with open (r'C:\Users\adamz\basic-python-15\Exercise\keluarga.txt') as words:
    sowpods = words.readlines()
word = random.choice(sowpods)
word = word.rstrip(word[-1])
word = word.upper()

#print(len(word))
#print(pick_up)
#print("_ "*(len(pick_up)-1))
#word = "abcabcdefdef".upper()
#print(word)
#start = True


str1 = "_"*len(word)
i = 1
print(str1)

guess = (input("Input your guess: ")).upper()
found = [pos for pos, char in enumerate(word) if guess == char]

def pilih(choice):
    if choice == 2:
            guess = (input("Input your guess: ")).upper()
            found = [pos for pos, char in enumerate(word) if guess == char]
    elif choice == 1:
            answer = input("input your answer: ")
            answer = answer.upper()
            if answer == word:
                print(f"You are correct. The word is: {word}")
            else:
                print(f"wrong. the word is: {word}")
    else:
        print("wrong input")

    
while i < len(word):
    if guess in word:
        #print(str1)
        for x in found:
            str1 = str1[:x] + guess + str1[x+1: ]
        print(str1)
        i += 1
        print(f"your hint slot is: {len(word)-i}")
        choice = int(input("Do you want to guess or hint?\n1.guess\n2.hint\n"))
        pilih(choice)
    else:
        print("incorrect")
        i += 1
        print(f"your hint slot is: {len(word)-i}")
        choice = int(input("Do you want to guess or hint?\n1.guess\n2.hint"))
        pilih(choice)

if i >= len(word):
    print("out of trial. the answer is {]",{word})

        


