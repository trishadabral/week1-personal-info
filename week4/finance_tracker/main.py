"""
main.py
Complete menu-driven Personal Finance Tracker
Implements ALL required options (1–9)
"""

from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import (
    save_expenses,
    load_expenses,
    backup_data
)
from finance_tracker.reports import monthly_report, category_breakdown
from finance_tracker.utils import print_divider
import csv
import os


class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.budget = None
        self.load_existing_data()

    # ---------- DATA LOADING ----------
    def load_existing_data(self):
        data = load_expenses()
        for item in data:
            expense = Expense(
                item["date"],
                item["amount"],
                item["category"],
                item["description"]
            )
            self.manager.add_expense(expense)

    # ---------- OPTION 1 ----------
    def add_expense(self):
        print("\nADD NEW EXPENSE")
        try:
            date = input("Date (YYYY-MM-DD): ")
            amount = input("Amount: ")
            category = input("Category: ")
            description = input("Description: ")

            expense = Expense(date, amount, category, description)
            self.manager.add_expense(expense)
            save_expenses(self.manager.get_all_expenses())

            print("✅ Expense added successfully!")
        except Exception as e:
            print("❌ Error:", e)

    # ---------- OPTION 2 ----------
    def view_expenses(self):
        print("\nALL EXPENSES")
        expenses = self.manager.get_all_expenses()

        if not expenses:
            print("No expenses found.")
            return

        for i, e in enumerate(expenses):
            print(f"{i}. {e.date} | ₹{e.amount} | {e.category} | {e.description}")

    # ---------- OPTION 3 ----------
    def search_expenses(self):
        category = input("Enter category to search: ")
        results = self.manager.search_by_category(category)

        if not results:
            print("No expenses found for this category.")
            return

        for e in results:
            print(f"{e.date} | ₹{e.amount} | {e.category} | {e.description}")

    # ---------- OPTION 4 ----------
    def generate_monthly_report(self):
        month = input("Enter month (MM): ")
        total = monthly_report(load_expenses(), month)
        print(f"📊 Total expense for month {month}: ₹{total}")

    # ---------- OPTION 5 ----------
    def view_category_breakdown(self):
        breakdown = category_breakdown(load_expenses())

        print("\nCATEGORY BREAKDOWN")
        for category, amount in breakdown.items():
            print(f"{category}: ₹{amount}")

    # ---------- OPTION 6 ----------
    def set_budget(self):
        try:
            self.budget = float(input("Enter monthly budget amount: "))
            print(f"✅ Budget set to ₹{self.budget}")
        except ValueError:
            print("❌ Invalid amount")

    # ---------- OPTION 7 ----------
    def export_data(self):
        os.makedirs("data/exports", exist_ok=True)
        file_path = "data/exports/expenses.csv"

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])

            for e in self.manager.get_all_expenses():
                writer.writerow([e.date, e.amount, e.category, e.description])

        print("📤 Data exported to CSV successfully!")

    # ---------- OPTION 8 ----------
    def view_statistics(self):
        expenses = self.manager.get_all_expenses()

        if not expenses:
            print("No data available.")
            return

        total = sum(e.amount for e in expenses)
        avg = total / len(expenses)

        print("\nSTATISTICS")
        print(f"Total Expenses: ₹{total}")
        print(f"Average Expense: ₹{avg:.2f}")
        print(f"Number of Expenses: {len(expenses)}")

        if self.budget:
            print(f"Remaining Budget: ₹{self.budget - total}")

    # ---------- OPTION 9 ----------
    def backup_restore(self):
        try:
            backup_data()
            print("💾 Backup created successfully!")
        except Exception as e:
            print("❌ Backup failed:", e)

    # ---------- MAIN LOOP ----------
    def run(self):
        while True:
            print_divider()
            print("PERSONAL FINANCE TRACKER")
            print_divider()
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")

            choice = input("Enter your choice (0-9): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.search_expenses()
            elif choice == "4":
                self.generate_monthly_report()
            elif choice == "5":
                self.view_category_breakdown()
            elif choice == "6":
                self.set_budget()
            elif choice == "7":
                self.export_data()
            elif choice == "8":
                self.view_statistics()
            elif choice == "9":
                self.backup_restore()
            elif choice == "0":
                print("👋 Thank you for using Personal Finance Tracker!")
                break
            else:
                print("❌ Invalid choice! Please enter 0–9.")
