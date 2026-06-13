import fatih094 as ft

#Operasi Dasar
x = 20
y = 20

print("\nOperasi Bilangan")
print("x =", x)
print("y =", y)
print("Penjumlahan =", ft.tambah_angka(x, y))
print("Pengurangan =", ft.kurang_angka(x, y))
print("Perkalian =", ft.kali_angka(x, y))
print("Pembagian =", ft.bagi_angka(x, y))

#MATRIKS 3x3
A = [[2, 3, 1], [0, 4, 2], [1, 0, 3]]

B = [[1, 0, 2], [3, 1, 0], [0, 2, 1]]

print("\nDemo Module fatih094")
print()
ft.tampil(A, "Matriks A:")
ft.tampil(B, "Matriks B:")

ft.tampil(ft.tambah(A, B), "1. Penjumlahan A + B:")
ft.tampil(ft.kurang(A, B), "2. Pengurangan A - B:")
ft.tampil(ft.kali(A, B), "3. Perkalian A x B:")
ft.tampil(ft.transpose(A), "4. Transpose A:")

print("5. Determinan A:")
print("  ", ft.determinan(A))
print()

ft.tampil(ft.invers(A), "6. Invers A:")
ft.tampil(ft.identitas(3), "7. Matriks Identitas 3x3")

print("Verifikasi A x invers(A):")
ft.tampil(ft.kali(A, ft.invers(A)))