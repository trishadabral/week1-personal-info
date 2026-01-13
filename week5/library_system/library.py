import json
import os
from library_system.book import Book
from library_system.member import Member
from datetime import datetime

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ---------- BOOK & MEMBER MANAGEMENT ----------

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def find_member(self, member_id):
        return self.members.get(member_id)

    def find_book(self, isbn):
        return self.books.get(isbn)

    # ---------- BORROW & RETURN ----------

    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return "Invalid member ID or ISBN"

        if not member.can_borrow():
            return "Borrow limit reached (Max 5 books)"

        success, message = book.check_out(member_id)
        if success:
            member.borrow_book(isbn)
        return message

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return "Invalid return request"

        book.return_book()
        member.return_book(isbn)
        return "Book returned successfully"

    # ---------- SEARCH & DISPLAY ----------

    def search_books(self, keyword):
        keyword = keyword.lower()
        return [
            book for book in self.books.values()
            if keyword in book.title.lower()
            or keyword in book.author.lower()
            or keyword == book.isbn
        ]

    def view_all_books(self):
        return list(self.books.values())

    def view_all_members(self):
        return list(self.members.values())

    def view_overdue_books(self):
        return [book for book in self.books.values() if book.is_overdue()]

    # ---------- FILE HANDLING ----------

    def save_data(self):
        os.makedirs("data", exist_ok=True)

        with open("data/books.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.books.items()}, f, indent=4)

        with open("data/members.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.members.items()}, f, indent=4)

    def load_data(self):
        if os.path.exists("data/books.json"):
            with open("data/books.json") as f:
                data = json.load(f)
                self.books = {k: Book.from_dict(v) for k, v in data.items()}

        if os.path.exists("data/members.json"):
            with open("data/members.json") as f:
                data = json.load(f)
                self.members = {k: Member.from_dict(v) for k, v in data.items()}
