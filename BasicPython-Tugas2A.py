#existing contact
contact = {
    'nama': ('Fawwaz', 'John'),
    'telp': ('0812345678', '0823456781')
    }

nama = list(contact['nama'])
telp = list(contact['telp'])

#start program
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
        print(f"Program akan selesai.")

def action(choice):
    if choice == 1:
        #menampilan contact
        for n, t in zip(nama, telp):
            print(f"Nama: {n}\nNo.Telp: {t}")
        start = input("Tekan Enter untuk kembali ke Menu.")
        menu(start)
    elif choice == 2:
        #menambahkan contact
        print(f"masukkan nama dan nomor telp yang ingin ditambahkan:")
        new_nama = input("Nama: ")
        new_telp = input("No. Telp: ")
        nama.append(new_nama)
        telp.append(new_telp)
        #print(nama)
        #print(telp)   
        start = input("Kontak baru berhasil ditambahkan.\nTekan Enter untuk kembali ke Menu.")
        menu(start)
    elif choice == 3:
        #program selesai
        print(f"Program selesai!\nSampai jumpa!\n")
    else:
        print(f"Menu tidak tersedia")
        start = ""
        menu(start)

menu(start)
