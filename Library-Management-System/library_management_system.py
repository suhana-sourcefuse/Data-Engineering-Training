import json
import pandas as pd
import os

class Book:
    def __init__(self, isbn, title, author, available=True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = available

    def get_details(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def is_available(self):
        return self.available

    def checkout(self):
        if self.available:
            self.available = False
            return True
        return False

class EBook(Book):
    def get_details(self):
        return f"[EBook] {super().get_details()}"

class PrintedBook(Book):
    def get_details(self):
        return f"[PrintedBook] {super().get_details()}"

class User:
    def __init__(self, username):
        self.username = username
        self.checked_out_books = []

    def checkout_book(self, book):
        if book.checkout():
            self.checked_out_books.append(book.isbn)
            return True
        return False

class Library:
    def __init__(self):
        self.books = self.load_books()
        self.users = self.load_users()

    def load_books(self):
        self.book_objects = []
        books_path = os.path.join("data", "books.csv")
        if os.path.exists(books_path):
            df = pd.read_csv(books_path)
            if 'Type' not in df.columns:
                print("Error: 'Type' column missing in books.csv")
                return df
            for _, row in df.iterrows():
                book_type = row["Type"]
                isbn = str(row["ISBN"])
                title = row["Title"]
                author = row["Author"]
                available = row.get("Available", True)
                if isinstance(available, str):
                    available = available.lower() == 'true'
                if book_type == "EBook":
                    book = EBook(isbn, title, author, available)
                else:
                    book = PrintedBook(isbn, title, author, available)
                self.book_objects.append(book)
            return df
        else:
            return pd.DataFrame(columns=["ISBN", "Title", "Author", "Available", "Type"])

    def save_books(self):
        books_path = os.path.join("data", "books.csv")
        data = []
        for book in self.book_objects:
            data.append({
                "ISBN": book.isbn,
                "Title": book.title,
                "Author": book.author,
                "Available": book.available,
                "Type": type(book).__name__
            })
        self.books = pd.DataFrame(data)
        self.books.to_csv(books_path, index=False)

    def load_users(self):
        users_path = os.path.join("data", "users.json")
        if os.path.exists(users_path):
            with open(users_path, "r") as f:
                return json.load(f)
        return {}

    def save_users(self):
        users_path = os.path.join("data", "users.json")
        with open(users_path, "w") as f:
            json.dump(self.users, f, indent=4)

    def add_book(self):
        isbn = input("Enter ISBN: ").strip()
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        book_type = input("Type (EBook/PrintedBook): ").strip()
        if book_type == "EBook":
            new_book = EBook(isbn, title, author)
        else:
            new_book = PrintedBook(isbn, title, author)
        self.book_objects.append(new_book)
        self.save_books()
        print("✅ Book added successfully.")

    def view_all_books(self):
        print("\n📚 Available Books:")
        for book in self.book_objects:
            status = "Available" if book.available else "Checked Out"
            print(f"- {book.get_details()} | Status: {status}")

    def view_users(self):
        print("\n👥 Registered Users:")
        for username, data in self.users.items():
            books = data.get("checked_out_books", [])
            print(f"- {username}: Books Checked Out - {books}")

    def checkout_flow(self, username):
        if username not in self.users:
            self.users[username] = {"checked_out_books": []}

        print("\n📖 Available Books for Checkout:")
        available_books = [book for book in self.book_objects if book.available]
        for book in available_books:
            print(f"- {book.get_details()}")

        isbn_input = input("Enter the ISBN of the book to check out: ").strip()
        book = next((b for b in available_books if b.isbn == isbn_input), None)

        if book:
            book.available = False
            self.users[username]["checked_out_books"].append(book.isbn)
            print(f"✅ Book '{book.title}' checked out successfully!")
            self.save_books()
            self.save_users()
        else:
            print("❌ Invalid ISBN or book not available.")

def main():
    print("📚 Welcome to the Library Management System!")
    print("---------------------------------------------")

    role = input("Are you an admin or user? (admin/user): ").strip().lower()
    username = input("Enter your username: ").strip()
    library = Library()

    # Register user immediately after login
    if username not in library.users:
        library.users[username] = {"checked_out_books": []}
        library.save_users()

    if role == "admin":
        while True:
            print("\n1. Add Book\n2. View All Books\n3. View Users\n4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                library.add_book()
            elif choice == "2":
                library.view_all_books()
            elif choice == "3":
                library.view_users()
            elif choice == "4":
                print("👋 Exiting admin panel.")
                break
            else:
                print("❌ Invalid choice.")
    else:
        while True:
            print("\n1. View Books\n2. Checkout Book\n3. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                library.view_all_books()
            elif choice == "2":
                library.checkout_flow(username)
            elif choice == "3":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice.")

if __name__ == "__main__":
    main()