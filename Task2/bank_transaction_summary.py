# user details
name = input("Enter your name: ")
balance = float(input("Enter your current balance: "))

n = int(input("How many transactions? "))

# transaction details
transactions = []

for i in range(n):
    print(f"\nTransaction {i+1}")
    amount = float(input("  Amount: "))
    t_type = input("  Type (credit/debit): ")

    transactions.append([amount, t_type])  # storing transaction as a list

# summary
print("\n--- Summary ---")
print("Name:", name)
print("Starting Balance:", balance)

for txn in transactions:
    amount, t_type = txn
    if t_type == 'credit':
        balance += amount
    else:
        balance -= amount
    print(f"{t_type.capitalize()} of {amount}")

print("Final Balance:", balance)