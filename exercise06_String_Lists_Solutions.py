"""
Ask the user for a string and print out
whether this string is a palindrome 
or not. 
(A palindrome is a string that 
 reads the same forwards and 
 backwards.)
"""

"""
#Method1
word = str(input("input a string: "))
rvs = (word[::-1])

if word == rvs:
    print("palindrome")
else:
    print("not palindrome")
"""

"""
>>> letters = "ABCDEF"

>>> letters[::-1]
'FEDCBA'

>>> letters
'ABCDEF'
"""

#Method2
word = str(input("input a string: "))
print(range(len(word)))

rvs = ""
for i in range(len(word)):
    rvs = rvs + word[len(word)-1-i]
    print(rvs)

if word == rvs:
    print("palindrome")
else:
    print("not palindrome")

























