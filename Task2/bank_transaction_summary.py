# Task 2 Extended: Multi-User Bank Transaction Summary with Detailed Transactions 
# Purpose: Store transactions for multiple users using dictionary, and display summaries

# Dictionary to store all user data
bank_data = {}

while True:
    name = input("\nEnter your name (or type 'done' to finish): ").strip()
    if name.lower() == 'done':
        break

    balance = float(input(f"Enter initial balance for {name}: "))
    num_transactions = int(input(f"How many transactions for {name}? "))

    transactions = []

    for i in range(num_transactions):
        print(f"\nTransaction {i + 1} for {name}:")
        amount = float(input("  Enter amount: "))
        txn_type = input("  Enter type (credit/debit): ").lower()
        description = input("  Enter description: ")

        # Validate transaction type
        if txn_type not in ['credit', 'debit']:
            print("  Invalid type! Defaulting to debit.")
            txn_type = 'debit'

        # Store each transaction as a tuple
        transactions.append((amount, txn_type, description))

    # Store all user info in dictionary
    bank_data[name] = {
        'initial_balance': balance,
        'transactions': transactions
    }

# Select a user to display transaction summary
print("\n All Users:")
for idx, user in enumerate(bank_data.keys(), 1):
    print(f"{idx}. {user}")

choice = int(input("\nEnter the number of the user to view their transaction summary: ")) - 1
selected_user = list(bank_data.keys())[choice]
user_data = bank_data[selected_user]

# Show summary
print(f"\n--- Transaction Summary for {selected_user} ---")
print(f"Initial Balance: ${user_data['initial_balance']:.2f}")
final_balance = user_data['initial_balance']

print("\nTransactions:")
for amount, txn_type, description in user_data['transactions']:
    if txn_type == 'credit':
        final_balance += amount
    else:
        final_balance -= amount
    print(f"  {txn_type.capitalize()} of ${amount:.2f} - {description}")

print(f"\nFinal Balance: ${final_balance:.2f}")

# Display of all stored data
view_all = input("\nDo you want to see all stored user transactions? (yes/no): ").strip().lower()
if view_all == 'yes':
    print("\n--- All Transactions in Memory ---")
    for user, data in bank_data.items():
        print(f"\nUser: {user}")
        print(f"  Initial Balance: ${data['initial_balance']:.2f}")
        print("  Transactions:")
        for amount, txn_type, description in data['transactions']:
            print(f"    {txn_type.capitalize()} of ${amount:.2f} - {description}")