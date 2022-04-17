"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 

For example, say I type the string:

 My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""

sntc = input("please enter a sentence to be reversed: ")

def rvsword(sntc):
    splitSntc = sntc.split()
    #print(splitSntc)
    rvsSplit = splitSntc[::-1]
    #print(rvsSplit)
    rvsSntc = " ".join(rvsSplit)
    print(rvsSntc)


rvsword(sntc)