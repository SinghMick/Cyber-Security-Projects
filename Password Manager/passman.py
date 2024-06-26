# This Python script implements a simple password manager using hashlib for password hashing and getpass for securely entering passwords. It allows users to create an account with a username and password, and then login with the same credentials. The passwords are stored in a dictionary with hashed values for security.

import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password")

def main():
    while True:
        user_choice = input("Enter 1 to create password, 2 to login, 3 to exit: ")
        if user_choice == "1":
            create_account()
        elif user_choice == "2":
            login()
        elif user_choice == "3":
            break
        else:
            print("Invalid entry, only accepted entries are 1, 2, 3")

if __name__ == "__main__":
    main()