# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Vincensius Alfa Setyawan
# NIM   : J0403251075
# Kelas : TPL A2
# ==========================================================

NAMA_FILE = "stok_barang.txt"

# Fungsi: Membaca data dari file
def baca_stok(nama_file):

    stok_dict = {}

    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()
                if baris == "":
                    continue

                data = baris.split(",")
                if len(data) != 3:
                    continue

                kode, nama, stok_str = data
                try:
                    stok_int = int(stok_str)
                except ValueError:
                    continue

                stok_dict[kode] = {
                    "nama": nama,
                    "stok": stok_int
                }
    except FileNotFoundError:
        pass  # jika file belum ada, stok kosong

    return stok_dict


# Fungsi: Menyimpan data ke file
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode, data in stok_dict.items():
            baris = f"{kode},{data['nama']},{data['stok']}\n"
            f.write(baris)


# Fungsi: Menampilkan semua data
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    if not stok_dict:
        print("Stok barang masih kosong.")
        return

    print("\nKode | Nama Barang | Stok")
    print("-" * 30)
    for kode, data in stok_dict.items():
        print(f"{kode} | {data['nama']} | {data['stok']}")

# Fungsi: Cari barang berdasarkan kode
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip()

    if kode in stok_dict:
        data = stok_dict[kode]
        print("Barang ditemukan:")
        print(f"Kode : {kode}")
        print(f"Nama : {data['nama']}")
        print(f"Stok : {data['stok']}")
    else:
        print("Barang tidak ditemukan.")


# Fungsi: Tambah barang baru
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ").strip()

    try:
        stok_awal = int(input("Masukkan stok awal: "))
        if stok_awal < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Stok harus berupa angka.")
        return

    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan.")
    simpan_stok(NAMA_FILE, stok_dict)

# Fungsi: Update stok barang
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).\
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: "))
        if jumlah < 0:
            print("Jumlah tidak boleh negatif.")
            return
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    stok_sekarang = stok_dict[kode]["stok"]

    if pilihan == "1":
        stok_dict[kode]["stok"] = stok_sekarang + jumlah
        print("Stok berhasil ditambah.")
        simpan_stok(NAMA_FILE, stok_dict)

    elif pilihan == "2":
        if stok_sekarang - jumlah < 0:
            print("Error: stok tidak boleh negatif.")
        else:
            stok_dict[kode]["stok"] = stok_sekarang - jumlah
            print("Stok berhasil dikurangi.")
            simpan_stok(NAMA_FILE, stok_dict)
    else:
        print("Pilihan tidak valid.")

# Menu Utama
def main():
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
