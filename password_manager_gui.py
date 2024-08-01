import tkinter as tk
from tkinter import messagebox
from password_manager_logic import PasswordManager

class PasswordManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("400x400")

        self.password_manager = PasswordManager()

        self.instructions = '''To add a password, fill in the details and click "Add Password".
To view a password, enter the account name and click "Get Password".
To delete a password, enter the account name and click "Delete Password".'''

        self.label_instructions = tk.Label(master, text=self.instructions, wraplength=350)
        self.label_instructions.pack()

        self.label_service = tk.Label(master, text="Service")
        self.label_service.pack()

        self.entry_service = tk.Entry(master)
        self.entry_service.pack()

        self.label_username = tk.Label(master, text="Username")
        self.label_username.pack()

        self.entry_username = tk.Entry(master)
        self.entry_username.pack()

        self.label_password = tk.Label(master, text="Password")
        self.label_password.pack()

        self.entry_password = tk.Entry(master)
        self.entry_password.pack()

        self.add_button = tk.Button(master, text="Add Password", command=self.add_password)
        self.add_button.pack()

        self.get_button = tk.Button(master, text="Get Password", command=self.get_password)
        self.get_button.pack()

        self.delete_button = tk.Button(master, text="Delete Password", command=self.delete_password)
        self.delete_button.pack()

        self.signature = tk.Label(master, text="Developed by Dmitrii Khadzhiev", fg="grey")
        self.signature.pack(side="bottom")

    def add_password(self):
        service = self.entry_service.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        if service and username and password:
            self.password_manager.add_password(service, username, password)
            messagebox.showinfo("Success", "Password added successfully")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def get_password(self):
        service = self.entry_service.get()

        if service:
            password = self.password_manager.get_password(service)
            if password:
                messagebox.showinfo("Password", f"Password for {service}: {password}")
            else:
                messagebox.showerror("Error", "No password found for this service")
        else:
            messagebox.showerror("Error", "Please enter a service name")

    def delete_password(self):
        service = self.entry_service.get()

        if service:
            success = self.password_manager.delete_password(service)
            if success:
                messagebox.showinfo("Success", f"Password for {service} deleted successfully")
            else:
                messagebox.showerror("Error", "No password found for this service")
        else:
            messagebox.showerror("Error", "Please enter a service name")

if __name__ == "__main__":
    root = tk.Tk()
    gui = PasswordManagerGUI(root)
    root.mainloop()
