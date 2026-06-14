"""
Program: matriks.py
Program ini mengimport module Inshan101 dan menguji fungsi-fungsi
aljabar matriks yang ada di dalamnya:
    - tambah_matriks
    - kurang_matriks
    - kali_matriks
    - transpose_matriks
"""

import Inshan101


def main():
    # Matriks contoh untuk operasi tambah, kurang, dan transpose
    # (ukuran sama, 2x3)
    A = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    B = [
        [6, 5, 4],
        [3, 2, 1],
    ]

    Inshan101.tampilkan_matriks(A, "Matriks A")
    Inshan101.tampilkan_matriks(B, "Matriks B")

    # 1. Penjumlahan matriks
    print("\n--- Penjumlahan (A + B) ---")
    hasil_tambah = Inshan101.tambah_matriks(A, B)
    Inshan101.tampilkan_matriks(hasil_tambah, "Hasil A + B")

    # 2. Pengurangan matriks
    print("\n--- Pengurangan (A - B) ---")
    hasil_kurang = Inshan101.kurang_matriks(A, B)
    Inshan101.tampilkan_matriks(hasil_kurang, "Hasil A - B")

    # 3. Transpose matriks
    print("\n--- Transpose Matriks A ---")
    hasil_transpose = Inshan101.transpose_matriks(A)
    Inshan101.tampilkan_matriks(hasil_transpose, "Transpose A")

    # 4. Perkalian matriks
    # Untuk perkalian, jumlah kolom A (3) harus sama dengan jumlah baris C (3)
    C = [
        [1, 0],
        [0, 1],
        [1, 1],
    ]

    print("\n--- Perkalian Matriks (A x C) ---")
    Inshan101.tampilkan_matriks(A, "Matriks A (2x3)")
    Inshan101.tampilkan_matriks(C, "Matriks C (3x2)")
    hasil_kali = Inshan101.kali_matriks(A, C)
    Inshan101.tampilkan_matriks(hasil_kali, "Hasil A x C (2x2)")


if __name__ == "__main__":
    main()
