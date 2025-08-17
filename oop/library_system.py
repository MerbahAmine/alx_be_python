# library_system.py

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived class for ebooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        # call parent constructor
        Book.__init__(self, title, author)
        self.file_size = file_size

# Derived class for printed books
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # call parent constructor
        Book.__init__(self, title, author)
        self.page_count = page_count

# Library class using composition
class Library:
    def __init__(self):
        self.books = []   # start with empty list

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            # check type of book
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, {book.page_count} pages")
            else:
                print(f"Book: {book.title} by {book.author}")
