"""
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

"""
 
filename = input("plase input file name: ")

with open(filename, 'w') as f:
    f.write('coba coba')

with open(filename, 'r') as open_file:
    all_text = open_file.read()
print("aaa")
print(all_text)