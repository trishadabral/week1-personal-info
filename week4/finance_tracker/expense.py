"""
expense.py
Defines the Expense class and validation logic
"""

from datetime import datetime


class Expense:
    """
    Represents a single expense entry
    """

    def __init__(self, date, amount, category, description):
        self.date = self.validate_date(date)
        self.amount = self.validate_amount(amount)
        self.category = category.strip()
        self.description = description.strip()

    def validate_date(self, date):
        """
        Validates date format (YYYY-MM-DD)
        """
        try:
            return datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

    def validate_amount(self, amount):
        """
        Ensures amount is positive
        """
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        return amount

    def to_dict(self):
        """
        Converts object to dictionary for JSON storage
        """
        return {
            "date": self.date.strftime("%Y-%m-%d"),
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
