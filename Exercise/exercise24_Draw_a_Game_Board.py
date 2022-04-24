"""
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 

This one is 3x3 (like in tic tac toe). 
Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, 
and draw it for them to the screen using Python’s print statement.
"""

print ("input size of the board")
x = int(input("horizontal: "))
y = int(input("vertical: "))

def length(x):
    dx = " ---"
    print(dx*x)
    
def width(x):
    dy = "|   "
    print(dy*(x+1))

i=1
while i <= y:
    length(x)
    width(x) 
    i += 1

print(" ---"*x)

#def repeat():