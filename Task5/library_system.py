# ---- Book Class ----
class Book:
    def __init__(self, title, author, isbn):
        self.title = title.strip().title()
        self.author = author.strip().title()
        self.isbn = isbn.strip()

    def display_details(self):
        print(f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn}")


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
        self.books = []        # Available books
        self.users = {}        # username: User object

    # Add a book to the library
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    # Remove a book using ISBN
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from library.")
                return
        print("Book not found.")

    # Search books by title, author, or ISBN
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

    # Display all available books
    def display_all_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable books in the library:")
            for book in self.books:
                book.display_details()

    # Register a new user
    def register_user(self, username):
        username = username.strip().lower()
        if username in self.users:
            print("User already exists.")
        else:
            self.users[username] = User(username)
            print(f"User '{username.title()}' registered successfully.")

    # View a user's checked-out books
    def view_user_books(self, username):
        username = username.strip().lower()
        if username in self.users:
            self.users[username].view_checked_out_books()
        else:
            print("User not found.")


# ---- Main interactive menu ----
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
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == "2":
            isbn = input("Enter ISBN of book to remove: ")
            library.remove_book(isbn)
        elif choice == "3":
            keyword = input("Enter keyword to search (title, author, or ISBN): ")
            library.search_books(keyword)
        elif choice == "4":
            library.display_all_books()
        elif choice == "5":
            username = input("Enter username to register: ")
            library.register_user(username)
        elif choice == "6":
            username = input("Enter username to view checked-out books: ")
            library.view_user_books(username)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

            
if __name__ == "__main__":
    main()