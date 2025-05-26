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

    def add_book(self, book, username):
        if username != 'admin':
            print("Only admin can add books.")
            return
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self, isbn, username):
        if username != 'admin':
            print("Only admin can remove books.")
            return
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

    def display_all_books(self, username):
        if username != 'admin':
            print("Only admin can view all books.")
            return
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

    def view_all_users(self, username):
        if username != 'admin':
            print("Only admin can view all users.")
            return
        if not self.users:
            print("No users registered.")
        else:
            print("\nRegistered Users:")
            for username in self.users:
                print(f"- {username.title()}")

    def generate_report(self, username):
        if username != 'admin':
            print("Only admin can generate report.")
            return
        total_books = len(self.books)
        total_users = len(self.users)
        checked_out_total = sum(len(user.checked_out_books) for user in self.users.values())

        print("\n--- Library Report ---")
        print(f"Total available books: {total_books}")
        print(f"Total registered users: {total_users}")
        print(f"Total books checked out: {checked_out_total}")


# ---- Main Menu System ----
def main():
    library = Library()

    while True:
        print("\nWelcome to the Library System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Enter username: ").strip().lower()
            if username not in library.users:
                print("User not found. Please register first.")
                continue

            print(f"\nWelcome, {username.title()}!")
            while True:
                if username == 'admin':
                    print("\nAdmin Menu:")
                    print("1. Add Printed Book")
                    print("2. Add EBook")
                    print("3. Remove Book")
                    print("4. Display All Books")
                    print("5. View All Users")
                    print("6. Generate Report")
                    print("7. Logout")
                    admin_choice = input("Enter choice: ")

                    if admin_choice == '1':
                        title = input("Title: ")
                        author = input("Author: ")
                        isbn = input("ISBN: ")
                        pages = int(input("Number of Pages: "))
                        book = PrintedBook(title, author, isbn, pages)
                        library.add_book(book, username)
                    elif admin_choice == '2':
                        title = input("Title: ")
                        author = input("Author: ")
                        isbn = input("ISBN: ")
                        size = float(input("File Size (MB): "))
                        fmt = input("File Format: ")
                        book = EBook(title, author, isbn, size, fmt)
                        library.add_book(book, username)
                    elif admin_choice == '3':
                        isbn = input("Enter ISBN to remove: ")
                        library.remove_book(isbn, username)
                    elif admin_choice == '4':
                        library.display_all_books(username)
                    elif admin_choice == '5':
                        library.view_all_users(username)
                    elif admin_choice == '6':
                        library.generate_report(username)
                    elif admin_choice == '7':
                        break
                    else:
                        print("Invalid choice.")
                else:
                    print("\nUser Menu:")
                    print("1. View My Books")
                    print("2. Search Books")
                    print("3. Checkout Book")
                    print("4. Return Book")
                    print("5. Logout")
                    user_choice = input("Enter choice: ")

                    if user_choice == '1':
                        library.view_user_books(username)
                    elif user_choice == '2':
                        keyword = input("Enter keyword to search: ")
                        library.search_books(keyword)
                    elif user_choice == '3':
                        isbn = input("Enter ISBN to checkout: ")
                        library.checkout_book(username, isbn)
                    elif user_choice == '4':
                        isbn = input("Enter ISBN to return: ")
                        library.return_book(username, isbn)
                    elif user_choice == '5':
                        break
                    else:
                        print("Invalid choice.")

        elif choice == '2':
            username = input("Enter new username: ").strip().lower()
            library.register_user(username)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
