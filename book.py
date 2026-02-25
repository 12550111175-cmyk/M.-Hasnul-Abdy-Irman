class Book:
    def __init__(self, title, author, isbn):
        self.title= title
        self.author= author
        self.isbn= isbn
        self.is_borrowed = False #Defaultnya itu belum dipinjam

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Buku '{self.title}' berhasil ente pinjem.")
        else:
            print(f"Maaf, buku '{self.title}' sedang dipinjem nih")

    def return_book(self):
        if  self.is_borrowed:
            self.is_borrowed = False
            print(f"Buku '{self.title}' berhasil anda kembalikan.")
        else:
            print(f"Waduh buku '{self.title}' memang tidak sedang dipinjem broo.")
