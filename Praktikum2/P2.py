#======================================
# Latihan Praktikum 2
# Lat 1 Load Data File
#======================================

#fungsi untuk membaca data dari file dan mengembalikan sebagai dictionary
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} 
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            data_dict[nim] = {"nama": nama,"nilai": int(nilai)}
    return data_dict

buka_data = baca_data(nama_file)
print("Jumlah Data :", len(buka_data))


#======================================
# Latihan Praktikum 2
# Lat 2 Fungsi menampilkan data
#======================================

#fungsi untuk menampilkan data mahasiswa
def tampil_data(data_dict):
    print("\n-------- Data Mahasiswa --------")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    print("-"*32)

    for nim, data in data_dict.items():
        print(f"{nim:<10} | {data['nama']:<12} | {data['nilai']:>5}")

#tampil_data(buka_data)


#======================================
# Latihan Praktikum 2 
# Lat 3 Fungsi mencari data
#======================================

#fungsi untuk mencari data mahasiswa berdasarkan NIM
def cari_data(data_dict):
    nim_cari = input("Masukkan NIM yang dicari : ")

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("=== Data Mahasiswa Ditemukan ===")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data Mahasiswa Tidak Ditemukan")

#ari_data(buka_data)
#======================================
# Latihan Praktikum 2
# Lat 4 Fungsi Ubah data
#======================================

#fungsi untuk mengubah data mahasiswa
def ubah_data(data_dict):
    
    nim = input("Masukkan NIM yang akan diupdate : ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan.")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru : ").strip())
    except ValueError:
        print("Nilai harus berupa angka. UPDATE DIABATALKAN.")

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 1 sampai 100.")
        
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")

#ubah_data(buka_data)
print("-"*32)

#======================================
# Latihan Praktikum 2  
# Lat 5 Fungsi Simpan data
#======================================

#fungsi untuk menyimpan data kembali ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
    print("\nData berhasil disimpan ke file: ", nama_file)
simpan_data(nama_file, buka_data)

#======================================
# Latihan Praktikum 2
# Lat 6 Membuat Menu Interaktif
#======================================

def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) #fungsi 1 load data

    while True:
        print("\n===== Menu Data Mahasiswa =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")
        pilihan = input("Pilih menu : ").strip()

        if pilihan == '1':
            tampil_data(buka_data) #fungsi 2 tampil data
        
        elif pilihan == '2':
            cari_data(buka_data) #fungsi 3 mencari data
        
        elif pilihan == '3':
            ubah_data(buka_data) #fungsi 4 ubah data
        
        elif pilihan == '4':
            simpan_data(nama_file, buka_data) #fungsi 5 simpan data
            print("Data berhasil disimpan.")
       
        elif pilihan == '0': #fungsi 6 keluar
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()