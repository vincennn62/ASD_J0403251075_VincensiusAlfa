# ==========================================
# Vincensius Alfa Setyawan
# J0403251075
# TPL A2
# ==========================================

graph = {
    "A": ["B", "C"],      # A terhubung ke B dan C
    "B": ["A", "C", "D"], # B terhubung ke A, C, D
    "C": ["A", "B", "D"], # C terhubung ke A, B, D
    "D": ["B", "C"]       # D terhubung ke B dan C
}

print("Adjacency List:")

for node, edges in graph.items():
    print(node, "->", edges)

# Graph direpresentasikan menggunakan dictionary
# Python karena lebih sederhana dibaca.

# Setiap key adalah node
# Setiap value adalah daftar node yang terhubung

# Huruf digunakan sebagai node sesuai ketentuan