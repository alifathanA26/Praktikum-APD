from tools import clear, pause
from furnitur import tampilkan_furnitur, tambah_furnitur, ubah_furnitur, hapus_furnitur

def menu_admin():
    while True:
        clear()
        print("== MENU ADMIN ==")
        print("1. Lihat Furnitur")
        print("2. Tambah Furnitur")
        print("3. Ubah Furnitur")
        print("4. Hapus Furnitur")
        print("5. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_furnitur()
            pause()
        elif pilih == "2":
            tambah_furnitur()
        elif pilih == "3":
            ubah_furnitur()
        elif pilih == "4":
            hapus_furnitur()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid!")
            pause()
