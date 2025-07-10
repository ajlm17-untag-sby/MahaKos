import os
from modul.auth import Mahasiswa
from modul.aktifitas import JadwalKegiatan, Diary
from modul.akademik import JadwalPerkuliahan, Tugas
from modul.keuangan import TransaksiKeuangan, ManajemenKeuangan
from modul.manajemen_pengguna import UserManager
from modul.utils import FileHandler, simpan_semua_data, muat_data_per_user, simpan_laporan_pengguna, simpan_laporan_admin
from datetime import datetime

# Inisialisasi
file = FileHandler()
daftar_pengguna = []
daftar_kegiatan = []
daftar_tugas = []
daftar_jadwal_kuliah = []
catatan_diary = Diary()
manajemen_keuangan = ManajemenKeuangan()

# Admin default
admin_akun = {
    "admin1": "admin123",
    "admin2": "admin456",
    "admin3": "admin789"
}
user_manager = UserManager(daftar_pengguna)

# Memuat semua data
def muat_semua_data():
    # Muat pengguna
    data_pengguna = file.baca_dari_csv("data/pengguna.csv")
    for u in data_pengguna:
        if len(u) >= 4:
            pengguna = Mahasiswa(u[0], u[1], u[2], u[3])
            daftar_pengguna.append(pengguna)

    # Muat kegiatan
    data_kegiatan = file.baca_dari_csv("data/kegiatan.csv")
    for k in data_kegiatan:
        if len(k) >= 5:
            kegiatan = JadwalKegiatan(k[0], k[1], k[2], k[3])
            daftar_kegiatan.append(kegiatan)

    # Muat diary
    diary_list = file.baca_dari_txt("data/diary.txt")
    for catatan in diary_list:
        if catatan.startswith("["):
            tanggal, isi = catatan[1:].split("] ", 1)
            catatan_diary._Diary__catatan.append((tanggal, isi))

    # Muat jadwal kuliah
    data_jadwal = file.baca_dari_csv("data/jadwal_kuliah.csv")
    for j in data_jadwal:
        if len(j) >= 6:
            jadwal = JadwalPerkuliahan(j[0], j[1], j[2], j[3], j[4], j[5])
            daftar_jadwal_kuliah.append(jadwal)

    # Muat tugas
    data_tugas = file.baca_dari_csv("data/tugas.csv")
    for t in data_tugas:
        if len(t) >= 5:
            tugas = Tugas(t[0], t[1], t[3], t[4])
            daftar_tugas.append(tugas)

    # Muat transaksi keuangan
    data_transaksi = file.baca_dari_csv("data/keuangan.csv")
    for t in data_transaksi:
        if len(t) >= 5:
            try:
                transaksi = TransaksiKeuangan(t[2], int(t[3]), t[4])
                manajemen_keuangan.tambah_transaksi(transaksi, silent=True)
            except ValueError:
                continue

# Fungsi menu utama (awal)
def menu_awal():
    while True:
        print("\n=== SELAMAT DATANG DI MAHAKOS ===")
        print("1. Login")
        print("2. Daftar")
        print("3. Keluar")
        
        try:
            pilihan = input("Pilih menu: ")
        except KeyboardInterrupt:
            print("\nInput dibatalkan. Kembali ke menu...")
            continue

        if pilihan == "1":
            login()
        elif pilihan == "2":
            daftar()
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan MahaKos!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi daftar
def daftar():
    print("\n=== FORM PENDAFTARAN ===")
    username = input("Buat Username: ")
    if any(u.get_username() == username for u in daftar_pengguna):
        print("Username sudah terdaftar.")
        return
    password = input("Buat Password: ")
    nama = input("Nama Lengkap: ")
    nim = input("NIM: ")
    pengguna_baru = Mahasiswa(username, password, nama, nim)
    daftar_pengguna.append(pengguna_baru)
    print("Pendaftaran berhasil! Silakan login.")
    file.simpan_ke_csv([u.get_data() for u in daftar_pengguna], "data/pengguna.csv")


