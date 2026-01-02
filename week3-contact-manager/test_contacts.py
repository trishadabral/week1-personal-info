import unittest
import os
import json
from contacts_manager import validate_phone, validate_email, add_contact, search_contacts

class TestContactManager(unittest.TestCase):

    def setUp(self):
        """Setup a sample contacts dictionary before each test"""
        self.contacts = {
            "Alice": {"phone": "1234567890", "email": "alice@example.com", "address": "Street 1", "group": "Friends"}
        }

    def test_validate_phone_valid(self):
        is_valid, digits = validate_phone("+1 (234) 567-8900")
        self.assertTrue(is_valid)
        self.assertEqual(digits, "12345678900")

    def test_validate_phone_invalid(self):
        is_valid, digits = validate_phone("abc123")
        self.assertFalse(is_valid)
        self.assertIsNone(digits)

    def test_validate_email_valid(self):
        self.assertTrue(validate_email("test@example.com"))

    def test_validate_email_invalid(self):
        self.assertFalse(validate_email("invalid-email"))

    def test_add_contact(self):
        # Simulate adding a new contact
        self.contacts = add_contact(self.contacts)
        self.assertTrue(len(self.contacts) >= 1)

    def test_search_contacts(self):
        results = search_contacts(self.contacts, "Alice")
        self.assertIn("Alice", results)

if __name__ == "__main__":
    unittest.main()
