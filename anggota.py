from buku import Buku

class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.daftar_buku_dipinjam = []

    def pinjam_buku(self, buku):
        if buku.status == "Tersedia":
            buku.ubah_status("Dipinjam")
            self.daftar_buku_dipinjam.append(buku)
            print(f"{self.nama} berhasil meminjam '{buku.judul}'")
        else:
            print(f"Buku '{buku.judul}' sedang tidak tersedia")

    def kembalikan_buku(self, buku):
        if buku in self.daftar_buku_dipinjam:

            #ubah buku jadi tersedia kembali
            buku.ubah_status("Tersedia")

            #hapus buku dari daftar buku yg telah dipinjam
            self.daftar_buku_dipinjam.remove(buku)
            print(f"{self.nama} berhasil mengembalikan '{buku.judul}'")
        else:
            print(f"{self.nama} tidak meminjam buku '{buku.judul}'")



            