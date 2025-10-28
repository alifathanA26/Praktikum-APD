import os

# Global 
users = {
    "maba": {"password": "026", "role": "user"},
    "admin": {"password": "111", "role": "admin"}
}

# Data furnitur 
furnitur = {
    "alat kebersihan": {"jumlah": 4, "kondisi": "baik", "lokasi": "gudang", "status": "tersedia"},
    "kartu akses ruangan": {"jumlah": 2, "kondisi": "baik", "lokasi": "resepsionis", "status": "aktif"},
    "pendingin ruangan": {"jumlah": 2, "kondisi": "rusak ringan", "lokasi": "ruang tamu", "status": "perbaikan"},
    "kursi plastik": {"jumlah": 10, "kondisi": "baik", "lokasi": "aula", "status": "tersedia"},
    "meja kerja": {"jumlah": 3, "kondisi": "baik", "lokasi": "kantor admin", "status": "dipakai"}
}

riwayat = []  

attempt = 0  

#Prosedur ga return 
def clear():
    os.system("cls")

def pause():
    input("\nTekan Enter untuk kembali...")

def login():
    clear()
    print("==LOGIN==")
    username = input("Username: ")
    password = input("Password: ")

    
    if username in users and password == users[username]["password"]:
        print("Login berhasil!!!")
        role = users[username]["role"]
        input("\nTekan Enter untuk melanjutkan..")

        if role == "admin":
            menu_admin()
        else:
            menu_user()
        return

    # Kalau salah:
    print("Username/Password salah!")
    input("\nTekan Enter untuk kembali..")

#NonParameter 
def tampilkan_furnitur():
    print("== DATA FURNITUR ==")
    for i, item in enumerate(furnitur, start=1):
        print(f"{i}. {item[0]} - Jumlah: {item[1]}")

#Parameter
def ubah_jumlah_furnitur(index, jumlah_baru):
    furnitur[index][1] = jumlah_baru
    return True

#Login(rekursif)
def login():
    global attempt
    clear()
    print("== LOGIN ==")
    username = input("Username: ")
    password = input("Password: ")
    attempt += 1


    for u in users:
        if username == u[0] and password == u[1]:
            print("Login berhasil!")
            pause()
            if u[2] == "admin":
                menu_admin()
            else:
                menu_user()
            return
        

    print("Username/Password salah!")
    if attempt < 3:
        pause()
        return login() 
    else:
        print("Terlalu banyak percobaan. Program keluar.")
        exit()

#Prosedur Menu Admin
def menu_admin():
    while True:
        clear()
        print("== MENU ADMIN BANGSAL LYN ==")
        print("1. Lihat Furnitur")
        print("2. Tambah Furnitur")
        print("3. Ubah Furnitur")
        print("4. Hapus Furnitur")
        print("5. Kembali")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            clear()
            tampilkan_furnitur()
            pause()

        elif pilihan == "2":
            clear()
            try:
                nama = input("Nama furnitur: ")
                jumlah = int(input("Jumlah: "))
                furnitur.append([nama, jumlah])
                print("Data berhasil ditambahkan!")
            except:
                print("Jumlah harus berupa angka!")
            pause()

        elif pilihan == "3":
            clear()
            tampilkan_furnitur()
            try:
                pilih = int(input("\nPilih nomor furnitur: ")) - 1
                nama_baru = input("Nama baru: ")
                jumlah_baru = int(input("Jumlah baru: "))
                furnitur[pilih][0] = nama_baru
                ubah_jumlah_furnitur(pilih, jumlah_baru)
                print("Data berhasil diubah!")
            except:
                print("Input salah!")
            pause()

        elif pilihan == "4":
            clear()
            tampilkan_furnitur()
            try:
                pilih = int(input("\nPilih nomor furnitur yang dihapus: ")) - 1
                print(f"{furnitur[pilih][0]} berhasil dihapus!")
                del furnitur[pilih]
            except:
                print("Input salah!")
            pause()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak valid!")
            pause()

#Prosedur Menu User 
def menu_user():
    while True:
        clear()
        print("== MENU USER ==")
        print("1. Lihat Furnitur")
        print("2. Keluar")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            clear()
            tampilkan_furnitur()
            pause()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid!")
            pause()

#Main Program 
while True:
    clear()
    print("== SISTEM PENGELOLAAN BANGSAL LYN ==")
    print("1. Login")
    print("2. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        login()
    elif pilih == "2":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid!")
        pause()
