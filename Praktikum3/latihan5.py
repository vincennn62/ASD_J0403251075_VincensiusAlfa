# Membuat Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Membuat Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Menampilkan Linked List
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Method untuk membalik Linked List
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next   # simpan next
            current.next = prev       # balik arah
            prev = current            # geser prev
            current = next_node       # geser current

        self.head = prev


# ===============================
# Program Utama
# ===============================

ll = LinkedList()

# Input elemen dari user
input_data = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")
elements = input_data.split(",")

for item in elements:
    ll.append(int(item.strip()))

print("Linked List sebelum dibalik:")
ll.display()

ll.reverse()

print("Linked List setelah dibalik:")
ll.display()
