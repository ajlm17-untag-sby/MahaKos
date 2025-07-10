class Transaksi:
    def __init__(self, tanggal, jam):
        self._tanggal = tanggal
        self._jam = jam

from datetime import datetime
from modul.abstract import FiturAplikasi

class TransaksiKeuangan(Transaksi, FiturAplikasi):
    def __init__(self, jenis, nominal, keterangan):
        tanggal = datetime.now().strftime("%Y-%m-%d")
        jam = datetime.now().strftime("%H:%M:%S")
        super().__init__(tanggal, jam)
        self.__jenis = jenis
        self.__nominal = nominal
        self.__keterangan = keterangan

    def get_data(self):
        return (self._tanggal, self._jam, self.__jenis, self.__nominal, self.__keterangan)

    def tampilkan(self, no):
        print(f"{no}. {self._tanggal} | {self._jam} | {self.__jenis} | Rp{self.__nominal} | {self.__keterangan}")

    def set_jenis(self, jenis):
        if jenis in ["pemasukan", "pengeluaran"]:
            self.__jenis = jenis

    def set_nominal(self, nominal):
        self.__nominal = nominal

    def set_keterangan(self, keterangan):
        self.__keterangan = keterangan


class ManajemenKeuangan:
    def __init__(self):
        self.__riwayat = []

    def tambah_transaksi(self, transaksi, silent=False):
        self.__riwayat.append(transaksi)
        if not silent:
            print("Transaksi berhasil ditambahkan.")

    def tampilkan_riwayat(self):
        if not self.__riwayat:
            print("Belum ada transaksi.")
        else:
            print("\n=== Riwayat Transaksi ===")
            for i, t in enumerate(self.__riwayat, 1):
                t.tampilkan(i)

    def hitung_saldo(self):
        saldo = 0
        for t in self.__riwayat:
            data = t.get_data()
            if data[2] == "pemasukan":
                saldo += data[3]
            elif data[2] == "pengeluaran":
                saldo -= data[3]
        return saldo

    def get_daftar_transaksi(self):
        return [t.get_data() for t in self.__riwayat]
