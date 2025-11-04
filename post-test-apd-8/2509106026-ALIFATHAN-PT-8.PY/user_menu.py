from tools import clear, pause
from furnitur import tampilkan_furnitur

def menu_user():
    while True:
        clear()
        print("== MENU USER ==")
        print("1. Lihat Furnitur")
        print("2. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_furnitur()
            pause()
        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid!")
            pause()
