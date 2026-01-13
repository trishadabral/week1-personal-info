from library_system.book import Book

def test_book_checkout():
    book = Book("Test", "Author", "111")
    success, _ = book.check_out("M1")
    assert success
