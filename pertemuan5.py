# ==============================================================================
# PERTEMUAN 5: MAKING DECISION IN PYTHON
# ==============================================================================
print("=== PERTEMUAN 5: MAKING DECISION ===")

# 1. Demonstration Comparison Operator
print("Hasil Comparison Operator:")
x_comp, y_comp, z_comp = 1, 2, 3
print("x == y ->", x_comp == y_comp)
print("x != y ->", x_comp != y_comp)
print("x < z  ->", x_comp < z_comp)
print("z >= y ->", z_comp >= y_comp)

# 2. Mencari Angka Terbesar Manual (If-Elif-Else) & Fungsi max()
print("\n--- Mencari Angka Terbesar ---")
# Contoh input statis (bisa diganti int(input()) jika ingin interaktif)
angka1 = 50
angka2 = 60
angka3 = 20

# Cara manual If-Elif-Else
if angka1 >= angka2 and angka1 >= angka3:
    terbesar_manual = angka1
elif angka2 >= angka1 and angka2 >= angka3:
    terbesar_manual = angka2
else:
    terbesar_manual = angka3
print(f"Angka terbesar (Manual If) dari ({angka1}, {angka2}, {angka3}) adalah: {terbesar_manual}")

# Cara menggunakan fungsi max()
angka_besar_func = max(angka1, angka2, angka3)
print(f"Angka terbesar (Fungsi max) dari ({angka1}, {angka2}, {angka3}) adalah: {angka_besar_func}")

# 3. Kuis 13: Perhitungan Pajak Pendapatan Per Tahun
print("\n--- Simulasi Kuis 13: Pajak Pendapatan ---")
pendapatan = 80000000  # Contoh pendapatan 80 Juta per tahun

if pendapatan <= 60000000:
    pajak = 0.05 * pendapatan
elif pendapatan <= 250000000:
    pajak = 0.15 * pendapatan
elif pendapatan <= 500000000:
    pajak = 0.25 * pendapatan
else:
    pajak = 0.30 * pendapatan

print(f"Pendapatan per tahun: Rp {pendapatan}")
print(f"Pajak yang harus dibayar adalah: Rp {pajak} Rupiah")
print("==============================================================================\n")