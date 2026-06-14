def _ukuran(M):
    baris = len(M)
    kolom = len(M[0]) if baris > 0 else 0
    return baris, kolom


def tambah_matriks(A, B):
    baris_a, kolom_a = _ukuran(A)
    baris_b, kolom_b = _ukuran(B)

    if (baris_a, kolom_a) != (baris_b, kolom_b):
        raise ValueError()

    hasil = []
    for i in range(baris_a):
        baris_hasil = []
        for j in range(kolom_a):
            baris_hasil.append(A[i][j] + B[i][j])
        hasil.append(baris_hasil)
    return hasil


def kurang_matriks(A, B):
    baris_a, kolom_a = _ukuran(A)
    baris_b, kolom_b = _ukuran(B)

    if (baris_a, kolom_a) != (baris_b, kolom_b):
        raise ValueError()

    hasil = []
    for i in range(baris_a):
        baris_hasil = []
        for j in range(kolom_a):
            baris_hasil.append(A[i][j] - B[i][j])
        hasil.append(baris_hasil)
    return hasil


def kali_matriks(A, B):
    baris_a, kolom_a = _ukuran(A)
    baris_b, kolom_b = _ukuran(B)

    if kolom_a != baris_b:
        raise ValueError(
        )

    # Inisialisasi matriks hasil dengan nilai 0
    hasil = [[0 for _ in range(kolom_b)] for _ in range(baris_a)]

    for i in range(baris_a):
        for j in range(kolom_b):
            total = 0
            for k in range(kolom_a):
                total += A[i][k] * B[k][j]
            hasil[i][j] = total

    return hasil


def transpose_matriks(A):
    baris_a, kolom_a = _ukuran(A)

    hasil = [[0 for _ in range(baris_a)] for _ in range(kolom_a)]

    for i in range(baris_a):
        for j in range(kolom_a):
            hasil[j][i] = A[i][j]

    return hasil


def tampilkan_matriks(M, nama="Matriks"):
    print(f"{nama} =")
    for baris in M:
        print("  ", baris)
