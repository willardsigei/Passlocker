import random
import string
import pyperclip
class User:
    user_list = []

    @classmethod
    def show_user(cls):
        return cls.user_list

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

