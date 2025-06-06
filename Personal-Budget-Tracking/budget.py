import pandas as pd
import os
import logging
from datetime import datetime
from rich.console import Console
from rich.table import Table

# Setup logging
logging.basicConfig(filename='budget_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize console
console = Console()

# File path for transactions
TRANSACTION_FILE = "transactions.csv"

# Ensure file exists with correct headers
if not os.path.exists(TRANSACTION_FILE):
    df = pd.DataFrame(columns=["Date", "Type", "Amount", "Category", "Description"])
    df.to_csv(TRANSACTION_FILE, index=False)

def load_data():
    return pd.read_csv(TRANSACTION_FILE)

def save_transaction(t_type, amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([[date, t_type, amount, category, description]],
                             columns=["Date", "Type", "Amount", "Category", "Description"])
    new_entry.to_csv(TRANSACTION_FILE, mode='a', header=False, index=False)
    logging.info(f"{t_type} transaction added: {amount} - {category} - {description}")
    console.print(f"[green]{t_type} recorded successfully![/green]")

def display_summary():
    df = load_data()
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expense = df[df['Type'] == 'Expense']['Amount'].sum()
    balance = income - expense

    table = Table(title="💰 Budget Summary")
    table.add_column("Total Income", justify="right")
    table.add_column("Total Expense", justify="right")
    table.add_column("Current Balance", justify="right")
    table.add_row(f"${income:.2f}", f"${expense:.2f}", f"${balance:.2f}")
    console.print(table)

def show_transactions():
    df = load_data()
    if df.empty:
        console.print("[yellow]No transactions recorded yet.[/yellow]")
        return

    table = Table(title="📄 All Transactions")
    for col in df.columns:
        table.add_column(col)

    for _, row in df.iterrows():
        table.add_row(*map(str, row))
    console.print(table)

def main():
    console.print("[bold cyan]=== Personal Budget Tracker ===[/bold cyan]")
    while True:
        console.print("\nChoose an option:\n1. Add Income\n2. Add Expense\n3. Show Summary\n4. Show Transactions\n5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter income amount: "))
                category = input("Enter income category: ")
                description = input("Enter description: ")
                save_transaction("Income", amount, category, description)
            except ValueError:
                logging.warning("Invalid income input.")
                console.print("[red]Invalid input. Please enter a number for amount.[/red]")

        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                description = input("Enter description: ")
                save_transaction("Expense", amount, category, description)
            except ValueError:
                logging.warning("Invalid expense input.")
                console.print("[red]Invalid input. Please enter a number for amount.[/red]")

        elif choice == '3':
            display_summary()

        elif choice == '4':
            show_transactions()

        elif choice == '5':
            console.print("[bold green]Goodbye![/bold green]")
            break

        else:
            console.print("[red]Invalid option. Please try again.[/red]")

if __name__ == "__main__":
    main()