# =========================================
# 1. Comparison Operator
# =========================================
x = 1
y = 2
z = 3

print(x == y)
print(x == z)
print(z == y)

print(x != y)
print(x != z)
print(z != y)

print(x > y)
print(x > z)

print(x < y)
print(x < z)
print(z < y)

print(x >= y)
print(x >= z)
print(z >= y)

print(x <= y)
print(x <= z)
print(z <= y)


# =========================================
# 2. Kuis 11
# =========================================
n = int(input("Masukkan angka: "))

if n < 100:
    print("false")
else:
    print("true")


# =========================================
# 3. If tunggal
# =========================================
x = 20
if x == 20:
    print("x sama dengan 20")


# =========================================
# 4. Rangkaian if
# =========================================
x = 20
if x < 100:
    print("x kurang dari 100")
if x > 5:
    print("x lebih dari 5")
if x == 20:
    print("x sama dengan 20")


# =========================================
# 5. If - else
# =========================================
x = 200
if x < 100:
    print("x kurang dari 100")
else:
    print("x lebih dari 100")


# =========================================
# 6. If - elif - else
# =========================================
x = 200
if x < 100:
    print("x < 100")
elif x < 150:
    print("x < 150")
elif x == 200:
    print("x sama dengan 200")
else:
    print("x lebih besar dari 200")


# =========================================
# 7. Membandingkan 2 angka
# =========================================
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if angka1 > angka2:
    angka_besar = angka1
else:
    angka_besar = angka2

print("Angka yang lebih besar adalah:", angka_besar)


# =========================================
# 8. Kuis 12 (3 angka terbesar)
# =========================================
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

if angka1 > angka2 and angka1 > angka3:
    angka_besar = angka1
elif angka2 > angka1 and angka2 > angka3:
    angka_besar = angka2
else:
    angka_besar = angka3

print("Angka terbesar adalah:", angka_besar)


# =========================================
# 9. Fungsi max()
# =========================================
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

angka_besar = max(angka1, angka2, angka3)
print("Angka terbesar (pakai max):", angka_besar)


# =========================================
# 10. Kuis 13 (pajak)
# =========================================
pendapatan = int(input("Masukkan pendapatan per tahun: "))

if pendapatan <= 60000000:
    pajak = 0.05 * pendapatan
elif pendapatan <= 250000000:
    pajak = 0.15 * pendapatan
elif pendapatan <= 500000000:
    pajak = 0.25 * pendapatan
else:
    pajak = 0.30 * pendapatan

print("Pajak yang harus dibayar:", pajak, "Rupiah")