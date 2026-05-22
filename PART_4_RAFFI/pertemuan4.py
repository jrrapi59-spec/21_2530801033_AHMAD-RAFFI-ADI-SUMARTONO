# =========================================
# 1. Input sederhana
# =========================================
nama = input("Masukkan nama: ")
print("Halo,", nama)


# =========================================
# 2. Input dengan argumen
# =========================================
umur = input("Masukkan umur: ")
print("Umur kamu:", umur)


# =========================================
# 3. Input tanpa konversi (string)
# =========================================
a = input("Masukkan angka pertama: ")
b = input("Masukkan angka kedua: ")

print("Hasil (tanpa konversi):", a + b)  # akan digabung, bukan dijumlah


# =========================================
# 4. Konversi ke float
# =========================================
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print("Hasil penjumlahan:", a + b)


# =========================================
# 5. Menghitung sisi miring (pakai variabel)
# =========================================
alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))

hypo = (alas**2 + tinggi**2) ** 0.5
print("Sisi miring:", hypo)


# =========================================
# 6. Sisi miring tanpa variabel
# =========================================
alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))

print("Sisi miring:", round((alas**2 + tinggi**2) ** 0.5, 2))


# =========================================
# 7. Operator Konkatenasi
# =========================================
teks1 = "Halo "
teks2 = "Dunia"
print(teks1 + teks2)


# =========================================
# 8. Operator Replikasi
# =========================================
print("Python " * 3)


# =========================================
# 9. Konversi ke string
# =========================================
angka = 10
teks = "Nilai = " + str(angka)

print(teks)


# =========================================
# 10. Melihat tipe data
# =========================================
x = 5
print("Tipe data x:", type(x))


# =========================================
# 11. Kuis 7 (kalkulator sederhana)
# =========================================
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)

print("Selamat kamu sudah pintar matematika")


# =========================================
# 12. Kuis 8 (pecahan bertingkat)
# =========================================
x = float(input("Masukkan nilai x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("Hasil y:", y)


# =========================================
# 13. Kuis 9 (hitung waktu)
# =========================================
jam = int(input("Masukkan jam awal: "))
menit = int(input("Masukkan menit awal: "))
durasi = int(input("Masukkan durasi (menit): "))

total_menit = menit + durasi
tambah_jam = total_menit // 60
sisa_menit = total_menit % 60

jam_akhir = (jam + tambah_jam) % 24

print("Waktu akhir:", jam_akhir, ":", sisa_menit)