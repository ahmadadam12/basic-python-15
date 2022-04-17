"""
Dictionary: use {},

"""

mydict = {"nama": ["iqbal", "john"], "alamat": ["bogor", "turkey"]}
#(mydict["alamat"][1])
b = range(0,len(mydict))


for x in mydict:
    for i in b:
        print(f"{x}: {mydict[x][i]}")
