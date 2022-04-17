num1 = int(input("insert a number: "))
num2 = int(input("insert a number: "))
a = []
b = []
noDuplicates = set()

for i in range(0, num1):
    a.append(i)
    noDuplicates.add(a[i])
    i = i+1
print(f"num1 list: {a}")

for j in range(0, num2):
    b.append(j)
    noDuplicates.add(b[j]) 
    j = j+1
print(f"num2 list: {b}")


print(noDuplicates)
