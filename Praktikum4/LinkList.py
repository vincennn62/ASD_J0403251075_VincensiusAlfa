#====================================
# Nama  : Vincensius Alfa Setyawan
# NIM   : J0403251075
# Kelas : TPL A2
#====================================
# Implementasi Node pada Linked List 
#====================================

class Node:
    def __init__(self, data=None):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #menyimpan alamat node berikutnya pada list

#1) membuat node dengan instatiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) mendefinisikan head dan     menghubungkan node-node tersebut
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Transversal : menelusuri node dari head sampai ke none
current = head
while current is not None:
    print(current.data) #menampilkan dat pada node
    current = current.next #pindah ke node berikutnya