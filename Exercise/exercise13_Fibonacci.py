"""
Write a program that asks the user 
how many Fibonnaci numbers to 
generate and then generates them. 

Take this opportunity to think about 
how you can use functions. 

Make sure to ask the user to enter 
the number of numbers in the sequence 
to generate.

(Hint: The Fibonnaci seqence is a 
 sequence of numbers where the next 
 number in the sequence is the sum of
 the previous two numbers in the
 sequence. The sequence looks like 
 this: 1, 1, 2, 3, 5, 8, 13, …)
"""

num = int(input("how many number of fibonacci do you want? "))
a = [1]
z = [1]
def fibonacci(num):
    b = range(0, num-1)
    for i in b:
        f = a[i] + a[i-1]
        a.append(f)
        z.append(a[i])
    #print(a)
    print(z)

fibonacci(num)