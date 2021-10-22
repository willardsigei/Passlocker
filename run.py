#!/usr/bin/env python3.8
from users import User, Credentials
def create_new_user(username,password):
    new_user = User(username,password)
    return new_user

def save_user(user):
    user.save_user()

def show_user():
    return User.show_user()

def login_user(username,password):
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    credentials. save_details()
def show_accounts_details():
    return Credentials.show_credentials()

def delete_credential(credentials):
    credentials.delete_credentials()

def find_credential(account):
    return Credentials.find_credential(account)

def check_credendtials(account):
    return Credentials.if_credential_exist(account)

def generate_Password():
    auto_password=Credentials.generatePassword()
    return auto_password

def copy_password(account):
    return Credentials.copy_password(account)

def userlocker():
    print("Welcome.\n Please choose one to proceed.\n SU ---  Sign up  \n LI ---  Login  \n")
    short_code=input("").lower().strip()
    if short_code == "SU":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" CP - Create Password:\n GP - Generate Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'CP':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'GP':
                password = generate_Password()
                break
            else:
                print("Invalid!")
        save_user(create_new_user(username,password))
        print("*"*70)
        print(f"Hello {username}, Succesfully Created! Your password is: {password}")
        print("*"*70)

    elif short_code == "li":
        print("*"*42)
        print("Enter your Username and Password:")
        print('*' * 40)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassLocker")  
            print('\n')
    while True:
        print("Below are the prefixes you can use:\n CC - Create new credential \n SC - Show Credentials \n FC - Find credential \n GP - Generate Password \n DC - Delete credential \n Exit - Close\n")
