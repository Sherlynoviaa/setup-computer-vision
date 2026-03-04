# Tugas Individu: Praktikum Machine Learning (Computer Vision)
**Dosen Pengampu:** Herfandi, A.Md., S.Kom., M.Kom

Repositori ini berisi dokumentasi dan hasil belajar mandiri mengenai persiapan lingkungan kerja (Setup Environment) untuk pengolahan citra digital (Computer Vision) berdasarkan video tutorial #1.

---

## Identitas Mahasiswa
- **Nama:** Sherly Novia Indriani
- **NIM:** 231001057

---

## Hasil Praktik Setup Environment
Berikut adalah spesifikasi dan tahapan yang saya lakukan:
- **Bahasa Pemrograman:** Python 3.11
- **Library Utama:** OpenCV (opencv-python)
- **Environment:** ENV_BELAJAR (Anaconda)

### Langkah-Langkah:
1. Membuat Virtual Environment agar sistem isolasi terjaga:  
   `conda create -n ENV_BELAJAR python=3.11`
2. Mengaktifkan environment:  
   `conda activate ENV_BELAJAR`
3. Menginstal library OpenCV menggunakan repositori **Conda-forge** (Play Store-nya library):  
   `pip install opencv-python`
4. Verifikasi instalasi berhasil dilakukan melalui Anaconda Prompt tanpa error DLL.

---

## Analisis Kode Verifikasi
Saya menggunakan skrip `main.py` untuk memverifikasi instalasi:
- **`import cv2`**: Berfungsi untuk memanggil/memuat pustaka OpenCV ke dalam memori kernel Python.
- **`cv2.imread()`**: Berfungsi membaca data gambar digital dan mengubahnya menjadi matriks angka (piksel) agar dapat diolah.
- **`print(cv2.__version__)`**: Digunakan untuk memastikan bahwa library yang terpasang sudah sesuai dan bisa digunakan.

---

## Video Presentasi
Tonton demonstrasi lengkap proses setup dan penjelasan materi saya di sini:  
👉 **(https://youtu.be/sdATJ5sBeIs?si=NqaPytYqgFHcXdIW)**

---

## Referensi & Resource Tambahan
Untuk membantu proses manajemen *environment* dan paket, saya menggunakan referensi perintah dari **Anaconda Official Cheat Sheet**. Teman-teman dapat mendownloadnya melalui tautan di bawah ini:

👉 [**Download Anaconda Cheat Sheet (PDF)**]
[https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf]
