# ==========================================================
# Nama  : Vincensius Alfa S
# NIM   : J0403251075
# Kelas : TPL A2
# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):

    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)

    countdown(n - 1)

    print("Keluar:", n)

countdown(3)