# ==============================================================================
# PERTEMUAN 12: SCOPE DAN MULTI-PARAMETER FUNCTION IN PYTHON
# ==============================================================================
print("=== PERTEMUAN 12: SCOPE & REKURSIF ===")

# 1. Demonstrasi Variabel Lokal & Global
bilangan = 100  # Ini Variabel Global

def penjumlahan(x):
    bilangan_lokal = 15  # Ini Variabel Lokal
    return x + bilangan_lokal

print("Hasil fungsi penjumlahan (Akses variabel lokal internal):", penjumlahan(44))
print("Akses Variabel Global 'bilangan':", bilangan)
# Note: Memanggil 'bilangan_lokal' di luar fungsi akan menyebabkan NameError.

# 2. Fungsi Fibonacci Iteratif
print("\n--- Deret Fibonacci Iteratif ---")
def fibonacci_iteratif(n):
    if n < 1:
        return None
    if n == 1 or n == 2:
        return 1
    
    elem1 = 1
    elem2 = 1
    for i in range(3, n + 1):
        hasil_jumlah = elem1 + elem2
        elem1 = elem2
        elem2 = hasil_jumlah
    return elem2

# Cetak suku ke-1 sampai ke-6
for i in range(1, 7):
    print(f"Suku ke-{i} -> {fibonacci_iteratif(i)}")

# 3. Rekursif Faktorial
print("\n--- Rekursif Faktorial ---")
def factorial(n):
    if n < 0:
        return None      
    if n == 0 or n == 1:
        return 1                  
    return n * factorial(n - 1)

# Menghitung faktorial dari 0 sampai 5
for i in range(6):
    print(f"Faktorial {i}! -> {factorial(i)}")

# 4. Rekursif Fibonacci
print("\n--- Rekursif Fibonacci ---")
def fibonacci_rekursif(n):
    if n < 1:
        return None      
    if n == 1 or n == 2:
        return 1          
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)

# Cetak deret suku ke-1 sampai ke-6 menggunakan rekursif
for i in range(1, 7):
    print(f"Suku ke-{i} (Rekursif) -> {fibonacci_rekursif(i)}")

print("==============================================================================")
print("=== PROGRAM GABUNGAN SELESAI ===")