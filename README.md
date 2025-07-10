# 🏡 MahaKos: Manajemen Harian Mahasiswa & Anak Kos

**MahaKos** adalah aplikasi manajemen harian berbasis teks (CLI) yang dirancang khusus untuk mahasiswa – terutama anak kos – untuk membantu mengatur aktivitas harian, akademik, dan keuangan secara mandiri dan terstruktur.

---

## 🎯 Fitur Utama Aplikasi

- ✅ **Manajemen Kegiatan Harian & Diary**
- ✅ **Manajemen Jadwal Kuliah & Tugas**
- ✅ **Manajemen Keuangan (Pemasukan & Pengeluaran)**
- ✅ **Login & Register untuk Multi-User**
- ✅ **Peran Admin untuk Kelola Pengguna**
- ✅ **Auto-Save & Backup Otomatis**
- ✅ **Ekspor Laporan dalam Bentuk TXT**
- ✅ **Validasi Input & Error Handling Lengkap**

---

## 🚀 Cara Menjalankan Program

1. **Pastikan Python ≥ 3.8 telah terinstal**
2. Buka terminal atau VS Code
3. Jalankan perintah:

```bash
python main.py
```

4. Ikuti petunjuk:
   - Pilih login sebagai `admin` atau `pengguna`
   - Jika pengguna baru → silakan daftar terlebih dahulu

---

## 🗂️ Struktur Folder

```
MahaKos-Final/
├── main.py                  ← Entry point aplikasi
├── modul/                  ← Modul modular untuk fitur utama
│   ├── __init__.py
│   ├── abstract.py         ← Abstract class (OOP: Abstraction)
│   ├── aktifitas.py        ← Jadwal kegiatan dan diary
│   ├── akademik.py         ← Jadwal kuliah dan tugas
│   ├── auth.py             ← Login, register, akun pengguna
│   ├── keuangan.py         ← Transaksi keuangan (inheritance)
│   ├── manajemen_pengguna.py ← Fitur admin
│   └── utils.py            ← Simpan/muat file, laporan, backup
├── data/                   ← File data pengguna (.csv / .txt)
├── backup/                 ← Backup otomatis setiap simpan
├── laporan/                ← Laporan .txt yang bisa diekspor
├── .gitignore              ← File/folder yang tidak di-upload
├── README.md               ← Dokumentasi proyek (ini!)
├── requirements.txt        ← Jika ada library tambahan
└── sample_run.txt          ← Contoh hasil run program
```

---

## 🔐 Sistem Login & Hak Akses

- 👨‍🎓 **Pengguna Mahasiswa**
  - Bisa login dan mengakses dashboard pribadinya
  - Data terpisah per pengguna (kegiatan, diary, tugas, keuangan)

- 🛠️ **Admin**
  - Bisa login sebagai admin
  - Bisa melihat daftar pengguna, reset password, ubah nama, hapus akun
  - Bisa ekspor laporan seluruh pengguna

---

## 💾 Penyimpanan & Keamanan Data

- Semua data disimpan secara **otomatis (auto-save)** saat pengguna menambahkan/mengubah data.
- File disimpan dalam format `.csv` (struktur data) & `.txt` (catatan teks).
- Data pengguna disimpan per file berdasarkan `username`.
- Sistem juga menyimpan **backup otomatis** di folder `/backup/`.

---

## 🧾 Fitur Ekspor Laporan

- 📤 **Laporan User (per individu)**:
  - Berisi kegiatan, diary, jadwal kuliah, tugas, dan transaksi.
  - Disimpan di folder `/laporan/` → bisa dicetak/kumpulkan ke dosen.

- 📤 **Laporan Admin (semua pengguna)**:
  - Daftar semua akun pengguna yang terdaftar.

---

## 🧠 Penerapan OOP (Object-Oriented Programming)

| Prinsip         | Implementasi                                                                      |
|-----------------|------------------------------------------------------------------------------------|
| **Encapsulation** | Semua class menggunakan atribut privat (`__atribut`) dan setter/getter           |
| **Inheritance**  | `TransaksiKeuangan` mewarisi dari class `Transaksi` (tanggal & jam otomatis)      |
| **Polymorphism** | Semua fitur (`tampilkan`, `get_data`) dipanggil secara seragam antar class        |
| **Abstraction**  | Abstract class `FiturAplikasi` digunakan untuk mewariskan struktur ke banyak class |

---

## 🧑‍💻 Tim Pengembang

| Nama Lengkap                  | NIM         |
|------------------------------|-------------|
| Aleksander Jonias Lololuan   | 1482400100  |
| Andre William Malelak        | 1482400088  |
| Fadhil Maula Alfa Reza       | 1482400081  |

---

## ✅ Status Proyek

- [x] Fitur Utama Implemented
- [x] Penyimpanan & Backup Otomatis
- [x] Validasi & Error Handling
- [x] Ekspor Laporan TXT
- [x] Penerapan Prinsip OOP Lengkap

---

## 📌 Catatan

- Aplikasi berbasis CLI (Command Line Interface)
- Cocok digunakan untuk tugas PBO, praktikum dasar Python, atau pengelolaan pribadi
- Bisa dikembangkan ke GUI (Tkinter/PyQt) atau Web (Flask/Django) sebagai next project

---

## 🤝 Kontribusi

Silakan Fork, Pull Request, atau laporkan issue jika ingin mengembangkan atau memberi saran!

---

## 📸 Tampilan CLI (Contoh)

```text
=== SELAMAT DATANG DI MAHAKOS ===
1. Login
2. Daftar
3. Keluar
Pilih menu: 1

=== LOGIN ===
Username: ajol
Password: *****

=== DASHBOARD AJOL ===
1. Manajemen Kegiatan & Diary
2. Manajemen Akademik
3. Manajemen Keuangan
4. Simpan Semua Data
5. Logout
```

---

> “Dengan MahaKos, hidup anak kos bisa jadi lebih tertib, teratur, dan mandiri!” 💡