# Fungsi login
def login():
    print("\n=== LOGIN ===")
    print("1. Login sebagai Admin")
    print("2. Login sebagai Pengguna Biasa")
    level = input("Pilih: ")

    username = input("Username: ")
    password = input("Password: ")

    if level == "1":
        if username in admin_akun and admin_akun[username] == password:
            print(f"\nSelamat datang, {username} (Admin)")
            menu_admin()
        else:
            print("Login admin gagal.")

    elif level == "2":
        for u in daftar_pengguna:
            if u.verifikasi_login(username, password):
                print(f"\nSelamat datang, {u.get_nama()}!")
                global daftar_kegiatan, catatan_diary, daftar_jadwal_kuliah, daftar_tugas, manajemen_keuangan
                daftar_kegiatan, catatan_diary, daftar_jadwal_kuliah, daftar_tugas, manajemen_keuangan = muat_data_per_user(u.get_username())
                menu_user(u)
                return
        print("Login pengguna gagal.")
        
    else:
        print("Pilihan tidak valid.")

# Menu Admin
def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat Semua Pengguna")
        print("2. Ubah Nama Pengguna")
        print("3. Reset Password")
        print("4. Hapus Pengguna")
        print("5. Ekspor Laporan Pengguna")
        print("6. Kembali")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            user_manager.tampilkan_semua_pengguna()
        elif pilih == "2":
            username = input("Masukkan username: ")
            nama_baru = input("Nama baru: ")
            user_manager.ubah_nama(username, nama_baru)
        elif pilih == "3":
            username = input("Masukkan username: ")
            pass_baru = input("Password baru: ")
            user_manager.reset_password(username, pass_baru)
        elif pilih == "4":
            username = input("Username yang akan dihapus: ")
            konfirmasi = input("Yakin hapus akun? (y/n): ")
            if konfirmasi.lower() == "y":
                user_manager.hapus_pengguna(username)
        elif pilih == "5":
            simpan_laporan_admin(daftar_pengguna)
        elif pilih == "6":
            break
        else:
            print("Pilihan tidak valid.")

# Menu User
def menu_user(pengguna):
    while True:
        print(f"\n=== DASHBOARD {pengguna.get_nama().upper()} ===")
        print("Tanggal sekarang:", datetime.now().strftime("%Y-%m-%d | pukul: %H:%M"))
        print("1. Manajemen Kegiatan & Diary")
        print("2. Manajemen Akademik")
        print("3. Manajemen Keuangan")
        print("4. Simpan Semua Data")
        print("5. Ekspor Laporan Pengguna")
        print("6. Logout")
        
        try:
            pilihan = input("Pilih menu: ")
        except KeyboardInterrupt:
            print("\nInput dibatalkan. Kembali ke dashboard...")
            continue

        if pilihan == "1":
            menu_aktifitas()
        elif pilihan == "2":
            menu_akademik()
        elif pilihan == "3":
            menu_keuangan()
        elif pilihan == "4":
            simpan_semua_data(
                pengguna.get_username(),
                daftar_pengguna,
                daftar_kegiatan,
                catatan_diary,
                daftar_jadwal_kuliah,
                daftar_tugas,
                manajemen_keuangan
            )
            print("Semua data berhasil disimpan.")
        elif pilihan == "5":
            simpan_laporan_pengguna(
                pengguna.get_username(),
                pengguna,
                daftar_kegiatan,
                catatan_diary,
                daftar_jadwal_kuliah,
                daftar_tugas,
                manajemen_keuangan
            )
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu Aktifitas
def menu_aktifitas():
    while True:
        print("\n=== MENU AKTIVITAS & DIARY ===")
        print("1. Lihat Kegiatan")
        print("2. Tambah Kegiatan Baru")
        print("3. Tulis Catatan Harian")
        print("4. Lihat Catatan Diary")
        print("5. Kembali")
        pilih = input("Pilih: ")
        if pilih == "1":
            if not daftar_kegiatan:
                print("Belum ada kegiatan.")
            else:
                for i, k in enumerate(daftar_kegiatan, 1):
                    k.tampilkan(i)
        elif pilih == "2":
            j = input("Judul: ")
            jm = input("Jam Mulai (HH:MM): ")
            js = input("Jam Selesai (HH:MM): ")
            k = input("Keterangan: ")
            kegiatan = JadwalKegiatan(j, jm, js, k)
            daftar_kegiatan.append(kegiatan)
            print("Kegiatan berhasil ditambahkan.")
            file.simpan_ke_csv([k.get_data() for k in daftar_kegiatan], "data/kegiatan.csv")
        elif pilih == "3":
            teks = input("Isi catatan: ")
            catatan_diary.tambah_catatan(teks)
            print("Catatan Diary berhasil ditambahkan.")
            file.simpan_ke_txt(catatan_diary.get_daftar_catatan(), "data/diary.txt")
        elif pilih == "4":
            catatan_diary.tampilkan_catatan()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu Akademik
