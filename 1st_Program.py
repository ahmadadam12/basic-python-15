
"""
b = range(0, int(len(a['nama'])))
c = range(0, int(len(a['telp'])))


for i in a:
    for y, z in b, c:
        print(i, ": ", a['nama'][y])
        print(i, ": ", a['telp'][z])

"""


a = {
    'nama': ('Fawwaz', 'John'),
    'telp': ('0812345678', '0823456789')
}

Nama_list = list(a['nama'])
print(Nama_list)
Tel_list = list(a['telp'])
print(Tel_list)

for n, t in zip (a['nama'], a['telp']):
    print(n, '\n', t)
