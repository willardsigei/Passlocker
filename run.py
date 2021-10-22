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
