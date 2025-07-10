from datetime import datetime

class JadwalPerkuliahan:
    def __init__(self, kode, mata_kuliah, hari, jam_mulai, jam_selesai, ruang):
        self.__kode = kode
        self.__mata_kuliah = mata_kuliah
        self.__hari = hari
        self.__jam_mulai = jam_mulai
        self.__jam_selesai = jam_selesai
        self.__ruang = ruang

    def get_data(self):
        return (self.__kode, self.__mata_kuliah, self.__hari, self.__jam_mulai, self.__jam_selesai, self.__ruang)

    def tampilkan(self, no):
        print(f"| {no:<3}| {self.__kode:<11} | {self.__mata_kuliah:<38} | {self.__hari:<9}| {self.__jam_mulai} - {self.__jam_selesai} | {self.__ruang:<5} |")

    def set_mata_kuliah(self, nama_baru):
        self.__mata_kuliah = nama_baru

    def set_jadwal(self, hari, jam_mulai, jam_selesai):
        self.__hari = hari
        self.__jam_mulai = jam_mulai
        self.__jam_selesai = jam_selesai

    def set_ruang(self, ruang_baru):
        self.__ruang = ruang_baru


class Tugas:
    def __init__(self, kode, mata_kuliah, keterangan, deadline):
        self.__kode = kode
        self.__mata_kuliah = mata_kuliah
        self.__tanggal_dibuat = datetime.now().strftime("%Y-%m-%d")
        self.__keterangan = keterangan
        self.__deadline = deadline

    def get_data(self):
        return (self.__kode, self.__mata_kuliah, self.__tanggal_dibuat, self.__keterangan, self.__deadline)

    def tampilkan_tugas(self, no):
        print(f"{no}. {self.__kode} | {self.__mata_kuliah} | Dibuat: {self.__tanggal_dibuat} | Deadline: {self.__deadline} | {self.__keterangan}")

    def set_keterangan(self, ket_baru):
        self.__keterangan = ket_baru

    def set_deadline(self, deadline_baru):
        self.__deadline = deadline_baru
