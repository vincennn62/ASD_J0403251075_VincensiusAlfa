#====================================
# Nama  : Vincensius Alfa Setyawan
# NIM   : J0403251075
# Kelas : TPL A2
#====================================
# Implementasi Queue dengan Linked List
#====================================

class Node:
    def __init__(self, data=None):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #menyimpan alamat node berikutnya pada list

class queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #node depan
        self.rear = None #node belakang

    def is_empty(self):
        return self.front is None
    
    #fungsi menambahkan data baru
    def enqueue(self, data):
        NodeBaru = Node(data) 
        
        #Jika queue kosong, maka front dan rear menunjuk ke node baru
        if self.is_empty():
            self.front = NodeBaru
            self.rear = NodeBaru
            return
        
        self.rear.next = NodeBaru #letakan data pada setelahnya rear
        self.rear = NodeBaru #jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data dari depan
        data_hapus = self.front.data #lihat data paling depan
        self.front = self.front.next 
        return data_hapus

    def tampilkan(self):
        current = self.front
        print("Front ->" , end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

#inisialisasi queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
