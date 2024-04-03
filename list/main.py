list_1 = [10, 70, 20]
for i in range(0, len(list_1)):
    print("index:", i, "elemen:", list_1[i])

# Enumerate function
"""
Fungsi enumerate() digunakan untuk membuat data sequence menjadi data enumerasi, yang jika dimasukan ke perulangan di setiap iterasinya bisa kita akses index beserta element-nya.
"""

list_2 = [10, 70, 20]

for i, v in enumerate(list_2):
    print("index:", i, "elem:", v)