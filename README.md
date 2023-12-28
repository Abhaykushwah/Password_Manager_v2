# Python Password Manager v2

This is a simple password manager written in Python that uses encryption to secure passwords. It allows users to generate, save, and retrieve passwords for different sites.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Setup Master Password](#setup-master-password)
  - [Generate a New Password](#generate-a-new-password)
  - [View Saved Passwords](#view-saved-passwords)
- [Demo](#demo)

## Features

- Password generation with customizable length.
- Secure storage of passwords using encryption.
- Ability to save passwords for different sites with optional notes.
- Master password protection for accessing saved passwords.

## Requirements

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - cryptography
  - pyperclip


## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Abhaykushwah/Password_Manager_v2.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Password_Manager_v2
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Setup Master Password

The master password is required to access and manage saved passwords. Run the program and follow the instructions to set up your master password.

```bash
python password_manager.py
```

## Generate a New Password

1. Choose option 1 from the menu to generate a new password.
2. Enter the desired length for your password.
3. The generated password will be displayed, and you can choose to save and copy it.

## View Saved Passwords

1. Choose option 2 from the menu to view saved passwords.
2. Enter your master password when prompted.
3. Choose whether to list all passwords or retrieve by site name/note.

## Demo
### Setup Master Password
```
PS C:\Abhay\Password Manager v2> python .\main.py
Set up your master password: 
  Master password set up successfully.
----------------------------------------

```
Note that Master password will not visible.
### Generate a New Password
```
1). Generate a new password :
2). View Saved Password
Enter Your Choice : 1
Enter the length of your password (RECOMMENDED[9-16])
    (Default[11] : 16

```
### Regenerate
```
Your Generated password is : b#Z#Xkx@!vz=:H2!
************ [ Next Step ] ************
1). Copy AND Save
2). Regenerate
Enter Your Choice : 2
```
### Next Step
```
---------------------------------
Regenerating Your password....
Enter the length of your password (RECOMMENDED[9-16])
    (Default[11] : 14
Your Generated password is : NN4s>OD^T\hK3+
************ [ Next Step ] ************
1). Copy AND Save
2). Regenerate
Enter Your Choice : 1
```
### Saving [Give details of site] 
```
Enter Your Choice : 1
Enter the site name: abhay.com
Enter an optional note (press Enter if none): my own site
Password saved and copied to clipboard for site: abhay.com
```
### Incorrect master password
```
PS C:\Abhay\Password Manager v2> python .\main.py
1). Generate a new password :
2). View Saved Password
Enter Your Choice : 2
Enter Master Password:
Incorrect master password. Exiting.

```

### View Saved password
```
Incorrect master password. Exiting.
PS C:\Abhay\Password Manager v2> python .\main.py
1). Generate a new password :
2). View Saved Password
Enter Your Choice : 2     
Enter Master Password:
1. List all passwords
2. Retrieve by site name or note
Enter your choice: 2
Enter the site name to retrieve passwords (press Enter if none): abhay.com
Enter the note to retrieve passwords (press Enter if none):
************ [ Retrieved Passwords ] ************
Site Name: abhay.com
Password: NN4s>OD^T\hK3+
Note: my own site
-------------------------------------------
```
