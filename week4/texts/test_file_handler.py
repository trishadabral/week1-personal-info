"""
text_file_handler.py
Handles reading and writing expense data using TEXT (.txt) files
Useful for simple storage and understanding basic file handling
"""

import os

TEXT_DATA_FILE = "data/expenses.txt"


def save_expenses_to_text(expenses):
    """
    Saves expenses to a text file in readable format
    """
    os.makedirs("data", exist_ok=True)

    with open(TEXT_DATA_FILE, "w") as file:
        for expense in expenses:
            file.write(
                f"{expense.date},"
                f"{expense.amount},"
                f"{expense.category},"
                f"{expense.description}\n"
            )


def load_expenses_from_text():
    """
    Loads expenses from a text file
    Returns list of dictionaries
    """
    expenses = []

    if not os.path.exists(TEXT_DATA_FILE):
        return expenses

    with open(TEXT_DATA_FILE, "r") as file:
        for line in file:
            date, amount, category, description = line.strip().split(",")

            expenses.append({
                "date": date,
                "amount": float(amount),
                "category": category,
                "description": description
            })

    return expenses
