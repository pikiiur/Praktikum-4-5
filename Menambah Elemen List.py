# Membuat list dengan 5 elemen
my_list = [22, 23, 24, 25, 26]

# Ambil 2 bagian dari list pertama (A) dan jadikan list ke-2 (B)
list_A = my_list[:2]
list_B = list_A.copy()

# Tambahkan list B dengan nilai string
list_B.append("Hello")

# Tambahkan list B dengan 3 nilai
list_B.extend([1, 2, 3])

# Gabungkan list B dengan list A
list_A_and_B = list_B + list_A

# Menampilkan hasil akhir
print("List A setelah perubahan:", list_A)
print("List B setelah perubahan:", list_B)
print("Hasil gabungan list B dan A:", list_A_and_B)