def menu_akademik():
    while True:
        print("\n=== MENU AKADEMIK ===")
        print("1. Lihat Jadwal Kuliah")
        print("2. Tambah Jadwal Kuliah")
        print("3. Lihat Tugas")
        print("4. Tambah Tugas Baru")
        print("5. Kembali")

        try:
            pilih = input("Pilih: ")
        except KeyboardInterrupt:
            print("\nInput dibatalkan. Kembali ke menu akademik...")
            continue

        if pilih == "1":
            if not daftar_jadwal_kuliah:
                print("Belum ada jadwal.")
            else:
                print("|----------------------------------------------------------------------------------------------|")
                print("| No | Kode        | Mata Kuliah                            | Hari     | Jam M - Jam S | Ruang |")
                print("|----------------------------------------------------------------------------------------------|")
                for i, j in enumerate(daftar_jadwal_kuliah, 1):
                    j.tampilkan(i)
                print("|----------------------------------------------------------------------------------------------|")

        elif pilih == "2":
            try:
                kode = input("Kode MK: ")
                nama = input("Nama MK: ")
                hari = input("Hari: ")
                jm = input("Jam Mulai (HH:MM): ")
                js = input("Jam Selesai (HH:MM): ")
                ruang = input("Ruang: ")
                jadwal = JadwalPerkuliahan(kode, nama, hari, jm, js, ruang)
                daftar_jadwal_kuliah.append(jadwal)
                print("Jadwal berhasil ditambahkan.")
                file.simpan_ke_csv([j.get_data() for j in daftar_jadwal_kuliah], "data/jadwal_kuliah.csv")
            except KeyboardInterrupt:
                print("\nInput dibatalkan.")
                continue

        elif pilih == "3":
            if not daftar_tugas:
                print("Belum ada tugas.")
            else:
                for i, t in enumerate(daftar_tugas, 1):
                    t.tampilkan_tugas(i)

        elif pilih == "4":
            try:
                kode = input("Kode MK: ")
                nama = input("Nama MK: ")
                ket = input("Keterangan Tugas: ")
                deadline = input("Deadline (YYYY-MM-DD): ")

                from datetime import datetime
                datetime.strptime(deadline, "%Y-%m-%d")

                tugas = Tugas(kode, nama, ket, deadline)
                daftar_tugas.append(tugas)
                print("Tugas berhasil ditambahkan.")
                file.simpan_ke_csv([t.get_data() for t in daftar_tugas], "data/tugas.csv")

            except ValueError:
                print("Format tanggal salah. Gunakan format YYYY-MM-DD.")
                continue
            except KeyboardInterrupt:
                print("\nInput dibatalkan.")
                continue

        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu Keuangan
def menu_keuangan():
    while True:
        print("\n=== MENU KEUANGAN ===")
        print("1. Lihat Saldo")
        print("2. Tambah Transaksi")
        print("3. Lihat Riwayat Transaksi")
        print("4. Kembali")

        try:
            pilih = input("Pilih: ")
        except KeyboardInterrupt:
            print("\nInput dibatalkan. Kembali ke menu keuangan...")
            continue

        if pilih == "1":
            saldo = manajemen_keuangan.hitung_saldo()
            print("Saldo saat ini: Rp", saldo)

        elif pilih == "2":
            try:
                print("- ketik 'masuk' untuk jenis pemasukan")
                print("- ketik 'keluar' untuk jenis pengeluaran")
                jenis = input(
                    "Jenis (pemasukan/pengeluaran): ").lower()
                if jenis not in ["masuk", "keluar"]:
                    print("Jenis tidak valid. Masukkan 'pemasukan' atau 'pengeluaran'.")
                    continue

                nominal = int(input("Nominal (angka saja): "))
                ket = input("Keterangan: ")

                transaksi = TransaksiKeuangan(jenis, nominal, ket)
                manajemen_keuangan.tambah_transaksi(transaksi)

                file.simpan_ke_csv(
                    manajemen_keuangan.get_daftar_transaksi(),
                    "data/keuangan.csv"
                )

                print("Transaksi berhasil ditambahkan.")

            except ValueError:
                print("Nominal harus berupa angka.")
            except KeyboardInterrupt:
                print("\nInput dibatalkan. Transaksi tidak jadi ditambahkan.")

        elif pilih == "3":
            manajemen_keuangan.tampilkan_riwayat()

        elif pilih == "4":
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    os.makedirs("laporan", exist_ok=True)
    muat_semua_data()
    menu_awal()