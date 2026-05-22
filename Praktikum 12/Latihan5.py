# ==========================================================
# Nama  : Vincensius Alfa Setyawan
# NIM   : J0403251075
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota
# ==========================================================

import heapq

# Graph berbobot antar kota
# Bobot menunjukkan jarak/tempuh antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek
    dari node awal ke semua node lainnya.
    """

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

start_node = 'Bogor'

hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")


# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node dengan jarak paling kecil adalah Depok dengan jarak 2.
# 3. Node dengan jarak paling besar adalah Bandung dengan jarak 8.
# 4. Dijkstra bekerja dengan memilih jalur dengan jarak terkecil terlebih dahulu, lalu memperbarui jarak ke node lain sampai semua jalur ditemukan.