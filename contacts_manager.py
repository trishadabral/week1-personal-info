# Contact Management System
# Week 3 Project - Functions & Dictionaries

import json
import re
from datetime import datetime
import csv
import os

CONTACTS_FILE = "contacts_data.json"

# ------------------ VALIDATION ------------------

def validate_phone(phone):
    """Validate phone number format"""
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# ------------------ FILE OPERATIONS ------------------

def save_to_file(contacts):
    """Save contacts to JSON file"""
    try:
        with open(CONTACTS_FILE, "w") as f:
            json.dump(contacts, f, indent=4)
        print("✅ Contacts saved to contacts_data.json")
    except Exception as e:
        print(f"❌ Error saving contacts: {e}")

def load_from_file():
    """Load contacts from JSON file"""
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            print("❌ Error loading contacts file. Starting fresh.")
            return {}
    else:
        print("✅ No existing contacts file found. Starting fresh.")
        return {}

# ------------------ CRUD FUNCTIONS ------------------

def add_contact(contacts):
    """Add a new contact"""
    print("\n--- ADD NEW CONTACT ---")
    while True:
        name = input("Enter contact name: ").strip()
        if name:
            if name in contacts:
                print(f"Contact '{name}' already exists!")
                choice = input("Do you want to update instead? (y/n): ").lower()
                if choice == 'y':
                    update_contact(contacts, name)
                    return
            break
        print("Name cannot be empty!")

    while True:
        phone = input("Enter phone number: ").strip()
        is_valid, cleaned_phone = validate_phone(phone)
        if is_valid:
            break
        print("Invalid phone number! Please enter 10-15 digits.")

    while True:
        email = input("Enter email (optional, press Enter to skip): ").strip()
        if not email or validate_email(email):
            break
        print("Invalid email format!")

    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Work/Family/Other): ").strip() or "Other"

    contacts[name] = {
        'phone': cleaned_phone,
        'email': email if email else None,
        'address': address if address else None,
        'group': group,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }

    print(f"✅ Contact '{name}' added successfully!")
    save_to_file(contacts)

def search_contacts(contacts, search_term):
    """Search contacts by name (partial match)"""
    search_term = search_term.lower()
    results = {name: info for name, info in contacts.items() if search_term in name.lower()}
    return results

def update_contact(contacts, name=None):
    """Update an existing contact"""
    print("\n--- UPDATE CONTACT ---")
    if not name:
        name = input("Enter contact name to update: ").strip()
    if name not in contacts:
        print("❌ Contact not found.")
        return

    contact = contacts[name]
    print(f"Updating '{name}'... Leave blank to keep current value.")

    phone = input(f"Enter new phone [{contact['phone']}]: ").strip()
    if phone:
        is_valid, cleaned_phone = validate_phone(phone)
        if is_valid:
            contact['phone'] = cleaned_phone
        else:
            print("Invalid phone number. Keeping old value.")

    email = input(f"Enter new email [{contact['email']}]: ").strip()
    if email:
        if validate_email(email):
            contact['email'] = email
        else:
            print("Invalid email format. Keeping old value.")

    address = input(f"Enter new address [{contact['address']}]: ").strip()
    if address:
        contact['address'] = address

    group = input(f"Enter new group [{contact['group']}]: ").strip()
    if group:
        contact['group'] = group

    contact['updated_at'] = datetime.now().isoformat()
    contacts[name] = contact
    print(f"✅ Contact '{name}' updated successfully!")
    save_to_file(contacts)

def delete_contact(contacts):
    """Delete a contact"""
    print("\n--- DELETE CONTACT ---")
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
        if confirm == 'y':
            del contacts[name]
            print(f"✅ Contact '{name}' deleted successfully!")
            save_to_file(contacts)
    else:
        print("❌ Contact not found.")

def display_all(contacts):
    """Display all contacts"""
    print(f"\n--- ALL CONTACTS ({len(contacts)} total) ---")
    print("=" * 60)
    for name, info in contacts.items():
        print(f"👤 {name}")
        print(f"   📞 {info['phone']}")
        if info['email']:
            print(f"   📧 {info['email']}")
        if info['address']:
            print(f"   📍 {info['address']}")
        print(f"   👥 {info['group']}")
        print("-" * 40)

def export_to_csv(contacts):
    """Export contacts to CSV"""
    filename = "contacts_export.csv"
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "Email", "Address", "Group", "Created At", "Updated At"])
            for name, info in contacts.items():
                writer.writerow([name, info['phone'], info['email'], info['address'], info['group'], info['created_at'], info['updated_at']])
        print(f"✅ Contacts exported to {filename}")
    except Exception as e:
        print(f"❌ Error exporting contacts: {e}")

def view_statistics(contacts):
    """View statistics"""
    print("\n--- CONTACT STATISTICS ---")
    print(f"Total Contacts: {len(contacts)}\n")

    groups = {}
    for info in contacts.values():
        groups[info['group']] = groups.get(info['group'], 0) + 1

    print("Contacts by Group:")
    for group, count in groups.items():
        print(f"  {group}: {count} contact(s)")

    recent = [name for name, info in contacts.items() if (datetime.now() - datetime.fromisoformat(info['updated_at'])).days <= 7]
    print(f"\nRecently Updated (last 7 days): {len(recent)}")

# ------------------ MENU SYSTEM ------------------

def main_menu():
    contacts = load_from_file()
    while True:
        print("\n==============================")
        print("          MAIN MENU")
        print("==============================")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")
        print("==============================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            term = input("Enter name to search: ").strip()
            results = search_contacts(contacts, term)
            if results:
                print(f"\nFound {len(results)} contact(s):")
                print("-" * 50)
                for i, (name, info) in enumerate(results.items(), 1):
                    print(f"{i}. {name}")
                    print(f"   📞 Phone: {info['phone']}")
                    if info['email']:
                        print(f"   📧 Email: {info['email']}")
                    if info['address']:
                        print(f"   📍 Address: {info['address']}")
                    print(f"   👥 Group: {info['group']}\n")
            else:
                print("No contacts found.")
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            display_all(contacts)
        elif choice == '6':
            export_to_csv(contacts)
        elif choice == '7':
            view_statistics(contacts)
        elif choice == '8':
            save_to_file(contacts)
            print("\n==================================================")
            print("Thank you for using Contact Management System!")
            print("==================================================")
            break
        else:
            print("❌ Invalid choice. Please enter 1-8.")

if __name__ == "__main__":
    main_menu()
