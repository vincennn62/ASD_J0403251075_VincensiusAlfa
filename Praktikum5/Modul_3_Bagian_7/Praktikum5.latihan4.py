# ==========================================================
# Nama  : Vincensius Alfa S
# NIM   : J0403251075
# Kelas : TPL A2
# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    
    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)

# Jumlah kombinasi yang dihasilkan adalah 2^2, setiap posisi punya 2 pilihan ada n posisi
# Total kemungkinan = 2*2 = 2^2, pangkat 2 itu bisa diubah dengan berapa aja, kita ibarat kan saja n
