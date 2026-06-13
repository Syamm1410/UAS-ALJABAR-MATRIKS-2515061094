# fatih094.py

def tambah_angka(x, y):
    return x + y

def kurang_angka(x, y):
    return x - y

def kali_angka(x, y):
    return x * y

def bagi_angka(x, y):
    if y == 0:
        raise ValueError("tidak bisa membagi dengan nol")
    return x / y

def _cek(M, nama="M"):
    if len(M) != 3 or any(len(r) != 3 for r in M):
        raise ValueError(f"{nama} harus 3x3")

# ngebantu ngitung det 2x2 
def _det2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

# ngambil submatriks 2x2 dengan buang baris br dan kolom kl
def _minor(M, br, kl):
    return [[M[i][j] for j in range(3) if j != kl]
                     for i in range(3) if i != br]


def tambah(A, B):
    _cek(A, "A"); _cek(B, "B")
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]

def kurang(A, B):
    _cek(A, "A"); _cek(B, "B")
    return [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]

def kali(A, B):
    _cek(A, "A"); _cek(B, "B")
    hasil = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

def transpose(A):
    _cek(A, "A")
    return [[A[j][i] for j in range(3)] for i in range(3)]

def determinan(A):
    _cek(A, "A")
    a,b,c = A[0]
    d,e,f = A[1]
    g,h,i = A[2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

def invers(A):
    _cek(A, "A")
    det = determinan(A)
    if det == 0:
        raise ValueError("matriks singular, ga bisa diinvers")
    kof = [[(-1)**(i+j) * _det2(_minor(A, i, j))
            for j in range(3)] for i in range(3)]
    adj = transpose(kof)
    return [[adj[i][j]/det for j in range(3)] for i in range(3)]

def identitas(n):
    return [[1 if i == j else 0 for j in range(n)]
            for i in range(n)]


# Agar rapi di terminal
def tampil(M, label=""):
    if label:
        print(label)
    for baris in M:
        print(" ", [round(x, 4) if isinstance(x, float) else x for x in baris])
    print()