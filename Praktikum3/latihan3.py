# Membuat Node untuk Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Membuat Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def append(self, data):
        new_node = Node(data)

        # Jika list kosong
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Fungsi pencarian
    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False


# ===============================
# Program Utama
# ===============================

dll = DoublyLinkedList()

# Input elemen (sesuai contoh soal)
elements = [2, 6, 9, 14, 20]

for item in elements:
    dll.append(item)

print("Masukkan elemen ke dalam Doubly Linked List: 2, 6, 9, 14, 20")

cari = int(input("Masukkan elemen yang ingin dicari: "))

if dll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {cari} tidak ditemukan dalam Doubly Linked List.")
