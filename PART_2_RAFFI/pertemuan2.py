# =========================================
# 1. Literal pada Python
# =========================================
nama = "Ahmad Raffi Adi Sumartono"
umur = 19
tinggi = 160.0
satuan_umur = "tahun"
satuan_tinggi = "cm"

print("Nama:", nama)
print("Umur:", umur, satuan_umur)
print("Tinggi:", tinggi, satuan_tinggi)


# =========================================
# 2. Integer positif & negatif
# =========================================
print(11111111)     # positif
print(-11111111)    # negatif


# =========================================
# 3. Octal & Hexadecimal
# =========================================
print(0o755)  # octal
print(0o12)

print(0xFF)   # hexadecimal
print(0x1A)


# =========================================
# 4. Float
# =========================================
print(0.4)
print(4.0)

print(.5)     # tanpa 0 di depan
print(5.)     # tanpa 0 di belakang

print(1e3)    # eksponensial (1000)
print(2.5e2)  # eksponensial (250)


# =========================================
# 5. String (petik 1 & 2)
# =========================================
print("Ini pakai petik dua")
print('Ini pakai petik satu')


# =========================================
# 6. Boolean
# =========================================
print(True)
print(False)


# =========================================
# 7. Operator Pangkat
# =========================================
print(2 ** 3)     # int-int
print(2 ** 3.0)   # int-float
print(2.0 ** 3)   # float-int
print(2.0 ** 3.0) # float-float


# =========================================
# 8. Operator Perkalian
# =========================================
print(2 * 3)
print(2 * 3.5)
print(2.5 * 3)
print(2.5 * 3.5)


# =========================================
# 9. Operator Pembagian
# =========================================
print(10 / 2)
print(10 / 2.5)
print(10.0 / 2)
print(10.0 / 2.5)


# =========================================
# 10. Pembagian Integer (//)
# =========================================
print(10 // 3)
print(10 // 3.0)
print(10.0 // 3)
print(10.0 // 3.0)


# =========================================
# 11. Modulo (%)
# =========================================
print(10 % 3)
print(10 % 3.0)
print(10.0 % 3)
print(10.0 % 3.0)


# =========================================
# 12. Unary & Binary
# =========================================
x = 5
y = -x   # unary
z = x + 3  # binary

print("Unary:", y)
print("Binary:", z)


# =========================================
# 13. Subekspresi
# =========================================
hasil = (2 + 3) * (4 - 1)
print("Hasil subekspresi:", hasil)


# =========================================
# 14. Kuis
# =========================================
# contoh gabungan operasi
hasil = (5 + 3) * 2 ** 2 / 4
print("Hasil kuis:", hasil)