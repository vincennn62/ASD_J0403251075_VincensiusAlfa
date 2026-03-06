# ==========================================================
# Nama  : Vincensius Alfa S
# NIM   : J0403251075
# Kelas : TPL A2
# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)

# Untuk mencegah angka yang sama pada kode ini menggunakan perpaduan angka unik unik dan juga setiap urutan dibuat dari urutan yang berbeda sehingga tidak sama