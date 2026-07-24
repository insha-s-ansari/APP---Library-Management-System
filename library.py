class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)
        print()


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display(self):
        print("Patron:", self.name)
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book.title)
        else:
            print("No books borrowed.")
        print()


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'Book "{title}" added successfully.')

    def register_patron(self, name):
        new_patron = Patron(name)
        self.patrons.append(new_patron)
        print(f'Patron "{name}" registered successfully.')

    def borrow_book(self, patron_name, book_title):
        patron = None
        book = None

        # Find patron
        for p in self.patrons:
            if p.name == patron_name:
                patron = p
                break

        if patron is None:
            print("Patron not found.")
            return

        # Find book
        for b in self.books:
            if b.title == book_title:
                book = b
                break

        if book is None:
            print("Book not found.")
            return

        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f'{patron.name} borrowed "{book.title}".')
        else:
            print("Book is already borrowed.")

    def return_book(self, patron_name, book_title):
        patron = None

        for p in self.patrons:
            if p.name == patron_name:
                patron = p
                break

        if patron is None:
            print("Patron not found.")
            return

        for book in patron.borrowed_books:
            if book.title == book_title:
                book.available = True
                patron.borrowed_books.remove(book)
                print(f'{patron.name} returned "{book.title}".')
                return

        print("Book not borrowed by this patron.")

    def show_books(self):
        print("\n------ LIBRARY BOOKS ------")
        for book in self.books:
            book.display()

    def show_patrons(self):
        print("\n------ LIBRARY PATRONS ------")
        for patron in self.patrons:
            patron.display()


# Driver Code
library = Library()

library.add_book("Python", "John")
library.add_book("Java", "Johny")

library.register_patron("Isha")
library.register_patron("Neha")

library.borrow_book("Isha", "Python")
library.borrow_book("Neha", "Java")

library.show_books()
library.show_patrons()

library.return_book("Isha", "Python")

library.show_books()
library.show_patrons()
                        
