# DOT
repository for subject  devops tools


**Password Manager**

This project offers a secure and user-friendly application to manage your passwords.

**Features:**

- **Add Passwords:** Store your login credentials for various services with ease.
- **Retrieve Passwords:** Access your saved passwords anytime you need them.
- **Delete Passwords:** Remove outdated entries from your password vault.
- **Update Passwords:** Keep your credentials up-to-date for optimal security.
- **Search Passwords:** Find specific entries quickly using service names.

**Getting Started**

**Prerequisites:**

- **Python 3.x:** Download and install it from [python.org](https://www.python.org/).
- **pip:** Python's package installer (usually included with Python, but you can install it separately if needed).

**Installation:**

1. **Clone the Repository:**

git clone <https://github.com/username/repository.git>

cd repository

Use code with caution.

1. **Make the Build Script Executable:**

chmod +x build.sh

Use code with caution.

1. **Install Dependencies:**

./build.sh install

Use code with caution.

**Optional Steps:**

- **Run Tests:** Verify the application's functionality with ./build.sh test.
- **Create Deployable Package:** Generate a distributable archive with ./build.sh package.

**Running the Application:**

1. **(Optional) Run all steps (dependencies, tests, package) at once:**

./build.sh all

Use code with caution.

This will create a deployable package named password_manager.zip in the project directory.

1. **Run the Password Manager:**

python3 password_manager_gui.py

Use code with caution.

**Using the Application:**

The intuitive GUI provides clear options for managing your passwords:

- **Add Password:** Enter service name, username, and password, then click "Add".
- **Retrieve Password:** Enter the service name and click "Retrieve".
- **Delete Password:** Enter the service name and click "Delete".
- **Update Password:** Enter the service name, new username, and password, then click "Update".
- **Search Password:** Enter the service name and click "Search".

**Build Automation (Optional)**

The build.sh script automates tasks like installing dependencies, running tests, and creating a deployable package. Refer to the script for specific commands.
