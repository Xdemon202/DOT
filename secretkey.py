import os
import json
from cryptography.fernet import Fernet

# Функция для генерации и сохранения ключа
def generate_and_save_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# Функция для загрузки ключа
def load_key():
    return open('secret.key', 'rb').read()

# Проверка наличия файла ключа и генерация, если его нет
if not os.path.exists('secret.key'):
    generate_and_save_key()

# Теперь можно загрузить ключ
key = load_key()

# Функции для шифрования и дешифрования
def encrypt_data(key, data):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(key, data):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()

# Функции для работы с паролями
passwords = {}

def save_passwords():
    with open('passwords.enc', 'wb') as file:
        encrypted_data = encrypt_data(key, json.dumps(passwords))
        file.write(encrypted_data)

def load_passwords():
    global passwords
    try:
        with open('passwords.enc', 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = decrypt_data(key, encrypted_data)
            passwords = json.loads(decrypted_data)
    except FileNotFoundError:
        passwords = {}

def add_password(service, username, password):
    passwords[service] = {'username': username, 'password': encrypt_data(key, password)}

def get_password(service):
    if service in passwords:
        return decrypt_data(key, passwords[service]['password'])
    return None

def delete_password(service):
    if service in passwords:
        del passwords[service]

# Загружаем пароли при запуске программы
load_passwords()
