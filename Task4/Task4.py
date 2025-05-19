import logging

# Setup logging for errors and info
logging.basicConfig(
    filename="banking_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---- Global Data ----
users = {}

# ---- Function to Add a New User ----
def add_user(name):
    """Add a new user to the system (case-insensitive)."""
    name = name.lower()
    if name in users:
        print(f"{name.title()} already has an account.")
    else:
        users[name] = []
        print(f"Account created for {name.title()}.")

# ---- Function to Add a Transaction ----
def add_transaction(name):
    """Add a transaction for a user."""
    name = name.lower()
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        t_type = input("Enter type (credit/debit): ").strip().lower()
        if t_type not in ["credit", "debit"]:
            raise ValueError("Invalid transaction type.")
        desc = input("Enter description: ").strip()
        transaction = {"amount": amount, "type": t_type, "desc": desc}
        users[name].append(transaction)
        print("Transaction added successfully!")
        logging.info(f"Transaction added for {name}: {transaction}")
    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"Transaction error for {name}: {ve}")

# ---- Function to View Transactions ----
def view_transactions(name):
    """Display all transactions for a user."""
    name = name.lower()
    if not users.get(name):
        print("No transactions found.")
        return
    print(f"\nTransactions for {name.title()}:")
    for idx, t in enumerate(users[name], start=1):
        print(f"{idx}. {t['type'].title()} of ₹{t['amount']:.2f} for '{t['desc']}'")

# ---- Function to Delete a Transaction ----
def delete_transaction(name):
    """Delete a specific transaction for a user."""
    name = name.lower()
    if not users.get(name):
        print("No transactions to delete.")
        return
    view_transactions(name)
    try:
        index = int(input("Enter transaction number to delete: ")) - 1
        if 0 <= index < len(users[name]):
            removed = users[name].pop(index)
            print(f"Deleted: {removed}")
            logging.info(f"Transaction deleted for {name}: {removed}")
        else:
            print("Invalid transaction number.")
            logging.warning(f"User {name} entered invalid transaction number {index+1} for deletion.")
    except ValueError:
        print("Please enter a valid number.")
        logging.error(f"Invalid input for deleting transaction by user {name}")

# ---- Function to View Balance ----
def view_balance(name):
    """Display current balance for a user."""
    name = name.lower()
    if name not in users or not users[name]:
        print("No transactions to calculate balance.")
        return
    balance = 0
    for t in users[name]:
        if t["type"] == "credit":
            balance += t["amount"]
        elif t["type"] == "debit":
            balance -= t["amount"]
    print(f"Current balance for {name.title()}: ₹{balance:.2f}")

# ---- Submenu for Logged-in User ----
def user_menu(name):
    """Submenu for logged-in user actions."""
    name = name.lower()
    while True:
        print(f"\n--- Welcome, {name.title()} ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. View Balance")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_transaction(name)
        elif choice == "2":
            view_transactions(name)
        elif choice == "3":
            delete_transaction(name)
        elif choice == "4":
            view_balance(name)
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")
            logging.warning(f"User {name} selected invalid option in user menu: {choice}")

# ---- Main Program Loop ----
def main():
    """Main login loop for the banking system."""
    while True:
        print("\n--- Banking System Login ---")
        print("1. New User")
        print("2. Returning User")
        print("3. Exit")
        
        login_choice = input("Choose an option (1-3): ")
        
        if login_choice == "1":
            name = input("Enter new user name: ").strip()
            add_user(name)
            user_menu(name)
        elif login_choice == "2":
            name = input("Enter your user name: ").strip().lower()
            if name in users:
                print(f"Welcome back, {name.title()}!")
                user_menu(name)
            else:
                print("User not found. Please sign up first.")
                logging.warning(f"Returning user attempted login but user not found: {name}")
        elif login_choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
            logging.warning(f"Invalid input at main login menu: {login_choice}")

# ---- Run the program ----
if __name__ == "__main__":
    main()