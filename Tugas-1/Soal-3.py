teori = round(float(input("Masukkan nilai ujian teori: ")), 0)
praktek = round(float(input("Masukkan nilai ujian praktek: ")),0)

print(teori)
print(praktek)


if teori >= 70 and praktek >= 70:
    print("Selamat, Anda lulus!")
elif teori >=70 and praktek < 70:
    print("Anda harus mengulang ujian praktek.")
elif teori < 70 and praktek >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian praktek dan teori.")