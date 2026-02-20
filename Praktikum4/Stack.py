#====================================
# Nama  : Vincensius Alfa Setyawan
# NIM   : J0403251075
# Kelas : TPL A2
#====================================
# Implementasi Stack
#====================================

from inspect import stack
from operator import ne


class Node:
    def __init__(self, data=None):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #menyimpan alamat node berikutnya pada list

#didalam stack ada operasi psuh(memasukan head baru) dan pop(menghapus head)
#A > B > C > None

class Stack:
    def __init__(self):
        self.top = None #TOP menunjuk kepada node paling atas pada stack

    def is_empty(self):
        return self.top is None #mengembalikan true jika stack kosong, false jika tidak kosong
    
    def push(self, data): #masukan data baru
        #1 membuat node baru
        nodeBaru = Node(data) #memanggil konstruktor pada class Node untuk membuat node baru dengan data yang diberikan

        #2 node baru harus menunjuk ke top yang lama
        nodeBaru.next = self.top #node baru menunjuk ke node yang saat ini menjadi top
            
        #3 top pindah ke node baru
        self.top = nodeBaru 

    def pop(self): # ambil/hapus node paling atas
        
        if self.is_empty():
            print("Stack kosong, tidak bisa melakukan pop")
            return None

        data_hapus = self.top.data #soroti bagian top dan simpan di variabel
        # B > A > None
        self.top = self.top.next #pindahkan top ke node berikutnya
        return data_hapus #kembalikan data yang dihapus

    def peek(self):
        #melihat data pada top tanpa menghapusnya
        if self.is_empty():
            return None
        return self.top.data
    

    def tampilkan(self):
        #top > A > B
        current = self.top
        print("Top" , end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instansiasi stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat TOP):", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat TOP):", s.peek())