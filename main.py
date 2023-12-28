import random
import hashlib
import pyperclip
import sys
import csv
from cryptography.fernet import Fernet
from getpass import getpass
import os

CONFIG_FILE_PATH = ".pm2.config"
key_file_path = "secret.key"

# Check if a key file exists or nnot
try:
    with open(key_file_path, "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    # If file doesn't exist, generate a new key
    key = Fernet.generate_key()

    # Save the key file
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)
crypto = Fernet(key)

def setup_master_password():
    master_password = getpass("Set up your master password: ")
    master_password_hash = hashlib.sha256(master_password.encode('utf-8')).hexdigest()

    # Store the hash in the configuration file
    with open(CONFIG_FILE_PATH, "w") as config_file:
        config_file.write(master_password_hash)

    print("  Master password set up successfully.")
    print("----------------------------------------")

def get_stored_master_password_hash():
    # Read hash from the configuration file
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, "r") as config_file:
            return config_file.read().strip()
    return None

def check_master_password(entered_password_hash):
    # checkinng hash
    stored_master_password_hash = get_stored_master_password_hash()
    return entered_password_hash == stored_master_password_hash

def generate_pass():
    length = int(input('''Enter the length of your password (RECOMMENDED[9-16])
    (Default[11] : ''') or "11")
    possible = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890;/<>?:\"/\\!@#$%^*()_+-=")

    def generate(length):
        global password
        password = ""
        for i in range(length):
            password += random.choice(possible)
        print("Your Generated password is : " + password)
        return password

    password = generate(length)
    choice_fun(password)

def save_and_copy(FOR_hash_password, site_name, note=""):
    # To Encrypt
    encrp_pass = crypto.encrypt(password.encode('utf-8'))
    hash_password = str(encrp_pass, 'utf-8')

    # Storing password in CSV file
    with open("passwords.csv", mode='a', newline='') as csv_file:
        fieldnames = ['Site Name', 'Password', 'Note']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Check if the file is empty and write headers
        if csv_file.tell() == 0:
            writer.writeheader()

        # Write the data
        writer.writerow({'Site Name': site_name, 'Password': hash_password, 'Note': note})

    print("Password saved and copied to clipboard for site:", site_name)
    pyperclip.copy(password)
    sys.exit()

def choice_fun(password):
    print("************ [ Next Step ] ************")
    choice = int(input('''1). Copy AND Save
2). Regenerate
Enter Your Choice : '''))

    if choice == 1:
        site_name = input("Enter the site name: ")
        note = input("Enter an optional note (press Enter if none): ")
        save_and_copy(password, site_name, note)
    elif choice == 2:
        print("---------------------------------")
        print("Regenerating Your password....")
        password = generate_pass()
    else:
        print("Enter a valid choice")
        choice_fun(password)

def menu():
    choice = int(input('''1). Generate a new password :
2). View Saved Password
Enter Your Choice : '''))

    if choice == 1:
        generate_pass()
    elif choice == 2:
        # Call the function to view saved passwords
        view_saved_passwords()
    else:
        print("Enter a valid choice")

def view_saved_passwords():
    # Ask for the master password
    master_password_hash = hashlib.sha256(getpass("Enter Master Password: ").encode('utf-8')).hexdigest()

    # Check if the master password is correct
    if not check_master_password(master_password_hash):
        print("Incorrect master password. Exiting.")
        sys.exit()

    # Ask the user if they want to list all passwords or retrieve by site name/note
    print("1. List all passwords")
    print("2. Retrieve by site name or note")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        list_all_passwords(master_password_hash)
    elif choice == 2:
        site_name = input("Enter the site name to retrieve passwords (press Enter if none): ")
        note = input("Enter the note to retrieve passwords (press Enter if none): ")
        retrieve_passwords_by_info(master_password_hash, site_name, note)
    else:
        print("Invalid choice. Exiting.")
        sys.exit()

def list_all_passwords(master_password_hash):
    with open("passwords.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print("************ [ Saved Passwords ] ************")
        for row in csv_reader:
            # Decrypt the password
            encrp_pass = row['Password'].encode('utf-8')
            decrp_pass = crypto.decrypt(encrp_pass).decode('utf-8')

            # Print the information
            print("Site Name:", row['Site Name'])
            print("Password:", decrp_pass)
            print("Note:", row['Note'])
            print("-------------------------------------------")

def retrieve_passwords_by_info(master_password_hash, site_name, note):
    with open("passwords.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print("************ [ Retrieved Passwords ] ************")
        for row in csv_reader:
            # Check if site name or note matches, and the master password is correct
            if (row['Site Name'] == site_name or row['Note'] == note) and check_master_password(master_password_hash):
                # Decrypt the password
                encrp_pass = row['Password'].encode('utf-8')
                decrp_pass = crypto.decrypt(encrp_pass).decode('utf-8')

                # Print the information
                print("Site Name:", row['Site Name'])
                print("Password:", decrp_pass)
                print("Note:", row['Note'])
                print("-------------------------------------------")

# Check if the master password is set up
if not os.path.exists(CONFIG_FILE_PATH):
    setup_master_password()

# Call Menu Function
menu()
