
start = input("Selamat datang!\nTekan Enter untuk memulai:")

def menu(start):
    if start == "":
        print(f"Silahkan pilih Menu di bawah:")
        print(f"\n---Menu---")
        print(f"1. Daftar Kontak")
        print(f"2. Tambah Kontak")
        print(f"3. Keluar")
        choice = int(input("Input pilihan Anda: "))
        action(choice)
    else:
        print(f"Program akan selesai")
        
contact = {
    'nama': ('Fawwaz', 'John'),
    'telp': ('0812345678', '0823456781')
    }

nama = list(contact['nama'])
telp = list(contact['telp'])


def action(choice):
    if choice == 1:
        for n, t in zip(nama, telp):
            print(f"Nama: {n}\nNo.Telp{t}")
        start = input("Tekan Enter untuk kembali ke Menu.")
        menu(start)
    elif choice == 2:
        #add contact
        start = input("Tekan Enter untuk kembali ke Menu.")
        menu(start)
    elif choice == 3:
        print(f"Program selesai!\nSampai jumpa!\n")
        #start = ""
        #menu(start)
    else:
        print(f"Input salah.")
        start = ""
        menu(start)

menu(start)
