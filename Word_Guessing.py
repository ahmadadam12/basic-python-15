from operator import length_hint
import random
from re import I

start = input(">>> Welcome to the game!\n_ _ _ _ _ _ _ _ _\nRule:\n1. You have to guess the word randomly chosen.\n2. There will be suggestion for you.\n3. You can take a hint.\npush enter to continue!")


with open (r'C:\Users\adamz\basic-python-15\Exercise\keluarga.txt') as words:
    sowpods = words.readlines()
word = random.choice(sowpods)
word = word.rstrip(word[-1])
word = word.upper()

first = word[0]
last = word[-1]

str1 = "_"*len(word)
str1 = first + str1[1:(len(word)-1)] + last
str2 = str1
print(str1)


def pilih(choice):
    if choice == 1:
        pilih1(choice)
    elif choice == 2:
        pilih2(choice, str1)
    else:
        print("wrong input")


def pilih1(choice):
        i = 1
        while i <= 3:
            answer = input("input your answer: ")
            answer = answer.upper()
            if answer == word:
                print(f"You are correct. The word is: {word}")
                break
            else:
                print("The answer is wrong")
                choice = int(input("Incorrect. What do you want?\n1. Guess again?\n2. Take a hint\n"))
                i += 1
                pilih(choice)
                continue
        print(f"wrong. the word is: {word}")

def pilih2(choice, str1):
    guess = (input("Input your guess: ")).upper()
    found = [pos for pos, char in enumerate(word) if guess == char]
    y = 1
    maxTry = len(word)-2
    if maxTry-y == 0:
        print("Game over")
    else:
        while y <= maxTry:
            if guess in word:
                #print(str1)
                for x in found:
                    str1 = str1[:x] + guess + str1[x+1: ]
                print(str1)
                y += 1
                print(f"your hint slot is: {maxTry-y}")
                choice = int(input("Do you want to guess or hint?\n1.guess\n2.hint\n"))
                pilih(choice)
            else:
                print("incorrect")
                y += 1
                print(f"your hint slot is: {maxTry-y}")
                choice = int(input("Do you want to guess or hint?\n1.guess\n2.hint"))
                pilih(choice)


guessWord = (input("Input your word guess: ")).upper()
#found = [pos for pos, char in enumerate(word) if guess == char]

if guessWord == word:
    print(f"Super! You are correct. The word is: {word}")
else:
    choice = int(input("Incorrect. What do you want?\n1. Guess again?\n2. Take a hint\n"))
    pilih(choice)