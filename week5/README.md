# 📚 Library Management System (OOP Based)

A fully functional **Library Management System** built using **Python and Object-Oriented Programming (OOP)** principles.  
This project simulates real-world library operations such as book borrowing, returns, member management, searching, and data persistence.

---

## 🎯 Objectives
- Apply OOP concepts in a real-world scenario
- Understand class relationships and data management
- Implement file handling using JSON
- Build a menu-driven console application

---

## 🛠️ Technologies Used
- Python 3
- Object-Oriented Programming
- JSON File Handling
- PyTest (for testing)

---

## 📂 Project Structure
week5-library-system/
│── library_system/
│ ├── book.py # Book class
│ ├── member.py # Member class
│ ├── library.py # Library manager class
│ └── main.py # User interface
│── data/
│ ├── books.json # Stored book data
│ └── members.json # Stored member data
│── tests/
│ ├── test_book.py
│ ├── test_member.py
│ └── test_library.py


---

## 🧩 OOP Concepts Used
| Concept | Usage |
|------|------|
| Class & Object | Book, Member, Library |
| Encapsulation | Data + methods inside classes |
| Abstraction | Library controls all operations |
| Composition | Library contains Books & Members |

---

## 📘 Class Overview

### Book Class
- Stores book details
- Tracks availability and due date
- Handles checkout & return logic

### Member Class
- Stores member details
- Tracks borrowed books
- Enforces borrowing limit

### Library Class
- Central controller
- Manages books & members
- Handles borrowing, returning, searching, saving data

---

## 🔍 Features
- Add & search books
- Register members
- Borrow & return books
- Due date tracking
- Persistent storage using JSON
- Menu-driven interface
- Unit tests included

---

## ▶️ How to Run
```bash
python library_system/main.py
