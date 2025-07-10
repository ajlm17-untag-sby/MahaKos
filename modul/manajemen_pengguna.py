class UserManager:
    def __init__(self, daftar_pengguna):
        self.__daftar_pengguna = daftar_pengguna

    def tampilkan_semua_pengguna(self):
        if not self.__daftar_pengguna:
            print("Belum ada pengguna terdaftar.")
        else:
            print("\n=== Daftar Pengguna ===")
            for i, user in enumerate(self.__daftar_pengguna, 1):
                print(f"{i}. {user.get_username()} - {user.get_nama()}")

    def cari_pengguna(self, username):
        for user in self.__daftar_pengguna:
            if user.get_username() == username:
                return user
        return None

    def reset_password(self, username, password_baru):
        user = self.cari_pengguna(username)
        if user:
            user.set_password(password_baru)
            print(f"Password untuk {username} berhasil direset.")
        else:
            print("Pengguna tidak ditemukan.")

    def ubah_nama(self, username, nama_baru):
        user = self.cari_pengguna(username)
        if user:
            user.set_nama(nama_baru)
            print(f"Nama pengguna {username} berhasil diubah.")
        else:
            print("Pengguna tidak ditemukan.")

    def hapus_pengguna(self, username):
        user = self.cari_pengguna(username)
        if user:
            self.__daftar_pengguna.remove(user)
            print(f"Pengguna {username} berhasil dihapus.")
        else:
            print("Pengguna tidak ditemukan.")

    def get_daftar_pengguna(self):
        return self.__daftar_pengguna
