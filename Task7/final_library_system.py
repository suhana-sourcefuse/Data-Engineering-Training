# ---- Book Class ----
class Book:
    def __init__(self, title, author, isbn):
        self.title = title.strip().title()
        self.author = author.strip().title()
        self.isbn = isbn.strip()

    def display_details(self):
        print(f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn}")


# ---- EBook Subclass ----
class EBook(Book):
    def __init__(self, title, author, isbn, file_size, file_format):
        super().__init__(title, author, isbn)
        self.file_size = file_size  # in MB
        self.file_format = file_format.upper()

    def display_details(self):
        print(f"EBook -> Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Size: {self.file_size}MB | Format: {self.file_format}")


# ---- PrintedBook Subclass ----
class PrintedBook(Book):
    def __init__(self, title, author, isbn, num_pages):
        super().__init__(title, author, isbn)
        self.num_pages = num_pages

    def display_details(self):
        print(f"Printed Book -> Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Pages: {self.num_pages}")


# ---- User Class ----
class User:
    def __init__(self, username):
        self.username = username.strip().lower()
        self.checked_out_books = []

    def view_checked_out_books(self):
        if not self.checked_out_books:
            print(f"{self.username.title()} has not checked out any books.")
        else:
            print(f"\nBooks checked out by {self.username.title()}:")
            for book in self.checked_out_books:
                book.display_details()


# ---- Library Class ----
class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from library.")
                return
        print("Book not found.")

    def search_books(self, keyword):
        keyword = keyword.strip().lower()
        results = [
            book for book in self.books
            if keyword in book.title.lower() or keyword in book.author.lower() or keyword in book.isbn
        ]
        if results:
            print(f"\nSearch results for '{keyword}':")
            for book in results:
                book.display_details()
        else:
            print("No matching books found.")

    def display_all_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable books in the library:")
            for book in self.books:
                book.display_details()

    def register_user(self, username):
        username = username.strip().lower()
        if username in self.users:
            print("User already exists.")
        else:
            self.users[username] = User(username)
            print(f"User '{username.title()}' registered successfully.")

    def view_user_books(self, username):
        username = username.strip().lower()
        if username in self.users:
            self.users[username].view_checked_out_books()
        else:
            print("User not found.")

    def checkout_book(self, username, isbn):
        username = username.strip().lower()
        if username not in self.users:
            print("User not found.")
            return

        for book in self.books:
            if book.isbn == isbn:
                self.users[username].checked_out_books.append(book)
                self.books.remove(book)
                print(f"Book '{book.title}' checked out to {username.title()}.")
                return

        print("Book not found or already checked out.")

    def return_book(self, username, isbn):
        username = username.strip().lower()
        if username not in self.users:
            print("User not found.")
            return

        user = self.users[username]
        for book in user.checked_out_books:
            if book.isbn == isbn:
                user.checked_out_books.remove(book)
                self.books.append(book)
                print(f"Book '{book.title}' returned to library.")
                return

        print("Book not found in user's checked-out list.")

    def view_all_users(self):
        if not self.users:
            print("No users registered.")
        else:
            print("\nRegistered Users:")
            for username in self.users:
                print(f"- {username.title()}")

    def generate_report(self):
        total_books = len(self.books)
        total_users = len(self.users)
        checked_out_total = sum(len(user.checked_out_books) for user in self.users.values())

        print("\n--- Library Report ---")
        print(f"Total available books: {total_books}")
        print(f"Total registered users: {total_users}")
        print(f"Total books checked out: {checked_out_total}")

if __name__ == "__main__":
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Printed Book")
        print("2. Add EBook")
        print("3. Register User")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. View All Books")
        print("7. View User's Books")
        print("8. Search Book")
        print("9. View All Users")
        print("10. Generate Report")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            pages = int(input("Number of pages: "))
            book = PrintedBook(title, author, isbn, pages)
            library.add_book(book)

        elif choice == "2":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            size = float(input("File size (MB): "))
            format = input("File format (e.g., pdf, epub): ")
            book = EBook(title, author, isbn, size, format)
            library.add_book(book)

        elif choice == "3":
            username = input("Enter username: ")
            library.register_user(username)

        elif choice == "4":
            username = input("Enter username: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            library.checkout_book(username, isbn)

        elif choice == "5":
            username = input("Enter username: ")
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(username, isbn)

        elif choice == "6":
            library.display_all_books()

        elif choice == "7":
            username = input("Enter username: ")
            library.view_user_books(username)

        elif choice == "8":
            keyword = input("Enter keyword to search: ")
            library.search_books(keyword)

        elif choice == "9":
            library.view_all_users()

        elif choice == "10":
            library.generate_report()

        elif choice == "0":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
