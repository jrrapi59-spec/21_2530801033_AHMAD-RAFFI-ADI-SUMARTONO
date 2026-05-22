# ==============================================================================
# TUGAS 13 - ALGORITMA DAN PEMROGRAMAN II
# Nama    : Ahmad Raffi Adi Sumartono
# Topik   : Tuple, Dictionaries, Exceptions in Python
# ==============================================================================

print("=== PART 1: MEMBUAT DAN MENAMPILKAN TUPLE ===")
# Membuat tuple biasa, tuple packing, dan tuple kosong
kucing = ("Caca", "Cici", "Mici")
kucingku = "Joy", "Cemong"
kucing_kosong = ()

print("Isi tuple kucing:", kucing)
print("Isi tuple kucingku:", kucingku)
print("Isi tuple kucing_kosong:", kucing_kosong)
print()


print("=== PART 2: MENGGUNAKAN TUPLE (INDEXING, SLICING, & LOOPING) ===")
kucing_lengkap = ("Caca", "Cici", "Mici", "Cemong", "Joy")

print("Elemen indeks 0 :", kucing_lengkap[0])
print("Elemen indeks -1:", kucing_lengkap[-1])
print("Slicing [:1]     :", kucing_lengkap[:1])
print("Slicing [:-2]    :", kucing_lengkap[:-2])

print("Looping isi tuple:")
for element in kucing_lengkap:
    print("-", element)
print()


print("=== PART 3: SIFAT IMMUTABLE TUPLE (MEMODIFIKASI TUPLE) ===")
# Catatan: Tuple bersifat tidak bisa diubah (immutable). 
# Kode di bawah ini aslinya akan menghasilkan error jika dijalankan langsung.
print("Tuple awal:", kucing_lengkap)

# kucing_lengkap.append("Lala")        # -> AttributeError (tidak bisa menambah)
# del kucing_lengkap[0]                 # -> TypeError (tidak bisa menghapus elemen tertentu)
# kucing_lengkap["Caca"] = ["chiko"]    # -> TypeError (tidak bisa mengubah nilai elemen)

print("[INFO] Operasi .append(), del elemen, dan assignment pada Tuple sengaja di-disable karena memicu error.")
print()


print("=== PART 4: OPERATOR DAN FUNGSI PADA TUPLE (len, +, *, in, not in) ===")
nomor = (25, 30, 80, 10, 59)

n1 = nomor + (15, 7)    # Menggabungkan dua tuple
n2 = nomor * 2          # Menduplikat isi tuple

print("Panjang tuple n2 (len) :", len(n2))
print("Hasil penggabungan (+) :", n1)
print("Hasil duplikasi (*)    :", n2)
print("Apakah 7 ada di nomor? :", 7 in nomor)
print("Apakah -7 tidak ada?   :", -7 not in nomor)
print()


print("=== PART 5: DICTIONARY DI PYTHON ===")
# Membuat dictionary, memodifikasi value, dan menghapus key
dictionary = {"rapi": 90, "dimas": 100, "azha": 99}
print("Dictionary awal:", dictionary)

# Modifikasi nilai pada key "azha"
dictionary["azha"] = 90
# Menghapus key "rapi"
if "rapi" in dictionary:
    del dictionary["rapi"]

print("Dictionary setelah dimodifikasi dan dihapus:")
for nama in dictionary:
    print(f"Nama: {nama} -> Nilai: {dictionary[nama]}")
print()


print("=== PART 6: EXCEPTION HANDLING (PENANGANAN ERROR) ===")
# Menangani single exception (ValueError)
try:
    print("[Single Exception Test]")
    angka = int(input("Masukkan angka: "))
    hasil = angka * 2 + 15
    print("Hasil perhitungan:", hasil)
except ValueError:
    print("Terjadi Error: Input harus berupa angka!")
print()

# Menangani multiple exception (ValueError dan ZeroDivisionError)
try:
    print("[Multiple Exception Test]")
    angka = int(input("Masukkan angka pembagi: "))
    hasil = 100 / angka + 15   
    print("Hasil pembagian:", hasil)
except (ValueError, ZeroDivisionError):
    print("Terjadi Error: Input harus angka dan tidak boleh nol (0)!")
print()

print("=== PROGRAM SELESAI ===")