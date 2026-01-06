"""
file_handler.py
Handles file operations (JSON, backup, CSV)
"""

import json
import os
import shutil

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup/"


def save_expenses(expenses):
    """
    Saves expenses to JSON file
    """
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(
            [expense.to_dict() for expense in expenses],
            file,
            indent=4
        )


def load_expenses():
    """
    Loads expenses from JSON file
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def backup_data():
    """
    Creates backup of expense data
    """
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError("No data to backup")

    os.makedirs(BACKUP_DIR, exist_ok=True)
    shutil.copy(DATA_FILE, BACKUP_DIR + "expenses_backup.json")
