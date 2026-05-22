# =========================================
# 1. Membuat dan menggunakan variable
# =========================================
nim = 2530801033
nomer_telpon = 82230749163
nama = "Ahmad Raffi Adi Sumartono"

print("nim =", nim)
print("nomer telpon =", nomer_telpon)
print("nama =", nama)


# =========================================
# 2. Case Sensitive (Nama vs nama)
# =========================================
Nama = "Budi"

print("Variable Nama:", Nama)
# print(nama)  # ERROR kalau diaktifkan (beda huruf besar kecil)


# =========================================
# 3. Mengubah nilai variable umur
# =========================================
umur = 19
print("Umur awal:", umur)

umur = 20
print("Umur setelah diubah:", umur)


# =========================================
# 4. Variable Tabungan
# =========================================
tabungan = 1000000
tabungan = tabungan + 2000000

print("Total tabungan:", tabungan)


# =========================================
# 5. Shortcut Operators
# =========================================
x = 10
x += 5   # tambah
x -= 3   # kurang
x *= 2   # kali
x /= 4   # bagi

print("Hasil shortcut operator:", x)


# =========================================
# 6. Simple Mathematical Problem
# =========================================
skor = 100
skor += 20   # bonus
skor -= 10   # penalti
skor *= 2    # dikali

print("Skor akhir:", skor)


# =========================================
# 7. Kuis 3 (jumlah tabungan)
# =========================================
ayu = 100000
bagus = 150000
citra = 200000

jumlah_tabungan = ayu + bagus + citra
print("Total tabungan:", jumlah_tabungan)


# =========================================
# 8. Kuis 4 (konversi miles <-> km)
# =========================================
miles = 10
km = miles * 1.61

print("Miles ke KM:", round(km, 2))

km2 = 16.1
miles2 = km2 / 1.61

print("KM ke Miles:", round(miles2, 2))


# =========================================
# 9. Kuis 5 (rumus y = 3x − 6x² − 1)
# =========================================
x = 2
y = 3*x - 6*(x**2) - 1

print("Nilai y:", y)