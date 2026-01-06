"""
text_expenses.py
Handles saving and loading expenses using TEXT (.txt) files.

This module demonstrates:
- Basic file handling
- Working with .txt files
- Read / Write operations
- Error handling
- Simple data parsing
"""

import os

# Path for text file storage
TEXT_FILE_PATH = "data/expenses.txt"


def save_expenses_to_text(expenses):
    """
    Saves expense objects to a text file.

    Each expense is stored in one line using comma-separated values.
    Format:
    date,amount,category,description
    """

    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    try:
        with open(TEXT_FILE_PATH, "w") as file:
            for expense in expenses:
                file.write(
                    f"{expense.date},"
                    f"{expense.amount},"
                    f"{expense.category},"
                    f"{expense.description}\n"
                )
    except IOError as e:
        print("Error while writing to text file:", e)


def load_expenses_from_text():
    """
    Loads expenses from a text file.

    Returns:
        List of dictionaries representing expenses
    """

    expenses = []

    # If file does not exist, return empty list
    if not os.path.exists(TEXT_FILE_PATH):
        return expenses

    try:
        with open(TEXT_FILE_PATH, "r") as file:
            for line in file:
                # Remove newline and split values
                date, amount, category, description = line.strip().split(",")

                expenses.append({
                    "date": date,
                    "amount": float(amount),
                    "category": category,
                    "description": description
                })

    except IOError as e:
        print("Error while reading text file:", e)
    except ValueError:
        print("Data format error in text file")

    return expenses
