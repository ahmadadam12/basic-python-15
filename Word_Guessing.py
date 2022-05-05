import random

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

def pilih1(choice, i):
    answer = input("input your answer: ")
    answer = answer.upper()
    if answer == word:
        print(f"You are correct. The word is: {word}")
    else:
        print("The answer is wrong")
        i += 1
    print(f"wrong. the word is: {word}")      

def pilih2(choice, str1, i):
    guess = (input("Input your guess: ")).upper()
    found = [pos for pos, char in enumerate(word) if guess == char]
    maxTry = len(word)
    if guess in word:
        #print(str1)
        for x in found:
            str1 = str1[:x] + guess + str1[x+1: ]
        print(str1)
        i +=1
        hintSlot = maxTry-i
        print(f"your hint slot is: {hintSlot}")
    else:
        print("incorrect")
        i += 1
        hintSlot = maxTry-i
        print(f"your hint slot is: {hintSlot}")
    return i


guessWord = (input("Input your word guess: ")).upper()
#found = [pos for pos, char in enumerate(word) if guess == char]


if guessWord == word:
    print(f"Super! You are correct. The word is: {word}")
else:
    print("your answer is incorrect")
    i = 1
    while True:
        if i <= (len(word)-2):
            choice = int(input("What do you want?\n1. Guess again?\n2. Take a hint\n"))
            if choice == 1:
                pilih1(choice, i)
            elif choice == 2:
                pilih2(choice, str1, i)
            else:
                print("wrong input")
        else:
            print("game over")