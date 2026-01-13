from datetime import datetime, timedelta

class Book:
    """
    Represents a single book in the library
    """

    def __init__(self, title, author, isbn, year=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def check_out(self, member_id, loan_period=14):
        if not self.available:
            return False, "Book is already borrowed"

        self.available = False
        self.borrowed_by = member_id
        self.due_date = (datetime.now() + timedelta(days=loan_period)).strftime("%Y-%m-%d")
        return True, f"Book borrowed successfully. Due date: {self.due_date}"

    def return_book(self):
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def is_overdue(self):
        if not self.available and self.due_date:
            return datetime.now() > datetime.strptime(self.due_date, "%Y-%m-%d")
        return False

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available,
            "borrowed_by": self.borrowed_by,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data["title"], data["author"], data["isbn"], data["year"])
        book.available = data["available"]
        book.borrowed_by = data["borrowed_by"]
        book.due_date = data["due_date"]
        return book

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrowed_by}"
        return f"{self.title} | {self.author} | {status}"
