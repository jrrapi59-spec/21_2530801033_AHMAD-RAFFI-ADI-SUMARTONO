# ============================================================
# GABUNGAN SELURUH KODE: PERTEMUAN 11
# Topik: Returning a Result from a Function
# Nama: Ahmad Raffi Adi Sumartono
# ============================================================

# 1. Return tanpa ekspresi: memanggil fungsi tanpa argumen
def Halo():
    print("Halo Tri")
    print("Meet")
    return

Halo()

# 2. Return tanpa ekspresi: memanggil fungsi dengan argumen False
def Akun(aktif):
    if not aktif:
        print("password akun salah, akses ditolak!")
        return
    print("Akses berhasil")

Akun(False)

# 3. Return dengan ekspresi: menyimpan nilai ke variabel
def luas_persegi(sisi):
    return sisi * sisi

Hasil_luas = luas_persegi(5)
print(Hasil_luas)

# 4. Return dengan ekspresi: mengabaikan nilai return
def kali(a, b):
    return a * b

kali(4, 3) 
print("Hebat kamu Bud")

# 5. Penggunaan Keyword None
def hitung(n):
    if (n % 3 == 0):
        return True

print(hitung(15)) # Hasil: True
print(hitung(13)) # Hasil: None

# 6. List sebagai argument dari fungsi
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s

print(list_sum([5, 4, 3]))

# 7. Fungsi dengan list sebagai return value
def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list

print(strange_list_fun(5))

# 8. Kuis 26: Fungsi Penjumlahan List
def list_sum_2(lst):
    s = 0
    for elem in lst:
        s += elem
    return s

# 9. Kuis 27: Cek Bilangan Prima (Optimasi akar kuadrat)
def cek_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Apakah 7 prima?", cek_prima(7))
print("Apakah 4 prima?", cek_prima(4))

# 10. Kuis 28: Konversi Konsumsi Bahan Bakar (L/100km & MPG)
def liter100km_ke_mpg(liter):
    mil_per_100km = 100 / 1.609344
    galon = liter / 3.785411784
    return mil_per_100km / galon

def mpg_ke_liter100km(miles):
    km_per_mil = 1.609344
    liter_per_galon = 3.785411784
    return (100 * liter_per_galon) / (miles * km_per_mil)

# Test Kuis 28
print(liter100km_ke_mpg(3.9))
print(liter100km_ke_mpg(7.5))
print(liter100km_ke_mpg(10.))
print(mpg_ke_liter100km(60.3))
print(mpg_ke_liter100km(31.4))
print(mpg_ke_liter100km(23.5))