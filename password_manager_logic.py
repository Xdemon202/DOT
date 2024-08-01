import json
import os
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, file_path="passwords.json"):
        self.file_path = file_path
        self.key_path = "secret.key"
        self.key = self.load_key()
        self.cipher = Fernet(self.key)
        self.passwords = self.load_passwords()

    def load_key(self):
        if not os.path.exists(self.key_path):
            self.generate_key()
        with open(self.key_path, "rb") as key_file:
            return key_file.read()

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_path, "wb") as key_file:
            key_file.write(key)

    def load_passwords(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as file:
                encrypted_data = file.read()
                decrypted_data = self.cipher.decrypt(encrypted_data)
                return json.loads(decrypted_data)
        return {}

    def save_passwords(self):
        encrypted_data = self.cipher.encrypt(json.dumps(self.passwords).encode())
        with open(self.file_path, "wb") as file:
            file.write(encrypted_data)

    def add_password(self, service, username, password):
        self.passwords[service] = {"username": username, "password": password}
        self.save_passwords()

    def get_password(self, service):
        if service in self.passwords:
            return self.passwords[service]["password"]
        return None

    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
            return True
        return False
