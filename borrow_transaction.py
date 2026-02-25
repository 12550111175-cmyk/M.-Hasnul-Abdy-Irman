class BorrowTransaction:
    def __init__(self, book, member, staff):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = "20-02-2026"
        self.returned = False

    def borrow_book(self):
        if not self.book.is_borrowed:
            self.book.borrow()
            self.member.borrowed_books.append(self)
            print(f" Transaksi diproses oleh staff: '{self.staff.name}'.")
        else:
            print(f"Yahh transaksinya gagal karena bukunya lagi dipinjem.")

    def return_book(self):
        if not self.returned:
            self.book.return_book()
            self.returned = True
            print(f"Buku dikembalikan dan diproses oleh staff : '{self.staff.name}'.")
        else:
            print(f"Bukunya udah dikembalikan sebelumnya broo.")
