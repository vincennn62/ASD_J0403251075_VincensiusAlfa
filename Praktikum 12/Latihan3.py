# ==========================================================
# Nama  : Vincensius Alfa Setyawan
# NIM   : J0403251075
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika ditemukan jarak yang lebih kecil
                if (
                    distances[node] != float('inf')
                    and distances[node] + weight < distances[neighbor]
                ):
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:
# 1. Bobot langsung A ke B adalah 5.
# 2. Total bobot jalur A -> C -> B adalah 2.
# 3. Jalur A -> C -> B lebih kecil karena total bobotnya 2.
# 4. Bellman-Ford bisa digunakan pada bobot negatif karena terus memperbarui jarak.
# 5. Relaksasi edge adalah proses memperbarui jarak jika ditemukan jalur lebih pendek.
# 6. Bellman-Ford mendukung bobot negatif, sedangkan Dijkstra tidak.