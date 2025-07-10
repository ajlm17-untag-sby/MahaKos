class Pengguna:
    def __init__(self, username, password, nama, nim):
        self.__username = username
        self.__password = password
        self.__nama = nama
        self.__nim = nim

    def verifikasi_login(self, username, password):
        return self.__username == username and self.__password == password

    def get_nama(self):
        return self.__nama

    def get_username(self):
        return self.__username

    def get_data(self):
        return (self.__username, self.__password, self.__nama, self.__nim)

    def set_nama(self, nama_baru):
        if nama_baru.strip():
            self.__nama = nama_baru
        else:
            print("Nama tidak boleh kosong.")

    def set_password(self, password_baru):
        if len(password_baru) >= 6:
            self.__password = password_baru
        else:
            print("Password minimal 6 karakter.")

class Mahasiswa(Pengguna):
    def __init__(self, username, password, nama, nim):
        super().__init__(username, password, nama, nim)

    def info_mahasiswa(self):
        return f"{self.get_nama()} - NIM: {self.get_data()[3]}"
