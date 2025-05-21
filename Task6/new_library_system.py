# -------- Book Class --------
class Book:
    def __init__(self, title, author, isbn):
        self.title = title.strip().title()
        self.author = author.strip().title()
        self.isbn = isbn.strip()

    def display_details(self):
        print(f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn}")


# -------- User Class --------
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


# -------- Library Class --------
class Library:
    def __init__(self):
        self.books = []        # List of available books
        self.users = {}        # Dict of users: {username: User object}

    # Book operations
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
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
            if keyword in book.title.lower() or
               keyword in book.author.lower() or
               keyword in book.isbn
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

    # User operations
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
                print(f"Book '{book.title}' returned by {username.title()}.")
                return

        print("Book not found in user's checked-out list.")

    # Admin operations
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
        checked_out_count = sum(len(user.checked_out_books) for user in self.users.values())

        print("\n--- Library Report ---")
        print(f"Total registered users      : {total_users}")
        print(f"Total available books       : {total_books}")
        print(f"Total books checked out     : {checked_out_count}")


# -------- Main Menu --------
def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Books")
        print("4. Display All Books")
        print("5. Register User")
        print("6. View User Checked-Out Books")
        print("7. Check Out Book")
        print("8. Return Book")
        print("9. View All Users")
        print("10. Generate Report")
        print("11. Exit")

        choice = input("Enter choice (1-11): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == '2':
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            keyword = input("Enter keyword (title, author, or ISBN): ")
            library.search_books(keyword)

        elif choice == '4':
            library.display_all_books()

        elif choice == '5':
            username = input("Enter username to register: ")
            library.register_user(username)

        elif choice == '6':
            username = input("Enter username to view checked-out books: ")
            library.view_user_books(username)

        elif choice == '7':
            username = input("Enter username: ")
            isbn = input("Enter ISBN of the book to check out: ")
            library.checkout_book(username, isbn)

        elif choice == '8':
            username = input("Enter username: ")
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(username, isbn)

        elif choice == '9':
            library.view_all_users()

        elif choice == '10':
            library.generate_report()

        elif choice == '11':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 11.")


# Run the program
if __name__ == "__main__":
    main()