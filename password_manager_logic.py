import json
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
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(key, encrypted_data):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

def save_passwords():
    key = load_key()
    decoded_passwords = {service: {'username': info['username'], 'password': decrypt_data(key, info['password'])} for service, info in passwords.items()}
    encrypted_data = encrypt_data(key, json.dumps(decoded_passwords))
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
    passwords[service] = {'username': username, 'password': encrypt_data(load_key(), password)}
    print(f"Password added for service {service}: {passwords[service]}")

def get_password(service):
    return decrypt_data(load_key(), passwords[service]['password'])

def delete_password(service):
    global passwords
    if service in passwords:
        del passwords[service]
    print(f"Password deleted for service {service}")
