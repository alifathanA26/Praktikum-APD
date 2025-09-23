# Program untuk memproses list dengan tipe data campuran
# menggunakan pernyataan print manual 

# Membuat list dengan tipe data campuran
'data_list = (1, 3.14, "hello", True, 2, 2.71, "world", False, 5)

print("=== LIST ASLI ===")
print("Isi list:", data_list)
print()

# Menampilkan setiap elemen dengan tipenya secara manual
print("=== TIPE DATA ELEMEN (MANUAL) ===")
print(f"Elemen 0: {data_list[0]} -> Tipe: {type(data_list[0])}")
print(f"Elemen 1: {data_list[1]} -> Tipe: {type(data_list[1])}")
print(f"Elemen 2: {data_list[2]} -> Tipe: {type(data_list[2])}")
print(f"Elemen 3: {data_list[3]} -> Tipe: {type(data_list[3])}")
print(f"Elemen 4: {data_list[4]} -> Tipe: {type(data_list[4])}")
print(f"Elemen 5: {data_list[5]} -> Tipe: {type(data_list[5])}")
print(f"Elemen 6: {data_list[6]} -> Tipe: {type(data_list[6])}")
print(f"Elemen 7: {data_list[7]} -> Tipe: {type(data_list[7])}")
print(f"Elemen 8: {data_list[8]} -> Tipe: {type(data_list[8])}")


# Menghitung elemen int dan float secara manual 
elemen_int = [x for x in data_list if isinstance(x, int) and not isinstance(x, bool)]
elemen_float = [x for x in data_list if isinstance(x, float)]

print("=== ANALISIS INT DAN FLOAT (SEBELUM KONVERSI) ===")
print("Elemen int:", elemen_int)
print("Elemen float:", elemen_float)
print("Jumlah elemen int:", len(elemen_int))
print("Jumlah elemen float:", len(elemen_float))
print()

# Mengkonversi tipe data secara manual tanpa perulangan
print("=== KONVERSI TIPE DATA (MANUAL) ===")
# Konversi int ke string secara manual
print(f"Mengkonversi int {data_list[0]} ke str: '{str(data_list[0])}'")
print(f"Mengkonversi int {data_list[4]} ke str: '{str(data_list[4])}'")
print(f"Mengkonversi int {data_list[8]} ke str: '{str(data_list[8])}'")

# Konversi float ke int secara manual
print(f"Mengkonversi float {data_list[1]} ke int: {int(data_list[1])}")
print(f"Mengkonversi float {data_list[5]} ke int: {int(data_list[5])}")
print()

# Membuat list baru dengan tipe data yang dikonversi secara manual
list_terkonversi = [
    str(data_list[0]),      # int -> str
    int(data_list[1]),      # float -> int
    data_list[2],           # string tetap string
    data_list[3],           # boolean tetap boolean
    str(data_list[4]),      # int -> str
    int(data_list[5]),      # float -> int
    data_list[6],           # string tetap string
    data_list[7],           # boolean tetap boolean
    str(data_list[8])       # int -> str
]

print("===SETELAH KONVERSI===")
print("List terkonversi", list_terkonversi)
print()

# Menampilkan elemen yang sudah dikonversi secara manual
print("=== TIPE DATA ELEMEN TERKONVERSI (MANUAL) ===")
print(f"Elemen 0: {list_terkonversi[0]} -> Tipe: {type(list_terkonversi[0])}")
print(f"Elemen 1: {list_terkonversi[1]} -> Tipe: {type(list_terkonversi[1])}")
print(f"Elemen 2: {list_terkonversi[2]} -> Tipe: {type(list_terkonversi[2])}")
print(f"Elemen 3: {list_terkonversi[3]} -> Tipe: {type(list_terkonversi[3])}")
print(f"Elemen 4: {list_terkonversi[4]} -> Tipe: {type(list_terkonversi[4])}")
print(f"Elemen 5: {list_terkonversi[5]} -> Tipe: {type(list_terkonversi[5])}")
print(f"Elemen 6: {list_terkonversi[6]} -> Tipe: {type(list_terkonversi[6])}")
print(f"Elemen 7: {list_terkonversi[7]} -> Tipe: {type(list_terkonversi[7])}")
print(f"Elemen 8: {list_terkonversi[8]} -> Tipe: {type(list_terkonversi[8])}")


# Menghitung elemen int dan float setelah konversi menggunakan list comprehension
elemen_int_baru = [x for x in list_terkonversi if isinstance(x, int) and not isinstance(x, bool)]
elemen_float_baru = [x for x in list_terkonversi if isinstance(x, float)]

print("=== ANALISIS INT DAN FLOAT TERAKHIR (SETELAH KONVERSI) ===")
print("Elemen int setelah konversi:", elemen_int_baru)
print("Elemen float setelah konversi:", elemen_float_baru)
print("Jumlah elemen int setelah konversi:", len(elemen_int_baru))
print("Jumlah elemen float setelah konversi:", len(elemen_float_baru))

print("\n======")
print(" memproses list dengan tipe data campuran")
print("""setelah operasi dilakukan secara manual dengan pernyataan print""")