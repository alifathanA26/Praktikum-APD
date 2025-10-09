import math 
# Input sisi segitiga
A = float(input("Masukkan sisi A: "))
B = float(input("Masukkan sisi B: "))
C = float(input("Masukkan sisi C: "))

# syarat segitiga
if (A + B > C) and (A + C > B) and (B + C > A):

    # Tentukan jenis segitiga
    if A == B == C:
        jenis = "Segitiga Sama Sisi"
    elif A == B or B == C or A == C:
        jenis = "Segitiga Sama Kaki"
    else:
        jenis = "Segitiga Sembarang"
    
    # Hitung luas (rumus Heron)
    s = (A + B + C) / 2
    luas = math.sqrt(s * (s - A) * (s - B) * (s - C))
    
    # Tampilkan hasil
    print(jenis)
    print("Luas segitiga =", luas)
else:
    print("Bukan segitiga")

username_benar = "alfath"  
password_benar = "026"    
max_kesalahan = 5
berhasil = False
    
for i in range(max_kesalahan):
        print(f"Percobaan ke-{i+1}")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username == username_benar and password == password_benar:
            print("Autentikasi berhasil! Selamat datang di python math.")
            berhasil = True
            break  
        else:
            sisa = max_kesalahan - (i + 1)
            if sisa > 0:
                print(f"Username atau password salah. Sisa percobaan: {sisa}")
                
             

while True:
        print("\n=== PROGRAM HITUNG SEGITIGA ===")
        print("Menu:")
        print("1. Hitung segitiga")
        print("2. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga = {luas}")

        elif pilihan == "2":
            print("Terima kasih, program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


