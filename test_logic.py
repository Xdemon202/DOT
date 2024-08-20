import unittest

class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        # Initialize a simple password manager as a dictionary
        self.passwords = {}

    def test_add_password(self):
        # Test adding a password
        service = "email"
        self.passwords[service] = {
            'username': 'user@example.com',
            'password': 'pass123'
        }
        self.assertIn(service, self.passwords)
        self.assertEqual(self.passwords[service]['username'], 'user@example.com')
        self.assertEqual(self.passwords[service]['password'], 'pass123')

    def test_retrieve_password(self):
        # Test retrieving a password
        service = "email"
        self.passwords[service] = {
            'username': 'user@example.com',
            'password': 'pass123'
        }
        retrieved_password = self.passwords.get(service)
        self.assertIsNotNone(retrieved_password)
        self.assertEqual(retrieved_password['username'], 'user@example.com')
        self.assertEqual(retrieved_password['password'], 'pass123')

    def test_update_password(self):
        # Test updating an existing password
        service = "email"
        self.passwords[service] = {
            'username': 'user@example.com',
            'password': 'pass123'
        }
        # Update the password
        self.passwords[service]['password'] = 'newpass456'
        self.assertEqual(self.passwords[service]['password'], 'newpass456')

    def test_delete_password(self):
        # Test deleting a password
        service = "email"
        self.passwords[service] = {
            'username': 'user@example.com',
            'password': 'pass123'
        }
        del self.passwords[service]
        self.assertNotIn(service, self.passwords)

    def test_password_exists(self):
        # Test checking if a password exists for a service
        service = "email"
        self.passwords[service] = {
            'username': 'user@example.com',
            'password': 'pass123'
        }
        self.assertTrue(service in self.passwords)
        self.assertFalse('nonexistent_service' in self.passwords)

if __name__ == '__main__':
    unittest.main()
