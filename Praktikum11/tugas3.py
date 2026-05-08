# ==========================================
# Vincensius Alfa Setyawan
# J0403251075
# TPL A2
# ==========================================

matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]

nodes = ["A", "B", "C", "D"]

graph = {}

for i in range(len(matrix)):

    # Membuat list kosong untuk node
    graph[nodes[i]] = []

    for j in range(len(matrix[i])):

        # Jika bernilai 1 berarti terhubung
        if matrix[i][j] == 1:

            # Tambahkan hubungan ke list
            graph[nodes[i]].append(nodes[j])

print("Adjacency List:")

for node, edges in graph.items():
    print(node, "->", edges)

# Program ini mengubah adjacency matrix menjadi adjacency list secara otomatis.

# Cara kerja:
# 1. Membaca setiap baris matrix
# 2. Mengecek nilai setiap kolom
# 3. Jika nilainya 1, berarti ada hubungan
# 4. Node dimasukkan ke adjacency list

# Hasil akhir menunjukkan koneksi antar node dalam bentuk list.
