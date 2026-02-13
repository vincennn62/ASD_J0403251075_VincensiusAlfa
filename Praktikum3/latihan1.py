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

    # Menampilkan isi linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Menghapus node berdasarkan nilai
    def delete_node(self, key):
        temp = self.head

        # Jika head yang dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Mencari node dengan nilai key
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika tidak ditemukan
        if temp is None:
            print("Data tidak ditemukan")
            return

        # Menghapus node
        prev.next = temp.next
        temp = None


# ===============================
# Contoh penggunaan
# ===============================

ll = LinkedList()

ll.append("Pisang")
ll.append("Jeruk")
ll.append("Melon")
ll.append("Apel")

print("Linked List sebelum dihapus:")
ll.display()

x = "Melon"
ll.delete_node(x)

print("Linked List setelah menghapus", x, ":")
ll.display()
