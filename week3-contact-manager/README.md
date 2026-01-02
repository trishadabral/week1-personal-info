# Contact Management System
Week 3 Project – Functions & Dictionaries

## 📚 Overview
This project demonstrates Python concepts from Week 3:
- Functions
- Dictionaries
- String Methods
- Scope (local vs global variables)
- Built-in Functions
- File Operations (JSON, CSV)

It is a **Contact Management System** that allows users to add, search, update, delete, and display contacts with proper validation and persistence.

---

## ✨ Features
- Add contacts with validation (name, phone, email)
- Search contacts (partial match by name or phone)
- Update existing contacts
- Delete contacts with confirmation
- Display all contacts in formatted view
- Export contacts to CSV
- View statistics (total contacts, groups, recent updates)
- Data persistence using JSON file

---

## 📂 Project Structure
week3-contact-manager/
│── contacts_manager.py      # Main program
│── contacts_data.json       # Data persistence file
│── test_contacts.py         # Unit tests
│── README.md                 # Documentation
│── requirements.txt          # Dependencies
└── .gitignore               # Ignore unnecessary files

---

## ⚙️ Installation & Setup
Clone the repository and run the program:

```bash
git clone https://github.com/yourusername/week3-contact-manager.git
cd week3-contact-manager
python contacts_manager.py
==============================
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
==============================
--- ADD NEW CONTACT ---
Enter contact name: John Doe
Enter phone number: +1 (234) 567-8900
Enter email (optional): john@example.com
Enter address (optional): 123 Main Street
Enter group (Friends/Work/Family/Other): Friends
✅ Contact 'John Doe' added successfully!
## Testing
Run unit tests with:

bash
python -m unittest test_contacts.py
Test Coverage
Phone/email validation

Add/search/update/delete contacts

File save/load operations

Edge cases (duplicate names, invalid phone numbers, empty input)