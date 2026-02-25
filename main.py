from book import Book
from member import Member
from staff import Staff
from borrow_transaction import BorrowTransaction

#Disini bagian kita buat objeknya lek
book1 = Book("Fikih Akhlak", "Syaikh Musthofa al-'Adawy", "978-979-3715-40-5")
member1 = Member("Abedy", "12345")
staff1 = Staff("MiminGanteng", "M012")

#membuat Transaksi
transaksi1 = BorrowTransaction(book1, member1, staff1)

#Proses Peminjaman
transaksi1.borrow_book()

#Proses Pengembalian 
transaksi1.return_book()