with open(r'C:\Users\adamz\basic-python-15\Exercise\happynumbers.txt') as happy:
    happy_text = happy.readline()
    #print(happy_text)
    happy_list = list()
    i = 1
    while happy_text:
        #print("Line {}: {}".format(i, happy_text.strip()))
        happy_list.append(happy_text)
        #print(happy_list)
        happy_text = happy.readline()
        #print(happy_text)
        i += 1
    #print(happy_list)

with open(r'C:\Users\adamz\basic-python-15\Exercise\primenumbers.txt') as prime:
    prime_text = prime.readline()
    #print(happy_text)
    prime_list = list()
    i = 1
    while prime_text:
        #print("Line {}: {}".format(i, prime_text.strip()))
        prime_list.append(prime_text)
        #print(prime_list)
        prime_text = prime.readline()
        #print(prime_text)
        i += 1
    #print(prime_list)

a = list()
for x in happy_list:
    if x in happy_list:
        if x in prime_list:
            a.append(x)
        else:
            continue

print(a)