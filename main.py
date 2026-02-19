from buku import Buku 
from anggota import Anggota
from pengelola import Pengelola

#ini membuat pengelola perpusnya
perpus = Pengelola("Perpustakaan Kampus")

#ini kita buat beberapa bukunya guys
buku1 = Buku("Change Your Habits", "Isnaeni Dk", "2018", "978-74793--9-5", "Caesar Media Pustaka")
buku2 = Buku("Dark Psychology", "Novita WD", "2024", "978-623-89303-2-6", "Jendela Penerbit")

#Tambahkan buku ke perpustakaan 
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

#Membuat anggota 
anggota1 = Anggota("Abdy", "0137")

#Daftarkan anggota ke perpustakaan
perpus.daftarkan_anggota(anggota1)

#cari buku
perpus.cari_buku("Change Your Habits")

#Anggota yang meminjam buku
anggota1.pinjam_buku(buku1)

#Cek status buku setelah dipinjam
buku1.tampilkan_info()

#Anggota yang mengembalikan buku
anggota1.kembalikan_buku(buku1)

#Anggota status buku lagi
buku1.tampilkan_info()
                
