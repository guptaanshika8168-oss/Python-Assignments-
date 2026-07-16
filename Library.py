# Simple Library Management System (Interactive Version)
# Takes input from the user at every step


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added book: {title} by {author}")

    def register_patron(self, name):
        new_patron = Patron(name)
        self.patrons.append(new_patron)
        print(f"Registered patron: {name}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name.lower() == name.lower():
                return patron
        return None

    def borrow_book(self, patron_name, book_title):
        book = self.find_book(book_title)
        patron = self.find_patron(patron_name)

        if book is None:
            print("Book not found.")
        elif patron is None:
            print("Patron not found.")
        elif book.is_borrowed:
            print(f"Sorry, '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'.")

    def return_book(self, patron_name, book_title):
        book = self.find_book(book_title)
        patron = self.find_patron(patron_name)

        if book is None or patron is None:
            print("Book or patron not found.")
        elif book in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book)
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print(f"{patron_name} did not borrow '{book_title}'.")

    def show_books(self):
        print("\n--- Library Books ---")
        if not self.books:
            print("No books available.")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"- {book.title} by {book.author} ({status})")

    def show_patrons(self):
        print("\n--- Registered Patrons ---")
        if not self.patrons:
            print("No patrons registered.")
        for patron in self.patrons:
            titles = [b.title for b in patron.borrowed_books]
            print(f"- {patron.name} | Borrowed: {titles if titles else 'None'}")


def main():
    library = Library()

    # Pre-load some books so the library isn't empty at the start
    library.add_book("Harry Potter", "J.K. Rowling")
    library.add_book("The Hobbit", "J.R.R. Tolkien")
    library.add_book("1984", "George Orwell")

    while True:
        print("\n===== Library Menu =====")
        print("1. Show all books")
        print("2. Add a new book")
        print("3. Register a patron")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Show all patrons")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            library.show_books()

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == "3":
            name = input("Enter patron name: ")
            library.register_patron(name)

        elif choice == "4":
            library.show_books()
            patron_name = input("Enter your name: ")
            book_title = input("Enter the book title to borrow: ")
            library.borrow_book(patron_name, book_title)

        elif choice == "5":
            patron_name = input("Enter your name: ")
            book_title = input("Enter the book title to return: ")
            library.return_book(patron_name, book_title)

        elif choice == "6":
            library.show_patrons()

        elif choice == "7":
            print("Thank you for using the Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()