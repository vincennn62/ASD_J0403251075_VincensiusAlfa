# ==========================================================
# Nama  : Vincensius Alfa S
# NIM   : J0403251075
# Kelas : TPL A2
# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16

# Alur program tersebut yaitu menghitung angka depan(a) yang dipangkatkan sebanyak angka belakang(n) 
# Base case yaitu sebuah kondisi berhenti (n == 0)
# Recursive call berfungsi memanggil dirinya sendiri dengan nilai lebih kecil (n - 1)
