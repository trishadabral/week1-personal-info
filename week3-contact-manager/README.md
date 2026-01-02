# 📇 Contact Management System  
*A Python project demonstrating Functions & Dictionaries (Week 3)*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Build](https://img.shields.io/badge/Build-Passing-success.svg)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

---

## 📚 Overview
This project is part of **Week 3: Functions & Dictionaries** coursework.  
It demonstrates how to build a **Contact Management System** using Python concepts:

- **Functions**: Creating reusable blocks of code with `def`  
- **Function Parameters**: Passing data into functions (positional, keyword, default)  
- **Return Values**: Getting results back from functions  
- **Dictionaries**: Key‑value pairs for organized data storage  
- **String Methods**: Advanced string manipulation (`strip()`, `lower()`, `split()`)  
- **Scope**: Understanding local vs global variables  
- **Built‑in Functions**: Leveraging Python’s powerful built‑in functions (`len()`, `print()`, `input()`)  
- **File Operations**: JSON persistence & CSV export  

---

## ✨ Features
- **Add contacts** with validation (name, phone, email)  
- **Search contacts** (partial match by name or phone)  
- **Update contacts** with overwrite confirmation  
- **Delete contacts** safely with confirmation  
- **Display all contacts** in a formatted view  
- **Export contacts to CSV** for external use  
- **View statistics** (total contacts, groups, recent updates)  
- **Data persistence** using JSON file  

---

## 📂 Project Structure
week3-contact-manager/
│--contacts_manager.py      # Main program with all functions & menu
│-- contacts_data.json       # Data persistence file (auto-created)
│-- test_contacts.py         # Unit tests for validation & CRUD functions
│-- README.md                 # Documentation & usage guide
│-- requirements.txt           # Dependencies (standard libraries only)
└── .gitignore               # Ignore unnecessary files

---

## ⚙️ Installation & Setup
Clone the repository and run the program:

```bash
git clone https://github.com/trishadabral/week1-personal-info/tree/main/week3-contact-manager
cd week3-contact-manager
python contacts_manager.py
