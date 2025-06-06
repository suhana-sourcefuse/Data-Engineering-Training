# 💰 Personal Budget Tracker (CLI)

A lightweight, terminal-based budget tracking application built with Python. Users can add income and expenses, view summaries, and inspect transaction history — all stored persistently in a CSV file.

---

## 🚀 Features

- Track incomes and expenses with descriptions and categories
- Automatically calculates total income, expenses, and balance
- Transaction history stored in `transactions.csv`
- Colorful CLI output using `rich`
- Logging of all actions to `budget_log.txt`
- Robust input validation for real-world reliability

---

## 🛠️ Tech Stack

- Python 3.8+
- `pandas` for data manipulation
- `rich` for beautifully formatted CLI tables
- `logging` for tracking internal events

---

## ▶️ How to Run
- Make sure you have Python 3 installed.
- Install the required package:
  pip install pandas

- Run the program:
  python3 budget.py