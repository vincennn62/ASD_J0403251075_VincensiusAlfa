# ==========================================
# Vincensius Alfa Setyawan
# J0403251075
# TPL A2
# ==========================================

matrix = [
    [0,1,1,0],  # A terhubung ke B dan C
    [1,0,1,1],  # B terhubung ke A, C, D
    [1,1,0,1],  # C terhubung ke A, B, D
    [0,1,1,0]   # D terhubung ke B dan C
]

nodes = ["A", "B", "C", "D"]

print("Adjacency Matrix:")
print("   ", " ".join(nodes))

for i in range(len(matrix)):
    print(nodes[i], matrix[i])

# Graph ini merupakan undirected graph karena
# hubungan antar node berlaku dua arah.

# Adjacency matrix dipilih karena mempermudah
# melihat hubungan antar node dalam bentuk tabel.

# Arti setiap baris:
# Baris A = hubungan node A ke node lain
# Baris B = hubungan node B ke node lain
# Baris C = hubungan node C ke node lain
# Baris D = hubungan node D ke node lain
