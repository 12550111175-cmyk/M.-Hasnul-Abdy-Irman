from buku import Buku
from anggota import Anggota

class Pengelola:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []      #ini untuk daftar buku nantinya
        self.daftar_anggota = []        #kalau ini untuk aftar anggotanya 

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' ditambahkan ke perpustakaan.")

    def hapus_buku(self, buku):
        if buku in self.daftar_buku:
            self.daftar_buku.remove(buku)
            print(f"Buku '{buku.judul}' telah dihapus dari perpustakaan.")
        else:
            print(f"Buku '{buku.judul}' tidak ditemukan di perpustakaan.")

    def daftarkan_anggota(self, anggota):
        self.daftar_anggota.append(anggota)
        print(f"Anggota '{anggota.nama}' berhasil ditambahkan.")

    def cari_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                print("Buku Ditemukan")
                buku.tampilkan_info()
                return
        print(f"Buku '{judul}' tidak ditemukan di perpustakaan")

            

