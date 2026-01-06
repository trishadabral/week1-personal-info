"""
test_reports.py
Unit tests for reports.py module

Tests included:
- Monthly expense calculation
- Category-wise expense breakdown
"""

import unittest
from finance_tracker.reports import monthly_report, category_breakdown


class TestReports(unittest.TestCase):
    """
    Test cases for expense report generation
    """

    def setUp(self):
        """
        Sample expense data used for testing
        This runs before each test case
        """
        self.sample_expenses = [
            {
                "date": "2024-01-05",
                "amount": 1000,
                "category": "Food",
                "description": "Lunch"
            },
            {
                "date": "2024-01-15",
                "amount": 500,
                "category": "Travel",
                "description": "Bus fare"
            },
            {
                "date": "2024-02-10",
                "amount": 2000,
                "category": "Food",
                "description": "Dinner"
            }
        ]

    def test_monthly_report_january(self):
        """
        Test total expenses for January (01)
        """
        total = monthly_report(self.sample_expenses, "01")
        self.assertEqual(total, 1500)

    def test_monthly_report_february(self):
        """
        Test total expenses for February (02)
        """
        total = monthly_report(self.sample_expenses, "02")
        self.assertEqual(total, 2000)

    def test_category_breakdown(self):
        """
        Test category-wise expense calculation
        """
        breakdown = category_breakdown(self.sample_expenses)

        self.assertEqual(breakdown["Food"], 3000)
        self.assertEqual(breakdown["Travel"], 500)


if __name__ == "__main__":
    unittest.main()
