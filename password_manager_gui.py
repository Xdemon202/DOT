import tkinter as tk
from tkinter import messagebox
from password_manager_logic import add_password, get_password, delete_password, load_passwords

def add_password_gui():
    service = service_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if service and username and password:
        add_password(service, username, password)
        messagebox.showinfo("Success", "Password added successfully")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def get_password_gui():
    service = service_entry.get().strip()

    if service:
        password = get_password(service)
        if password:
            messagebox.showinfo("Password", f"Password for {service}: {password}")
        else:
            messagebox.showerror("Error", "Service not found")
    else:
        messagebox.showerror("Error", "Please enter a service name")

def delete_password_gui():
    service = service_entry.get().strip()

    if service:
        delete_password(service)
        messagebox.showinfo("Success", "Password deleted successfully")
    else:
        messagebox.showerror("Error", "Please enter a service name")

# Initialize GUI components here
load_passwords()

instructions = '''To add a password, fill in the details and click "Add Password".
To view a password, enter the account name and click "Get Password".
To delete a password, enter the account name and click "Delete Password".'''

signature = "Developed by Dmitrii Khadzhiev"

BACKGROUND_COLOR = "white"
FRAME_COLOR = "#d3d3d3"

window = tk.Tk()
window.title("Password Manager")
window.configure(bg=BACKGROUND_COLOR)
window.resizable(False, False)

center_frame = tk.Frame(window, bg=FRAME_COLOR)
center_frame.grid(row=0, column=0, padx=10, pady=10)

instruction_label = tk.Label(center_frame, text=instructions, bg=FRAME_COLOR)
instruction_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

service_label = tk.Label(center_frame, text="Account:", bg=FRAME_COLOR)
service_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
service_entry = tk.Entry(center_frame)
service_entry.grid(row=1, column=1, padx=10, pady=5)

username_label = tk.Label(center_frame, text="Username:", bg=FRAME_COLOR)
username_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(center_frame)
username_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(center_frame, text="Password:", bg=FRAME_COLOR)
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(center_frame, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

add_button = tk.Button(center_frame, text="Add Password", command=add_password_gui, height=1, width=15)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

get_button = tk.Button(center_frame, text="Get Password", command=get_password_gui, height=1, width=15)
get_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

delete_button = tk.Button(center_frame, text="Delete Password", command=delete_password_gui, height=1, width=15)
delete_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

signature_label = tk.Label(center_frame, text=signature, bg=FRAME_COLOR)
signature_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
