import json
import os
import unittest
from cryptography.fernet import Fernet

passwords = {}

def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_data(key, data):
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    return encrypted_data

def decrypt_data(key, encrypted_data):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

def save_passwords():
    key = load_key()
    decoded_passwords = {service: {'username': info['username'], 'password': decrypt_data(key, info['password'])} for service, info in passwords.items()}
    encrypted_data = encrypt_data(key, json.dumps(decoded_passwords).encode())
    with open('passwords.enc', 'wb') as file:
        file.write(encrypted_data)
    print("Passwords saved")

def load_passwords():
    global passwords
    key = load_key()
    with open('passwords.enc', 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = decrypt_data(key, encrypted_data)
    decoded_passwords = json.loads(decrypted_data)
    passwords = {service: {'username': info['username'], 'password': encrypt_data(key, info['password'])} for service, info in decoded_passwords.items()}
    print("Passwords loaded:", passwords)

def add_password(service, username, password):
    global passwords
    passwords[service] = {'username': username, 'password': encrypt_data(load_key(), password.encode())}
    print(f"Password added for service {service}: {passwords[service]}")

def get_password(service):
    return decrypt_data(load_key(), passwords[service]['password'])

def delete_password(service):
    global passwords
    if service in passwords:
        del passwords[service]
    print(f"Password deleted for service {service}")

class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        # Create temporary files for testing
        self.key_file = 'test_secret.key'
        self.password_file = 'test_passwords.enc'
        if os.path.exists(self.key_file):
            os.remove(self.key_file)
        if os.path.exists(self.password_file):
            os.remove(self.password_file)

    def tearDown(self):
        # Remove temporary files after tests
        if os.path.exists(self.key_file):
            os.remove(self.key_file)
        if os.path.exists(self.password_file):
            os.remove(self.password_file)

    def test_key_generation(self):
        key = generate_key()
        self.assertIsNotNone(key)

    def test_key_loading(self):
        generate_key()
        key = load_key()
        self.assertIsNotNone(key)

    def test_encryption_decryption(self):
        key = generate_key()
        data = b'test_data'
        encrypted = encrypt_data(key, data)
        decrypted = decrypt_data(key, encrypted)
        self.assertEqual(data, decrypted.encode())
    def test_password_storage_retrieval(self):
        service = 'test_service'
        username = 'test_user'
        password = 'test_password'

        add_password(service, username, password)
        save_passwords()
        load_passwords()

        stored_password = get_password(service)
        self.assertEqual(password, stored_password)

    def test_password_deletion(self):
        passwords = original_passwords.copy()  # Create a local copy of passwords
        service = 'test_service'
        add_password(service, 'test_user', 'test_password')
        delete_password(service)
        self.assertFalse(service in passwords)

if __name__ == '__main__':
    unittest.main()

