class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        return f"{self._books}' by {self._books[1]}"
    
    def check_out_book(self, title):
        if isinstance(title, Book):
            self._books.remove(Book.title)
            status = "Checked Out" if self._is_checked_out else "Available"
            return f"'{self.title}' by {self.author} + {status}"
        
    def return_book(self, title):
        if isinstance(title, Book):
            self._books.append(Book.title)
        return f"{self.title}' by {self.author}"
    
    def list_available_books(self):
        return self._books