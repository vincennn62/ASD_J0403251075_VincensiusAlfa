class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next   
            current.next = prev      
            prev = current           
            current = next_node     

        self.head = prev


ll = LinkedList()

input_data = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")
elements = input_data.split(",")

for item in elements:
    ll.append(int(item.strip()))

print("Linked List sebelum dibalik:")
ll.display()

ll.reverse()

print("Linked List setelah dibalik:")
ll.display()
