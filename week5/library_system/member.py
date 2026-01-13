class Member:
    """
    Represents a library member
    """

    MAX_BORROW_LIMIT = 5

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < self.MAX_BORROW_LIMIT

    def borrow_book(self, isbn):
        if self.can_borrow():
            self.borrowed_books.append(isbn)
            return True
        return False

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data["name"], data["member_id"])
        member.borrowed_books = data["borrowed_books"]
        return member

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) | Books borrowed: {len(self.borrowed_books)}"
