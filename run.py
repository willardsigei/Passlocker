#!/usr/bin/env python3.8
from users import User, Credentials
def create_new_user(username,password):
    new_user = User(username,password)
    return new_user

def save_user(user):
    user.save_user()

def show_user():
    return User.show_user()
