# ==========================================
# Library Management System
# Day 7 Project
# ==========================================

library = []


def add_book():
    """Add a new book to the library."""

    print("\n------ Add Book ------")

    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    # Check if Book ID already exists
    for book in library:
        if book["id"] == book_id:
            print("❌ Book ID already exists!")
            return

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    library.append(book)

    print("✅ Book added successfully!")


def view_books():
    """Display all books."""

    print("\n------ Library Books ------")

    if len(library) == 0:
        print("No books available.")
        return

    for book in library:
        print("--------------------------------")
        print(f"Book ID   : {book['id']}")
        print(f"Title     : {book['title']}")
        print(f"Author    : {book['author']}")
        print(f"Available : {'Yes' if book['available'] else 'No'}")


def search_book():
    """Search a book by title."""

    print("\n------ Search Book ------")

    title = input("Enter Book Title: ").lower()

    found = False

    for book in library:
        if book["title"].lower() == title:
            found = True

            print("\nBook Found")
            print("----------------------------")
            print(f"Book ID   : {book['id']}")
            print(f"Title     : {book['title']}")
            print(f"Author    : {book['author']}")
            print(f"Available : {'Yes' if book['available'] else 'No'}")

    if not found:
        print("Book not found.")


def borrow_book():
    """Borrow a book."""

    print("\n------ Borrow Book ------")

    book_id = int(input("Enter Book ID: "))

    for book in library:

        if book["id"] == book_id:

            if book["available"]:
                book["available"] = False
                print("✅ Book Borrowed Successfully")
            else:
                print("❌ Book is already borrowed.")

            return

    print("Book not found.")


def return_book():
    """Return a borrowed book."""

    print("\n------ Return Book ------")

    book_id = int(input("Enter Book ID: "))

    for book in library:

        if book["id"] == book_id:

            if not book["available"]:
                book["available"] = True
                print("✅ Book Returned Successfully")
            else:
                print("Book is already available.")

            return

    print("Book not found.")


def delete_book():
    """Delete a book."""

    print("\n------ Delete Book ------")

    book_id = int(input("Enter Book ID: "))

    for book in library:

        if book["id"] == book_id:
            library.remove(book)
            print("✅ Book Deleted Successfully")
            return

    print("Book not found.")


def menu():
    """Display menu."""

    while True:

        print("\n")
        print("=" * 40)
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        print("=" * 40)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_book()

            elif choice == 2:
                view_books()

            elif choice == 3:
                search_book()

            elif choice == 4:
                borrow_book()

            elif choice == 5:
                return_book()

            elif choice == 6:
                delete_book()

            elif choice == 7:
                print("\nThank you for using Library Management System.")
                print("Goodbye!")
                break

            else:
                print("❌ Invalid Choice")

        except ValueError:
            print("❌ Please enter numbers only.")


# ===============================
# Program Starts Here
# ===============================

menu()