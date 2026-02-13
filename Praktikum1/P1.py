#-----------------------------------
# Praktikum 1 : Konsep ADT dan File Handling 
# Lat Dasar 1 : Membaca seluruh isi file data
#-----------------------------------

print("---Membuka File dalam satu string---")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("")
print("=================================")
print("")

#-----------------------------------
# Praktikum 1 : Konsep ADT dan File Handling 
# Lat Dasar 2 : Membaca dan mencari data per baris
#-----------------------------------

print("Tipe data :", type(isi_file))

jumlah_baris = 0
print("---Membuka File per baris---")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris
        print("Baris ke-", jumlah_baris) 
        
        print("Isinya :", baris)

print("")
print("=================================")
print("")

print("---Membuka File per baris dan memisahkan data---")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter pada setiap akhir baris
        nim, nama, nilai = baris.split(",") #Memisahkan setiap elemen pada baris
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", int(nilai))

print("")
print("=================================")
print("")

#-----------------------------------
# Praktikum 1 : Konsep ADT dan File Handling 
# Lat Dasar 3 : Membaca data dan menyimpan nya ke data list
#-----------------------------------

data_list = [] #Membuat list kosong

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter pada setiap akhir baris
        nim, nama, nilai = baris.split(",") #Memisahkan setiap elemen pada baris
        data_list.append([nim, nama, int(nilai)]) #Memasukkan data ke dalam list
print("---Menampilkan data dalam bentuk list---")
print(data_list)
print("contoh akses data ke-2 :", data_list[1]) 
print("contoh akses data ke-3 :", data_list[3]) 
print("jumlah data :", len(data_list)) 

print("")
print("=================================")
print("")

#-----------------------------------
# Praktikum 1 : Konsep ADT dan File Handling 
# Lat Dasar 4 : Membaca data dan menyimpan nya ke data dictionary
#-----------------------------------

data_dict = {} #Membuat dictionary kosong
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() 
        nim, nama, nilai = baris.split(",") 
        data_dict[nim] = {
            'nama': nama, 
            'nilai': int(nilai)
            } 

print("---Menampilkan data dalam bentuk dictionary---")
print(data_dict)