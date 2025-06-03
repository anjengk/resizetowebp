# resizetowebp
# 🖼️ Produk Image Resizer & Optimizer

Script Python ini digunakan untuk mengubah ukuran dan mengoptimalkan gambar produk agar lebih ringan untuk keperluan web, e-commerce, atau katalog digital. 
Gambar yang lebarnya melebihi 1000 piksel akan diubah ukurannya secara proporsional dan dikonversi ke format `.webp` yang efisien.

🔧 Fitur

- Mengubah ukuran gambar yang lebarnya lebih dari 1000px
- Menyimpan gambar sebagai `.webp` dengan kualitas dan efisiensi optimal
- Dukungan format input: `.jpg`, `.jpeg`, `.png`
- Output disimpan dalam folder `produk_optimized`

📦 Dependency

- [Pillow](https://python-pillow.org) (Fork dari PIL)

Instalasi Pillow:

pip install Pillow

▶️ Cara Penggunaan
Simpan script ini sebagai resize.py (atau nama lain).

Jalankan melalui terminal/command prompt:
python script.py
Masukkan path folder yang berisi gambar produk saat diminta.

🗂️ Struktur Output
Gambar hasil optimasi akan disimpan di folder produk_optimized/ di direktori yang sama dengan script.

Format file hasil: .webp

📌 Contoh
Misalnya kamu punya folder produk/ yang berisi:

Copy
Edit
produk/
├── sepatu1.jpg
├── tas2.png
└── baju3.jpeg
Setelah diproses, kamu akan mendapatkan:

Copy
Edit
produk_optimized/
├── sepatu1.webp
├── tas2.webp
└── baju3.webp
⚠️ Catatan
Gambar yang lebarnya sudah kurang dari atau sama dengan 1000px tidak akan diubah ukurannya.

Pastikan gambar tidak rusak agar tidak gagal saat diproses.

📃 Lisensi
Script ini bebas digunakan dan dimodifikasi sesuai kebutuhan proyekmu.
Silakan sesuaikan jika kamu ingin menambahkan branding, lisensi khusus, atau dokumentasi tambahan.

Terima Kasih...
