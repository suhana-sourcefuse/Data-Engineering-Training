# ---- Global Data ----
users = {}

# ---- Function to Add a New User ----
def add_user(name):
    """Add a new user to the system."""
    if name in users:
        print(f"{name} already has an account.")
    else:
        users[name] = []
        print(f"Account created for {name}.")

# ---- Function to Add an Income (Credit) Transaction ----
def add_income(name):
    """Add an income (credit) transaction for a user."""
    if name not in users:
        print("User not found. Please add the user first.")
        return
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    transaction = {"amount": amount, "type": "credit", "desc": description}
    users[name].append(transaction)
    print("Income added successfully!")

# ---- Function to Add an Expense (Debit) Transaction ----
def add_expense(name):
    """Add an expense (debit) transaction for a user."""
    if name not in users:
        print("User not found. Please add the user first.")
        return
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    transaction = {"amount": amount, "type": "debit", "desc": description}
    users[name].append(transaction)
    print("Expense added successfully!")

# ---- Function to View Transactions ----
def view_transactions(name):
    """Display all transactions for a user."""
    if name not in users:
        print("User not found.")
        return
    print(f"\nTransactions for {name}:")
    for idx, t in enumerate(users[name], start=1):
        print(f"{idx}. {t['type'].title()} of {t['amount']} for '{t['desc']}'")

# ---- Function to Delete a Transaction ----
def delete_transaction(name):
    """Delete a specific transaction for a user."""
    if name not in users:
        print("User not found.")
        return
    view_transactions(name)
    try:
        index = int(input("Enter transaction number to delete: ")) - 1
        if 0 <= index < len(users[name]):
            removed = users[name].pop(index)
            print(f"Deleted: {removed}")
        else:
            print("Invalid transaction number.")
    except ValueError:
        print("Please enter a valid number.")

# ---- Function to View Balance (Credit - Debit) ----
def view_balance(name):
    """View the current balance of a user."""
    if name not in users:
        print("User not found.")
        return
    balance = 0
    for transaction in users[name]:
        if transaction['type'] == 'credit':
            balance += transaction['amount']
        elif transaction['type'] == 'debit':
            balance -= transaction['amount']
    print(f"Current balance for {name}: {balance}")

# ---- Function to Create a User if Not Already Present ----
def create_user(name):
    """Ensure user exists before adding a transaction."""
    if name not in users:
        add_user(name)

# ---- Main Menu Function ----
def main():
    """Main program loop with user interaction."""
    while True:
        print("\n--- Banking System ---")
        print("1. Add User")
        print("2. Add Income (Credit)")
        print("3. Add Expense (Debit)")
        print("4. View Transactions")
        print("5. Delete Transaction")
        print("6. View Balance")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Enter user name: ").strip()
            add_user(name)
        elif choice == "2":
            name = input("Enter user name: ").strip()
            create_user(name)  # Ensures user exists before adding transaction
            add_income(name)
        elif choice == "3":
            name = input("Enter user name: ").strip()
            create_user(name)  # Ensures user exists before adding transaction
            add_expense(name)
        elif choice == "4":
            name = input("Enter user name: ").strip()
            view_transactions(name)
        elif choice == "5":
            name = input("Enter user name: ").strip()
            delete_transaction(name)
        elif choice == "6":
            name = input("Enter user name: ").strip()
            view_balance(name)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# ---- Run the program ----
if __name__ == "__main__":
    main()