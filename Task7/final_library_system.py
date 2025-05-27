# Library Management System with Encapsulation and Admin Initialization

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def is_available(self):
        return self.__available

    def checkout(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

    def display_info(self):
        print(f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Available: {self.__available}")


class EBook(Book):
    def __init__(self, title, author, isbn, file_size, file_format):
        super().__init__(title, author, isbn)
        self.__file_size = file_size
        self.__file_format = file_format

    def display_info(self):
        super().display_info()
        print(f"[EBook] File Size: {self.__file_size}MB, Format: {self.__file_format}")


class PrintedBook(Book):
    def __init__(self, title, author, isbn, num_pages):
        super().__init__(title, author, isbn)
        self.__num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"[PrintedBook] Pages: {self.__num_pages}")


class User:
    def __init__(self, username):
        self.__username = username
        self.__checked_out_books = []

    def get_username(self):
        return self.__username

    def get_checked_out_books(self):
        return self.__checked_out_books

    def checkout_book(self, book):
        if book.checkout():
            self.__checked_out_books.append(book)
            print(f"{self.__username} checked out {book.get_title()}")
        else:
            print(f"{book.get_title()} is not available.")

    def return_book(self, book):
        if book in self.__checked_out_books:
            book.return_book()
            self.__checked_out_books.remove(book)
            print(f"{self.__username} returned {book.get_title()}")
        else:
            print(f"{self.__username} did not check out {book.get_title()}.")


class Library:
    def __init__(self):
        self.__books = []
        self.__users = {}
        self.__admin_user = User("admin")
        self.__users[self.__admin_user.get_username()] = self.__admin_user

    def add_book(self, book):
        self.__books.append(book)
        print(f"Book '{book.get_title()}' added to the library.")

    def register_user(self, username):
        if username not in self.__users:
            user = User(username)
            self.__users[username] = user
            print(f"User '{username}' registered.")
        else:
            print(f"User '{username}' already exists.")

    def get_user(self, username):
        return self.__users.get(username, None)

    def display_books(self):
        print("\nBooks in Library:")
        for book in self.__books:
            book.display_info()

    def display_users(self):
        print("\nRegistered Users:")
        for username in self.__users:
            print(f"- {username}")


def main():
    library = Library()

    while True:
        print("\nWelcome to the Library System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Enter username: ")
            user = library.get_user(username)
            if user:
                if username == "admin":
                    while True:
                        print("\nAdmin Menu:")
                        print("1. Add Printed Book")
                        print("2. Add EBook")
                        print("3. View All Books")
                        print("4. View All Users")
                        print("5. Logout")
                        admin_choice = input("Enter choice: ")
                        if admin_choice == '1':
                            title = input("Title: ")
                            author = input("Author: ")
                            isbn = input("ISBN: ")
                            pages = int(input("Number of Pages: "))
                            book = PrintedBook(title, author, isbn, pages)
                            library.add_book(book)
                        elif admin_choice == '2':
                            title = input("Title: ")
                            author = input("Author: ")
                            isbn = input("ISBN: ")
                            size = float(input("File Size (MB): "))
                            fmt = input("Format (e.g. PDF, EPUB): ")
                            book = EBook(title, author, isbn, size, fmt)
                            library.add_book(book)
                        elif admin_choice == '3':
                            library.display_books()
                        elif admin_choice == '4':
                            library.display_users()
                        elif admin_choice == '5':
                            break
                        else:
                            print("Invalid choice.")
                else:
                    while True:
                        print(f"\nWelcome, {username}!")
                        print("1. View My Books")
                        print("2. Checkout Book")
                        print("3. Return Book")
                        print("4. Logout")
                        user_choice = input("Enter choice: ")
                        if user_choice == '1':
                            books = user.get_checked_out_books()
                            if not books:
                                print("No books checked out.")
                            else:
                                for book in books:
                                    book.display_info()
                        elif user_choice == '2':
                            library.display_books()
                            title = input("Enter book title to checkout: ")
                            for book in library._Library__books:
                                if book.get_title() == title:
                                    user.checkout_book(book)
                                    break
                            else:
                                print("Book not found.")
                        elif user_choice == '3':
                            title = input("Enter book title to return: ")
                            for book in user.get_checked_out_books():
                                if book.get_title() == title:
                                    user.return_book(book)
                                    break
                            else:
                                print("Book not found in your checkout list.")
                        elif user_choice == '4':
                            break
                        else:
                            print("Invalid choice.")
            else:
                print("User not found. Please register first.")

        elif choice == '2':
            username = input("Enter new username: ")
            library.register_user(username)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()