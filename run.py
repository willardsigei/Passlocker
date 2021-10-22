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

class Credentials():
    credentials_list = []

    @classmethod
    def verify_user(cls,username, password):
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)
