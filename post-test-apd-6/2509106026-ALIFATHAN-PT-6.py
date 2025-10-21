import os

# Data user 
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

# SESI UMUM
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# REGISTER 
def register():
    clear()
    print("== REGISTRASI USER ==")
    username = input("Masukkan username: ").lower()
    password = input("Masukkan password: ")

    # Cek username  ada/tidak?
    if username in users:
        print(" Username sudah digunakan!")
    else:
        users[username] = {"password": password, "role": "user"}
        print(" Registrasi berhasil! Silakan login.")
    input("\nTekan Enter untuk kembali ke menu utama...")


#SESI LOGIN
def login():
    clear()
    print("==LOGIN==")
    username = input("Username:")
    password = input("Password:")

    for u in users:
        if u[0] == username and u[1] == password:
            print("Login berhasil!!!")

            if u[2] == "user":  
                input("\nTekan Enter untuk melihat furnitur...")
                lihat_furnitur()  

            return u[2]

    print("username/password salah!!")
    input("\nTekan Enter untuk kembali..")
    return None

def login():
    clear()
    print("== LOGIN ==")
    username = input("Username: ").lower()
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(" Login berhasil!")
        input("\nTekan Enter untuk melanjutkan...")
        return users[username]["role"]
    else:
        print(" Username atau password salah!")
        input("\nTekan Enter untuk mencoba lagi...")
        return None


# MENU ADMIN
def menu_admin():
    while True:
        clear()
        print("== MENU ADMIN BANGSAL LYN ==")
        print("1. Lihat Data Furnitur")
        print("2. Tambah Furnitur")
        print("3. Ubah Data Furnitur")
        print("4. Hapus Furnitur")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_furnitur()
        elif pilihan == "2":
            tambah_furnitur()
        elif pilihan == "3":
            ubah_furnitur()
        elif pilihan == "4":
            hapus_furnitur()
        elif pilihan == "5":
            break
        else:
            print(" Pilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")


# MENU USER
def menu_user():
    while True:
        clear()
        print("== MENU USER BANGSAL LYN ==")
        print("1. Lihat Furnitur")
        print("2. Keluar")
        pilih = input("Pilih: ")

        if pilih == "1":
            lihat_furnitur()
        elif pilih == "2":
            print("\nTerima kasih telah menggunakan sistem Bangsal Lyn!")
            break
        else:
            print(" Pilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")




# CRUD ADMIN
def lihat_furnitur():
    clear()
    print("== DATA FURNITUR ==")
    if not furnitur:
        print("Belum ada data furnitur.")
    else:
        for i, (nama, data) in enumerate(furnitur.items(), start=1):
            print(f"{i}. {nama.title()} | Jumlah: {data['jumlah']} | Kondisi: {data['kondisi']} | Lokasi: {data['lokasi']} | Status: {data['status']}")
    input("\nTekan Enter untuk kembali...")


def tambah_furnitur():
    clear()
    print("== TAMBAHKAN FURNITUR ==")
    nama = input("Nama Furnitur: ").lower()
    if nama in furnitur:
        print("Furnitur sudah ada!")
    else:
        jumlah = input("Jumlah: ")
        kondisi = input("Kondisi: ")
        lokasi = input("Lokasi: ")
        status = input("Status: ")

        if jumlah.isdigit():
            furnitur[nama] = {
                "jumlah": int(jumlah),
                "kondisi": kondisi,
                "lokasi": lokasi,
                "status": status
            }
            print(" Furnitur berhasil ditambahkan!")
        else:
            print("Jumlah harus berupa angka!")
    input("\nTekan Enter untuk kembali...")


def ubah_furnitur():
    clear()
    print("== UBAH DATA FURNITUR ==")
    lihat_furnitur()
    nama = input("\nMasukkan nama furnitur yang ingin diubah: ").lower()

    if nama in furnitur:
        print(f"Data lama: {furnitur[nama]}")
        jumlah_baru = input("Masukkan jumlah baru: ")
        kondisi_baru = input("Masukkan kondisi baru: ")
        lokasi_baru = input("Masukkan lokasi baru: ")
        status_baru = input("Masukkan status baru: ")

        if jumlah_baru.isdigit():
            furnitur[nama] = {
                "jumlah": int(jumlah_baru),
                "kondisi": kondisi_baru,
                "lokasi": lokasi_baru,
                "status": status_baru
            }
            print(" Data furnitur berhasil diperbarui!")
        else:
            print(" Jumlah harus berupa angka!")
    else:
        print(" Furnitur tidak ditemukan!")
    input("\nTekan Enter untuk kembali...")


def hapus_furnitur():
    clear()
    print("== HAPUS FURNITUR ==")
    lihat_furnitur()
    nama = input("\nMasukkan nama furnitur yang ingin dihapus: ").lower()

    if nama in furnitur:
        del furnitur[nama]
        print(" Furnitur berhasil dihapus!")
    else:
        print(" Furnitur tidak ditemukan!")
    input("\nTekan Enter untuk kembali...")


# PROGRAM UTAMA
while True:
    clear()
    print("== SISTEM PENGELOLAAN BANGSAL LYN ==")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        role = login()
        if role == "admin":
            menu_admin()
        elif role == "user":
            menu_user()
    elif pilih == "2":
        register()
    elif pilih == "3":
        clear()
        print("Terima kasih telah mengakses sistem Bangsal Lyn!")
        break
    else:
        print("Pilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")
