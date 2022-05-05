import random

start = input(">>> Welcome to 'Tebak Nama Quiz'!\n_ _ _ _ _ _ _ _ _\nRule:\n1. You have to guess the word randomly chosen.\n2. There will be suggestion for you.\n3. You can take a hint.\n4. Please read the instruction carefully.\nPush enter to continue!\n")
print("For hint: You have to guess a letter that possibly exist in the word.\nThe program will point on the place if it exists in the word\n")


with open (r'C:\Users\adamz\basic-python-15\Exercise\sowpods.txt') as words:
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

#print(word)

def pilih1(choice):
    answer = input("Input word guess: ")
    answer = answer.upper()
    if answer == word:
        print(f"\nYou are correct. The word is: {word}")
    else:
        print("\nYour answer is wrong")

def pilih2(choice, str1):
    guess = (input("Input a letter: ")).upper()
    found = [pos for pos, char in enumerate(word) if guess == char]
    if guess in word:
        #print(str1)
        for x in found:
            str1 = str1[:x] + guess + str1[x+1: ]
        print(str1)
    else:
        print("incorrect")

guessWord = (input("Enter your answer: ")).upper()
#found = [pos for pos, char in enumerate(word) if guess == char]

i = 0
j = 0
maxTry = len(word)-2
trySlot = maxTry
hintSlot = maxTry
if guessWord == word:
    print(f"\nSuper! You are correct. The word is: {word}")
else:
    print("\nyour answer is wrong")
    while True:
        if i < (len(word)-2) and j < (len(word)-2):
            choice = int(input(f"What do you want?\n1. Guess again?\n2. Take a hint\nYour guessing slot: {trySlot}\nYour hint slot is: {hintSlot}\n"))
            if choice == 1:
                pilih1(choice)
                i += 1
                trySlot = maxTry-i
                print(f"your chance is: {trySlot} times more")
                #print(f"i value is: {i}")
            elif choice == 2:
                pilih2(choice, str1)
                j += 1
                hintSlot = maxTry-j
                print(f"your hint slot is: {hintSlot}")
                #print(f"i value is: {j}")
                if hintSlot == 0:
                    answer = input("This is your last chance.\nEnter your answer: ")
                    answer = answer.upper()
                    if answer == word:
                        print(f"\nYou are correct. The word is: {word}")
                        break
                    else:
                        print("\nYour answer is wrong")     
                else:
                    continue
            else:
                print("wrong input")
        else:
            print("game over")
            break