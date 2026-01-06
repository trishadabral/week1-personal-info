"""
expense_manager.py
Handles collection of expenses
"""

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        """
        Adds a new expense
        """
        self.expenses.append(expense)

    def remove_expense(self, index):
        """
        Removes expense by index
        """
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
        else:
            raise IndexError("Invalid expense index")

    def search_by_category(self, category):
        """
        Returns expenses of a specific category
        """
        return [
            e for e in self.expenses
            if e.category.lower() == category.lower()
        ]

    def get_all_expenses(self):
        """
        Returns all expenses
        """
        return self.expenses
