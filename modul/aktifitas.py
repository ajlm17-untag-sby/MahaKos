from datetime import datetime
from modul.abstract import FiturAplikasi

class JadwalKegiatan(FiturAplikasi):
    def __init__(self, judul, jam_mulai, jam_selesai, keterangan):
        self.__judul = judul
        self.__jam_mulai = jam_mulai
        self.__jam_selesai = jam_selesai
        self.__keterangan = keterangan
        self.__tanggal = datetime.now().strftime("%Y-%m-%d")

    def get_data(self):
        return (self.__judul, self.__jam_mulai, self.__jam_selesai, self.__keterangan, self.__tanggal)

    def tampilkan(self, no):
        print(f"{no}. {self.__judul} | {self.__jam_mulai} - {self.__jam_selesai} | {self.__keterangan} | {self.__tanggal}")

    def set_judul(self, judul_baru):
        if judul_baru.strip():
            self.__judul = judul_baru

    def set_waktu(self, jam_mulai, jam_selesai):
        self.__jam_mulai = jam_mulai
        self.__jam_selesai = jam_selesai

    def set_keterangan(self, keterangan_baru):
        self.__keterangan = keterangan_baru

class Diary:
    def __init__(self):
        self.__catatan = []

    def tambah_catatan(self, teks):
        tanggal = datetime.now().strftime("%Y-%m-%d")
        self.__catatan.append((tanggal, teks))

    def tampilkan_catatan(self):
        if not self.__catatan:
            print("Belum ada catatan harian.")
        else:
            print("\n=== Catatan Harian ===")
            for i, (tgl, isi) in enumerate(self.__catatan, 1):
                print(f"{i}. [{tgl}] {isi}")

    def get_daftar_catatan(self):
        return [f"[{tgl}] {isi}" for tgl, isi in self.__catatan]
