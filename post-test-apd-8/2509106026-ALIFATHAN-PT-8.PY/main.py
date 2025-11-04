from tools import clear, pause
from auth import login

while True:
    clear()
    print("== SISTEM PENGELOLAAN BANGSALAN LYN ==")
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
 