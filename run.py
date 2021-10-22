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
