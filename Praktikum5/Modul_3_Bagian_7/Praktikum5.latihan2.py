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

#"Masuk" dicetak saat fungsi dipanggil (turun).
#"Keluar" dicetak setelah fungsi di bawahnya selesai (naik).
#Jadi ini diibaratkan kita sedang menumpuk piring untuk dicuci(masuk), dari tumpukan tersebut piring terakhir lah yang akan dicuci duluan
