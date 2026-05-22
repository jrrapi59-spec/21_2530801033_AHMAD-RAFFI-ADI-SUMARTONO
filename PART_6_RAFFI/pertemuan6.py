
# 1. While True (loop tanpa henti)
while True:
   print("perulangan ini bakal lanjut terus")



# 2. While dengan pengurangan

angka = 5
while angka > 2:
    print("While turun:", angka)
    angka -= 1



# 3. Menghitung ganjil & genap

angka_genap = 0
angka_ganjil = 0

while True:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
    
    if angka == 0:
        break
    
    if angka % 2 == 0:
        angka_genap += 1
    else:
        angka_ganjil += 1

print("Jumlah genap:", angka_genap)
print("Jumlah ganjil:", angka_ganjil)



# 4. Kuis 15 (tebak angka 777)

angka = int(input("Masukkan angka (tebak 777): "))

while angka != 777:
    print("Hahaha, kamu nyangkut di loop saya")
    angka = int(input("Masukkan angka lagi: "))

print("Selamat, Muggle! kamu bebas sekarang.")



# 5. For range contoh

print("range(10):")
for i in range(10):
    print(i)

print("range(2,8):")
for i in range(2, 8):
    print(i)

print("range(2,8,3):")
for i in range(2, 8, 3):
    print(i)



# 6. Pangkat 2 (eksponensial)

kuadrat = 1
for i in range(11):
    print("2 pangkat", i, "=", kuadrat)
    kuadrat *= 2



# 7. Break

for i in range(1, 6):
    if i == 4:
        break
    print("Break:", i)



# 8. Continue

for i in range(1, 5):
    if i == 2:
        continue
    print("Continue:", i)



# 9. Kuis 16 (tebak 888)

while True:
    angka = int(input("Masukkan angka (tebak 888): "))
    
    if angka == 888:
        print("Selamat, tebakan benar!")
        break
    else:
        print("Salah, coba lagi!")



# 10. Kuis 17 (hapus vokal)

kata = input("Masukkan kata: ").upper()

for huruf in kata:
    if huruf in "AIUEO":
        continue
    print(huruf, end=" ")
print()



# 11. While dengan else

angka = 1
while angka < 5:
    print("While else:", angka)
    angka += 1
else:
    print("Perulangan selesai")



# 12. For dengan else

for i in range(5):
    print("For else:", i)
else:
    print("Loop selesai, nilai terakhir i =", i)



# 13. Ekspresi logika (not)

x = 100
y = not not x
print("Nilai y:", y)



# 14. Logical vs Bitwise

x = 5
y = 3

print("Logical AND:", x and y)
print("Logical NOT x:", not x)
print("Bitwise NOT x:", ~x)



# 15. Binary Shifting

x = 77
print("Geser kanan (x >> 1):", x >> 1)
print("Geser kiri (x << 2):", x << 2)