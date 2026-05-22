# ============================================================
# GABUNGAN SELURUH KODE: PERTEMUAN 9
# Topik: Sorting and Operations Lists in Python
# Nama: Ahmad Raffi Adi Sumartono
# ============================================================

# 1. Bubble Sort Dasar [cite: 56]
my_list = [8, 10, 6, 2, 4]
swapped = True
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print("Hasil Bubble Sort Dasar:", my_list)

# 2. Interactive Bubble Sort (Input Pengguna) [cite: 58]
def bubble_sort_interaktif():
    my_list = []
    swapped = True
    num = int(input("Masukkan panjang elemen yang akan diurutkan: "))

    for i in range(num):
        val = float(input(f"Masukkan elemen ke-{i + 1}: "))
        my_list.append(val)

    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                swapped = True
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    
    print("\nSorted:")
    print(my_list)

# 3. Method sort() dan reverse() bawaan Python 
def demo_method_bawaan():
    # Menggunakan .sort()
    list_a = [8, 10, 6, 2, 4]
    list_a.sort()
    print("Hasil .sort():", list_a)

    # Menggunakan .reverse()
    list_b = [5, 4, 3, 2, 1]
    list_b.reverse()
    print("Hasil .reverse():", list_b)

# 4. Slicing List (Berbagai Variasi) [cite: 14, 17, 20, 23]
# Contoh Slice [awal:akhir]
angka_awal = [5, 10, 15, 20, 25, 30]
print("Slice [-5:4]:", angka_awal[-5:4])

# Contoh Slice dengan langkah negatif
angka = [10, 20, 30, 40, 50]
print("Slice [:-4]:", angka[:-4])

# Contoh Slice s/d akhir & len()
puluhan = [10, 20, 30, 40, 50, 60]
puluhan_baru = puluhan[3:]
print("Hasil slice [3:]:", puluhan_baru)
print("Jumlah elemen hasil slice:", len(puluhan_baru))

# Menyalin List dengan slice [:]
ratusan = [120, 230, 340, 450, 560]
new_ratusan = ratusan[:]
ratusan[0] = 777
print("List awal diubah:", ratusan)
print("List hasil copy (tetap):", new_ratusan)

# 5. Menghapus dengan Slice [cite: 26]
listtt = [11, 22, 33, 44, 55, 66, 77]
del listtt[-5:-1]
print("Setelah del slice [-5:-1]:", listtt)

# 6. Operator 'in' dan 'not in' [cite: 29]
EPL = ["Man City", "Arsenal", "Liverpool", "Chelsea", "MU"]
print("Apakah Man City ada di EPL?", "Man City" in EPL)
print("Apakah Real Madrid ada di EPL?", "Real Madrid" in EPL)

# 7. Mencari Nilai Terbesar 
my_list_acak = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list_acak[0]
for i in my_list_acak:
    if i > largest:
        largest = i
print("Nilai terbesar:", largest)

# 8. Kuis 22: Menghapus Angka Duplikat (Unique List) 
list_berulang = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list_uniq = []
for angka in list_berulang:
    if angka not in list_uniq:
        list_uniq.append(angka)
print(f"List asli: {list_berulang}")
print(f"List bersih (uniq): {list_uniq}")

# Menjalankan fungsi demo jika diperlukan
# bubble_sort_interaktif() 
demo_method_bawaan()