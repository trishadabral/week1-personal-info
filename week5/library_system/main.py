from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

library = Library()
library.load_data()

while True:
    print("\n================================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add New Book")
    print("2. Register New Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. View All Books")
    print("7. View All Members")
    print("8. View Overdue Books")
    print("9. Save & Exit")
    print("0. Exit Without Saving")

    choice = input("Enter your choice: ")

    # 1. Add New Book
    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        year = input("Year: ")
        library.add_book(Book(title, author, isbn, year))
        print("Book added successfully")

    # 2. Register New Member
    elif choice == "2":
        name = input("Member Name: ")
        member_id = input("Member ID: ")
        library.register_member(Member(name, member_id))
        print("Member registered successfully")

    # 3. Borrow Book
    elif choice == "3":
        member_id = input("Member ID: ")
        isbn = input("Book ISBN: ")
        print(library.borrow_book(member_id, isbn))

    # 4. Return Book
    elif choice == "4":
        member_id = input("Member ID: ")
        isbn = input("Book ISBN: ")
        print(library.return_book(member_id, isbn))

    # 5. Search Books
    elif choice == "5":
        keyword = input("Enter title / author / ISBN: ")
        results = library.search_books(keyword)
        if not results:
            print("No books found")
        else:
            for book in results:
                print(book)

    # 6. View All Books
    elif choice == "6":
        for book in library.view_all_books():
            print(book)

    # 7. View All Members
    elif choice == "7":
        for member in library.view_all_members():
            print(member)

    # 8. View Overdue Books
    elif choice == "8":
        overdue_books = library.view_overdue_books()
        if not overdue_books:
            print("No overdue books")
        else:
            for book in overdue_books:
                print(f"{book} | Due Date: {book.due_date}")

    # 9. Save & Exit
    elif choice == "9":
        library.save_data()
        print("Data saved successfully. Exiting...")
        break

    # 0. Exit Without Saving
    elif choice == "0":
        print("Exiting without saving...")
        break

    else:
        print("Invalid choice. Please try again.")
