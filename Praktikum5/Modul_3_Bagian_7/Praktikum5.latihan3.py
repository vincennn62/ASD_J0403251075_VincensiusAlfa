# ==========================================================
# Nama  : Vincensius Alfa S
# NIM   : J0403251075
# Kelas : TPL A2
# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    
    if index == len(data) - 1:
        return data[index]
    
    maks_sisa = cari_maks(data, index + 1)
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]

print("Nilai maksimum:", cari_maks(angka))

# Base casenya berhenti di elemen terakhir.
# Recursive call maju ke elemen berikutnya yang terdapat di dalam list angka (index + 1).
# Tiap angka dibandingkan untuk mencari yang paling besar diantara yang lainnya.
