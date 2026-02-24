class Book:
    def __init__(self, title, author, isbn):
        if not Book.is_valid_isbn(isbn):
            raise ValueError("ISBN-ში უნდა შედიოდეს მხოლოდ 13 ციფრი")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.__is_available = True

    def __str__(self):
        return f"{self.title} | {self.author} > {self.status}"

    @property
    def status(self):
        return "ხელმისაწვდომია" if self.__is_available else "გატანილია"

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            return True
        return False

    @classmethod
    def create_textbook(cls, title, author, isbn):
        return cls(title, author, isbn)

    @staticmethod
    def is_valid_isbn(isbn):
        return isinstance(isbn, str) and isbn.isdigit() and len(isbn) == 13


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

    @property
    def books_count(self):
        return len(self.borrowed_books)


class PremiumMember(Member):
    def __init__(self, name, member_id, max_books=5):
        super().__init__(name, member_id)
        self.max_books = max_books

    def borrow_book(self, book):
        if self.books_count >= self.max_books:
            return False
        return super().borrow_book(book)


book = Book("კვაჭი კვაჭანტირაძე", "მიხეილ ჯავახიშვილი", "1234567891234")
user = Member("ვარაზი", 1)

print(book)
user.borrow_book(book)
print(book)
user.return_book(book)
print(book)

premium = PremiumMember("ლევანი", 2)
print(f"Premium წიგნები: {book}")


b = Book(f"კვაჭი კვაჭანტირაძე", "მიხეილ ჯავახიშვილი", f"123456789")
print(premium.borrow_book(b))