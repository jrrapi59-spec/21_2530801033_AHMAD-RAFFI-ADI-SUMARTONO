# ============================================================
# GABUNGAN SELURUH KODE: PERTEMUAN 10
# Topik: List in Advance Applications in Python
# Nama: Ahmad Raffi Adi Sumartono
# ============================================================

# 1. List Comprehensions (Pangkat & Filter Genap)
pangkat = [x ** 2 for x in range(10)]
print(pangkat) [cite: 15]

dua_pangkat = [2 ** i for i in range(8)]
print(dua_pangkat) [cite: 15]

genap = [x for x in pangkat if x % 2 == 0]
print(genap) [cite: 15]

# 2. Array 2 Dimensi (Papan Catur 4x4)
KOSONG = "A" 
papan_catur = []
for i in range(4):
    baris = [KOSONG for i in range(4)] 
    papan_catur.append(baris) [cite: 17]

for baris in papan_catur:
    print(baris) [cite: 17]

# 3. List Multidimensi (Tabel Temperatur 7x12)
temperatur = [[0.0 for jam in range(12)] for hari in range(7)] [cite: 19]

for catatan in temperatur:
    print(catatan) [cite: 19]

# 4. Fungsi Berparameter
def sapa_teman(nama):
    print("Halo " + nama + ", selamat belajar coding!") [cite: 21]

sapa_teman("Sota") [cite: 21]

# 5. Kuis 1: Filter Genap dan Perkalian 3
# Program menghasilkan list hasil perkalian 3 dengan angka genap dari 1-10
hasil = [x * 3 for x in range(1, 11) if x % 2 == 0] [cite: 23]
print(hasil) [cite: 23]

# 6. Kuis 2: Matriks 3x3
array_2d = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]] [cite: 25]

print("Array 2D:")
for row in array_2d:
    print(row) [cite: 25]

# 7. Kuis 3: Flatten List (Mengubah list multidimensi jadi 1D)
data = [[2, 4], [6, 8], [10, 12]]
flatten = [x for sublist in data for x in sublist] [cite: 27]
print(flatten) [cite: 27]

# 8. Slice 4: Fungsi Hitung Luas Persegi Panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar [cite: 29]

hasil_luas = luas_persegi_panjang(8, 5) [cite: 29]
print(hasil_luas) [cite: 29]