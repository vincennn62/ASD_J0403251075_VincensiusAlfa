data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

kandidat = []
for i in range(len(data)):
    kandidat.append((i+1, data[i]))

kandidat_sorted = sorted(kandidat, key=lambda x: x[1], reverse=True)

top5 = kandidat_sorted[:5]

print("1. Lima skor tertinggi (descending):")
for k in top5:
    print(k[1])

print("\n2. Kandidat yang lolos:")
for k in top5:
    print("Kandidat", k[0])