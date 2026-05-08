# ==========================================
# Vincensius Alfa Setyawan
# J0403251075
# TPL A2
# ==========================================

# ============================================================
# MENENTUKAN NODE (VERTEX)
# ============================================================
nodes = [
    "Router1",
    "Switch1",
    "Switch2",
    "PC1",
    "PC2",
    "Server"
]


# ============================================================
# MENENTUKAN EDGE
# ============================================================
edges = [
    ("Router1", "Switch1"),
    ("Router1", "Switch2"),
    ("Switch1", "PC1"),
    ("Switch1", "PC2"),
    ("Switch2", "Server"),
    ("Switch2", "PC2")
]


# ============================================================
# ADJACENCY LIST
# ============================================================
graph = {
    "Router1": ["Switch1", "Switch2"],
    "Switch1": ["Router1", "PC1", "PC2"],
    "Switch2": ["Router1", "Server", "PC2"],
    "PC1": ["Switch1"],
    "PC2": ["Switch1", "Switch2"],
    "Server": ["Switch2"]
}

print("=== NODE ===")
for node in nodes:
    print(node)

print("\n=== EDGE ===")
for edge in edges:
    print(edge)

print("\n=== ADJACENCY LIST ===")
for node, connections in graph.items():
    print(node, "->", connections)


# ============================================================
# ADJACENCY MATRIX
# ============================================================
matrix = []

for node1 in nodes:
    row = []

    for node2 in nodes:
        if node2 in graph[node1]:
            row.append(1)
        else:
            row.append(0)

    matrix.append(row)

print("\n=== ADJACENCY MATRIX ===")
print("         ", " ".join(nodes))

for i in range(len(matrix)):
    print(nodes[i], matrix[i])


# ============================================================
# HUBUNGAN ANTAR NODE
# ============================================================
print("\n=== HUBUNGAN ANTAR NODE ===")

for node, connections in graph.items():
    print(node, "terhubung dengan", ", ".join(connections))


# ============================================================
# ANALISIS SINGKAT
# ============================================================
print("=== ANALISIS ===")

print("1. Jenis Graph : Undirected Graph")
print("2. Alasan memilih edge : Edge merepresentasikan koneksi fisik antar perangkat")

print("3. Representasi yang lebih cocok : Adjacency List")
print("   Karena lebih hemat memori")

print("4. Kategori Graph : Sparse Graph")
print("   Karena jumlah edge tidak terlalu banyak")


# ============================================================
# KESIMPULAN
# ============================================================
print("=== KESIMPULAN ===")
print("Graph dapat digunakan untuk memodelkan hubungan antar perangkat jaringan komputer.")
print("Adjacency list lebih efisien untuk graph ini.")