import csv, os, shutil
from modul.aktifitas import JadwalKegiatan, Diary
from modul.akademik import JadwalPerkuliahan, Tugas
from modul.keuangan import TransaksiKeuangan, ManajemenKeuangan

class FileHandler:
    def simpan_ke_csv(self, data_list, nama_file, header=None):
        with open(nama_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if header:
                writer.writerow(header)
            writer.writerows(data_list)
        print(f"Data berhasil disimpan ke {nama_file}")

    def baca_dari_csv(self, nama_file):
        data = []
        if os.path.exists(nama_file):
            with open(nama_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        else:
            print(f"(info) {nama_file} tidak ditemukan. Akan dibuat otomatis saat menyimpan.")
        return data

    def simpan_ke_txt(self, daftar_teks, nama_file):
        with open(nama_file, 'w', encoding='utf-8') as file:
            for baris in daftar_teks:
                file.write(baris + '\n')
        print(f"Data berhasil disimpan ke {nama_file}")

    def baca_dari_txt(self, nama_file):
        if os.path.exists(nama_file):
            with open(nama_file, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines()]
        else:
            print(f"(info) {nama_file} tidak ditemukan. Akan dibuat otomatis saat menyimpan.")
            return []

    def backup_file(self, source_path, backup_path):
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)
        if os.path.exists(source_path):
            shutil.copy(source_path, backup_path)
            print(f"Backup dibuat: {backup_path}")

def simpan_semua_data(username, daftar_pengguna, daftar_kegiatan, catatan_diary,
                      daftar_jadwal_kuliah, daftar_tugas, manajemen_keuangan):
    file = FileHandler()

    # Simpan pengguna (global)
    pengguna_file = "data/pengguna.csv"
    file.simpan_ke_csv([u.get_data() for u in daftar_pengguna], pengguna_file)
    file.backup_file(pengguna_file, "backup/pengguna_backup.csv")

    # Per-user files
    path_kegiatan = f"data/kegiatan_{username}.csv"
    path_diary = f"data/diary_{username}.txt"
    path_jadwal = f"data/jadwal_{username}.csv"
    path_tugas = f"data/tugas_{username}.csv"
    path_keuangan = f"data/keuangan_{username}.csv"

    # Simpan data user
    file.simpan_ke_csv([k.get_data() for k in daftar_kegiatan], path_kegiatan)
    file.simpan_ke_txt(catatan_diary.get_daftar_catatan(), path_diary)
    file.simpan_ke_csv([j.get_data() for j in daftar_jadwal_kuliah], path_jadwal)
    file.simpan_ke_csv([t.get_data() for t in daftar_tugas], path_tugas)
    file.simpan_ke_csv(manajemen_keuangan.get_daftar_transaksi(), path_keuangan)

    # Backup semua file per user
    file.backup_file(path_kegiatan, f"backup/kegiatan_{username}_backup.csv")
    file.backup_file(path_diary, f"backup/diary_{username}_backup.txt")
    file.backup_file(path_jadwal, f"backup/jadwal_{username}_backup.csv")
    file.backup_file(path_tugas, f"backup/tugas_{username}_backup.csv")
    file.backup_file(path_keuangan, f"backup/keuangan_{username}_backup.csv")

def muat_data_per_user(username):
    file = FileHandler()

    # === Kegiatan ===
    data_kegiatan = file.baca_dari_csv(f"data/kegiatan_{username}.csv")
    daftar_kegiatan = []
    for row in data_kegiatan:
        if len(row) >= 5:
            kegiatan = JadwalKegiatan(row[0], row[1], row[2], row[3])
            daftar_kegiatan.append(kegiatan)

    # === Diary ===
    data_diary = file.baca_dari_txt(f"data/diary_{username}.txt")
    catatan_diary = Diary()
    for baris in data_diary:
        if baris.startswith("[") and "]" in baris:
            tanggal, isi = baris.split("] ", 1)
            tanggal = tanggal.strip("[]")
            catatan_diary._Diary__catatan.append((tanggal, isi))

    # === Jadwal Kuliah ===
    data_jadwal = file.baca_dari_csv(f"data/jadwal_{username}.csv")
    daftar_jadwal_kuliah = []
    for row in data_jadwal:
        if len(row) >= 6:
            jadwal = JadwalPerkuliahan(row[0], row[1], row[2], row[3], row[4], row[5])
            daftar_jadwal_kuliah.append(jadwal)

    # === Tugas ===
    data_tugas = file.baca_dari_csv(f"data/tugas_{username}.csv")
    daftar_tugas = []
    for row in data_tugas:
        if len(row) >= 5:
            tugas = Tugas(row[0], row[1], row[3], row[4])
            tugas._Tugas__tanggal_dibuat = row[2]
            daftar_tugas.append(tugas)

    # === Keuangan ===
    data_keuangan = file.baca_dari_csv(f"data/keuangan_{username}.csv")
    manajemen_keuangan = ManajemenKeuangan()
    for row in data_keuangan:
        if len(row) >= 5:
            transaksi = TransaksiKeuangan(row[2], int(row[3]), row[4])
            transaksi._TransaksiKeuangan__tanggal = row[0]
            transaksi._TransaksiKeuangan__jam = row[1]
            manajemen_keuangan.tambah_transaksi(transaksi, silent=True)

    return daftar_kegiatan, catatan_diary, daftar_jadwal_kuliah, daftar_tugas, manajemen_keuangan

def simpan_laporan_pengguna(username, pengguna, daftar_kegiatan, catatan_diary, daftar_jadwal_kuliah, daftar_tugas, manajemen_keuangan):
    isi = []

    isi.append(f"{username} - {pengguna.get_nama()}")
    isi.append("=== Jadwal Kegiatan ===")
    for i, k in enumerate(daftar_kegiatan, 1):
        data = k.get_data()
        isi.append(f"{i}. {data[0]} | {data[1]} - {data[2]} | {data[3]} | {data[4]}")

    isi.append("=== Catatan Harian ===")
    catatan = catatan_diary.get_daftar_catatan()
    if not catatan:
        isi.append("Belum ada catatan.")
    else:
        for i, c in enumerate(catatan, 1):
            isi.append(f"{i}. {c}")

    isi.append("=== Jadwal Perkuliahan ===")
    isi.append("|----------------------------------------------------------------------------------------------|")
    isi.append("| No | Kode        | Mata Kuliah                            | Hari     | Jam M - Jam S | Ruang |")
    isi.append("|----------------------------------------------------------------------------------------------|")
    for i, j in enumerate(daftar_jadwal_kuliah, 1):
        data = j.get_data()
        isi.append(f"| {i:<2} | {data[0]:<11}| {data[1]:<38}| {data[2]:<9}| {data[3]} - {data[4]} | {data[5]:<5} |")
    isi.append("|----------------------------------------------------------------------------------------------|")

    isi.append("=== Daftar Tugas ===")
    for i, t in enumerate(daftar_tugas, 1):
        data = t.get_data()
        isi.append(f"{i}. {data[0]} | {data[1]} | Dibuat: {data[2]} | Deadline: {data[4]} | {data[3]}")

    isi.append("=== Riwayat Transaksi ===")
    transaksi = manajemen_keuangan.get_daftar_transaksi()
    for i, t in enumerate(transaksi, 1):
        isi.append(f"{i}. {t[0]} | {t[1]} | {t[2]:<10} | Rp{t[3]} | {t[4]}")

    file_path = f"laporan/laporan_{username}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(isi))
    print(f"Laporan pengguna disimpan di: {file_path}")

def simpan_laporan_admin(daftar_pengguna):
    isi = ["=== Daftar Pengguna ==="]
    for i, u in enumerate(daftar_pengguna, 1):
        isi.append(f"{i}. {u.get_username()} - {u.get_nama()}")

    with open("laporan/laporan_pengguna_admin.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(isi))
    print("Laporan admin disimpan di: laporan/laporan_pengguna_admin.txt")
