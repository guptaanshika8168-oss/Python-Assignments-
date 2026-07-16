books = []
patrons = []


def add_book(title, author):
    book = {"title": title, "author": author, "is_borrowed": False}
    books.append(book)
    print(f"Added book: {title} by {author}")


def register_patron(name):
    patron = {"name": name, "borrowed_books": []}
    patrons.append(patron)
    print(f"Registered patron: {name}")


def find_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None


def find_patron(name):
    for patron in patrons:
        if patron["name"].lower() == name.lower():
            return patron
    return None


def borrow_book(patron_name, book_title):
    book = find_book(book_title)
    patron = find_patron(patron_name)

    if book is None:
        print("Book not found.")
    elif patron is None:
        print("Patron not found.")
    elif book["is_borrowed"]:
        print(f"Sorry, '{book['title']}' is already borrowed.")
    else:
        book["is_borrowed"] = True
        patron["borrowed_books"].append(book["title"])
        print(f"{patron['name']} borrowed '{book['title']}'.")


def return_book(patron_name, book_title):
    book = find_book(book_title)
    patron = find_patron(patron_name)

    if book is None or patron is None:
        print("Book or patron not found.")
    elif book["title"] in patron["borrowed_books"]:
        book["is_borrowed"] = False
        patron["borrowed_books"].remove(book["title"])
        print(f"{patron['name']} returned '{book['title']}'.")
    else:
        print(f"{patron_name} did not borrow '{book_title}'.")


def show_books():
    print("\n--- Library Books ---")
    if not books:
        print("No books available.")
    for book in books:
        status = "Borrowed" if book["is_borrowed"] else "Available"
        print(f"- {book['title']} by {book['author']} ({status})")


def show_patrons():
    print("\n--- Registered Patrons ---")
    if not patrons:
        print("No patrons registered.")
    for patron in patrons:
        borrowed = patron["borrowed_books"] if patron["borrowed_books"] else "None"
        print(f"- {patron['name']} | Borrowed: {borrowed}")


def main():
    # Pre-load some books so the library isn't empty at the start
    add_book("Harry Potter", "J.K. Rowling")
    add_book("The Hobbit", "J.R.R. Tolkien")
    add_book("1984", "George Orwell")

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
            show_books()

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(title, author)

        elif choice == "3":
            name = input("Enter patron name: ")
            register_patron(name)

        elif choice == "4":
            show_books()
            patron_name = input("Enter your name: ")
            book_title = input("Enter the book title to borrow: ")
            borrow_book(patron_name, book_title)

        elif choice == "5":
            patron_name = input("Enter your name: ")
            book_title = input("Enter the book title to return: ")
            return_book(patron_name, book_title)

        elif choice == "6":
            show_patrons()

        elif choice == "7":
            print("Thank you for using the Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()