from rich.console import Console
from rich.table import Table
from tools import clear, pause

furnitur = [
    ["Kursi Plastik", 10],
    ["Meja Kerja", 3],
    ["Pendingin Ruangan", 2]
]

console = Console()

def tampilkan_furnitur():
    clear()
    table = Table(title="Data Furnitur")
    table.add_column("Nama", style="cyan")
    table.add_column("Jumlah", justify="right", style="green")
    for item in furnitur:
        table.add_row(item[0], str(item[1]))
    console.print(table)

def tambah_furnitur():
    clear()
    nama = input("Nama furnitur: ")
    jumlah = int(input("Jumlah: "))
    furnitur.append([nama, jumlah])
    print("Data berhasil ditambahkan!")
    pause()

def ubah_furnitur():
    tampilkan_furnitur()
    try:
        pilih = int(input("\nPilih nomor furnitur: ")) - 1
        nama_baru = input("Nama baru: ")
        jumlah_baru = int(input("Jumlah baru: "))
        furnitur[pilih] = [nama_baru, jumlah_baru]
        print("Data berhasil diubah!")
    except:
        print("Input salah!")
    pause()

def hapus_furnitur():
    tampilkan_furnitur()
    try:
        pilih = int(input("\nPilih nomor furnitur yang dihapus: ")) - 1
        print(f"{furnitur[pilih][0]} berhasil dihapus!")
        del furnitur[pilih]
    except:
        print("Input salah!")
    pause()
