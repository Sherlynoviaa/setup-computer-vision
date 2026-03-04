# Nama: Sherly Novia Indriani
# NIM: 231001057
# Deskripsi: Program sederhana untuk verifikasi instalasi OpenCV

import cv2

# 1. Membaca gambar yang ada di folder
# Ganti 'test.jpg' dengan nama file gambar kamu
gambar = cv2.imread('test.jpg')

# Cek apakah gambar berhasil terbaca
if gambar is None:
    print("Error: Gambar tidak ditemukan di folder!")
else:
    # 2. Menampilkan informasi versi OpenCV
    print("Versi OpenCV yang terinstal:", cv2.__version__)
    
    # 3. Menampilkan gambar dalam jendela pop-up
    cv2.imshow('Jendela Hasil Praktik - Computer Vision', gambar)
    
    # 4. Menunggu tombol ditekan agar jendela tidak langsung tertutup
    print("Tekan tombol apapun pada keyboard untuk menutup jendela gambar.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()