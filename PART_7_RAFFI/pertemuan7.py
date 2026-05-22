# ==========================================
# GABUNGAN SELURUH KODE: PERTEMUAN 7
# Topik: Lists in Python
# ==========================================

# 1. Indexing List Dasar
angka = [2, 3, 4, 5, 6]
print(angka[2])      # mengakses elemen ketiga

angka[2] = 10        # mengubah elemen ketiga menjadi 10
print(angka) 

angka[2] = angka[4]  # elemen ketiga diisi nilai elemen kelima
print("isi list sekarang:", angka)

# 2. Akses Isi List (UCL)
UCL = [1, 3, 5, 7, 15]
print("Tim ini memiliki UCL:", UCL[0]) 
print("Isi list UCL:", UCL)

# 3. Fungsi len() dan Perubahan Nilai
Puluhan = [10, 20, 70, 50, 90] 
Puluhan[2] = 40
print("Panjang list Puluhan:", len(Puluhan))
print("Isi list Puluhan:", Puluhan)

# 4. Menghapus Elemen dengan del
del Puluhan[2]
print("Panjang setelah del:", len(Puluhan))
print("Isi setelah del:", Puluhan)

# 5. Negative Indexing
Ratusan = [100, 200, 300, 400, 500, 600, 700] 
print("Elemen indeks -7:", Ratusan[-7])

# 6. Kuis 19: Input dan Operasi List
topi_list = [1, 2, 3, 4, 5]
# Langkah 1: Ganti nilai tengah dengan input user
topi_list[2] = int(input("Masukkan angka untuk mengganti nilai tengah: "))
# Langkah 2: Hapus elemen terakhir
del topi_list[-1]
# Langkah 3: Tampilkan panjang list baru
print("Panjang list topi:", len(topi_list))
print("Isi list topi:", topi_list)

# 7. Kuis 20: Manipulasi List Anggota EXO
# Langkah 1: Buat list kosong
exo = []
print("Langkah 1:", exo)

# Langkah 2: Tambah anggota awal
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2:", exo)

# Langkah 3: Tambah anggota dari list lain
anggota_tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for x in anggota_tambahan:
    exo.append(x)
print("Langkah 3:", exo)

# Langkah 4: Hapus anggota tertentu
del exo[6]  # hapus Kris
del exo[7]  # hapus Luhan 
del exo[7]  # hapus Tao 
print("Langkah 4:", exo)

# Langkah 5: Insert anggota di posisi tertentu
exo.insert(len(exo) - 2, "Xiumin")
print("Langkah 5 (Hasil Akhir):", exo)
print("Jumlah total anggota EXO:", len(exo))