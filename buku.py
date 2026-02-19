class Buku:
    def __init__(self, judul, penulis, tahun_terbit, isbn, penerbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.isbn = isbn
        self.penerbit = penerbit
        self.status = "Tersedia"

    def tampilkan_info(self):
        print(f"judul       :{self.judul}")
        print(f"penulis     :{self.penulis}")
        print(f"tahun terbit:{self.tahun_terbit}")
        print(f"isbn        :{self.isbn}")
        print(f"penerbit    :{self.penerbit}")
        print(f"status      :{self.status}")
        print("-" * 30)

    def ubah_status(self, status_baru):
        self.status = status_baru   