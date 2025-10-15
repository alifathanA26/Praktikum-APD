import os

# Data admin user beserta furnitur
users = [
    ["maba", "026", "maba"],
    ["admin", "111", "admin"],
    ]

furnitur = [
    ["alat kebersihan", 4],
    ["kartu akses ruangan", 2],
    ["pendingin ruangan", 2],
    ["kursi plastik", 2],
]

#bersihkan layar
def clear():
    os.system("cls")

#Register
def register():
    
    clear()
    print("==REGISTRASI USER==")
    username = input("Masukkan username:")
    password = input(("Masukkan password:"))

    #cek sudah ada?
    sudah_ada = False
    for u in users:
        if u[0] == username:
            sudah_ada = True
    if sudah_ada :
        print("username sudah digunakan")

    else:
        users.append([username, password, "user"])
        print("Registrasi berhasil!")

#Login
def login():
    clear()
    print("==LOGIN==")
    username = input("Username:")
    password = input("Password")

    for u in users:
        if u[0]== username and u[1]== password:
            print("Login berhasil!!!")
            return u[2] 
    print("username/password salah!!") 
    input("\nTekan Enter untuk kembali..") 
    return None
  
#crud admin
def menu_admin():
      while True:
        clear()
        print("==MENU ADMIN BANGSALAN LYN PERJUANGAN 4==")  
        print("1. Lihat Data Furnitur")    
        print("2. Tambah Furnitur")
        print("3. Ubah Data Furnitur")
        print("4. Hapus Furnitur")
        print("5. Keluar")
        pilihan = input("pilih menu:")

        if pilihan =="1": #READ/MENAMPILKAN
            clear()
            print("==DATA FURNITUR BANGSALAN LYN")
            for i, item in enumerate (furnitur, start=1):
             print(f"{i}. {item[0]} - Jumlah: {item[1]}")
            input("\nTekan Enter untuk kembali..")
        
        elif pilihan == "2": #CREATE/MENAMBAH
            clear()
            print("==TAMBAHKAN FURNITUR==")
            nama = input("Nama Furnitur")
            jumlah = input("Jumlah")

            if jumlah.isdigit():
                furnitur.append([nama, int(jumlah)])
                print("Data telah ditambahkan!!")
            else:
                print("Jumlah harus angka!!")
            input("\nTekan Enter untuk kembali..")

        elif pilihan == "3": #UPDATE/MENGUBAH
            clear()
            print("==UBAH DATA FURNITUR==")
            for i, item in enumerate(furnitur, start=1):
                print(f"{i}. {item[0]} - Jumlah: {item[1]}")
                pilih = input("\nPilih nomor yang ingin diubah")

                if pilih.isdigit():
                    pilih = int(pilih) - 1
                    if 0 <= pilih < len(furnitur):
                        nama_baru =  input("Nama baru:")
                        jumlah_baru = input("Jumlah baru")
                        if jumlah_baru.isdigit():
                            furnitur[pilih] = [nama_baru, int(jumlah_baru)]     
                            print("Data telah diubah")
                        else:
                            print("Jumlah harus angka!!")
                    else:
                        print("Nomor tak ditemukan!!")
                else:
                    print("input harus angka")
                input("n\Tekan Enter untuk kembali..")

        elif pilihan == "4": #DELETE/MENGHAPUS
            clear()
            print("==HAPUS DATA FURNITUR==")
            for i, item in enumerate(furnitur, start=1):
                print(f"{i}. {item[0]} - jumlah: {item[1]}")
            hapus = input("\nPilih nomor yang ingin dihapus:" )

            if hapus.isdigit():
                hapus = int(hapus) - 1
                if 0 <= hapus < len(furnitur):
                    print(f"{furnitur[hapus][0]} berhasil dihapus")
                    del furnitur[hapus]
                else:
                    print("Nomor tak ditemukan!!")
            else:
                print("Input harus angka!!")
            input("\nTekan Enter untuk kembali..")

        elif pilihan == "5":
            break
        else:
            print("Pilihan tak valid!!")
            input("\nTekan Enter untuk kembali..")

# user biasa
def menu_user():
    while True:
        clear()
        print("==MENU USER BANGSALAN LYN==")
        print("1. Lihat Furnitur")
        print("2. Keluar")    
        pilih = input("Pilih:")
        if pilih == "1":
            clear()
            for i, item in enumerate(furnitur, start=1):
                print(f"{i}. {item[0]} - Jumlah: {item[1]}")
            print("\nMENAMPILKAN FURNITUR BANGSALAN LYN")
        elif pilih == "2":
            print("\nTerima kasih telah berkunjung dan memilih Bangsalan Lyn^-^")
            break

        else:
            print("Pilihan tak valid!!")
            input("\nTekan Enter untuk kembali..")    

#Main program (Utama)
while True:
    clear()
    print("==Pengelolaan Bangsalan Lyn==")            
    print("1. Login")
    print("2. Register")      
    print("3. Keluar")        
    pilih = input("Pilih Menu:")                                            

    if pilih == "1":
        akses = login()
        if akses == "admin":
            menu_admin()
        elif akses == "user":
            menu_user()
        else:
            input("\nTekan Enter untuk kembali..")  

    elif pilih == "2":
        register()
        input("\nTekan Enter untuk kembali.." )

    elif pilih == "3":
        clear()
        print("Terima kasih telah mengakses program Bangsalan Lyn.")
        break

    else:
        print("Pilihan tak valid!!")
        input("\nTekan Enter untuk kembali..")                                                                      
