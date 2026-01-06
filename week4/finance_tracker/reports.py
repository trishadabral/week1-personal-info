"""
reports.py
Generates reports and statistics
"""

from collections import defaultdict


def monthly_report(expenses, month):
    """
    Calculates total expense for a given month (MM)
    """
    total = 0
    for expense in expenses:
        if expense["date"][5:7] == month:
            total += expense["amount"]
    return total


def category_breakdown(expenses):
    """
    Returns category-wise expense summary
    """
    summary = defaultdict(float)

    for expense in expenses:
        summary[expense["category"]] += expense["amount"]

    return summary
