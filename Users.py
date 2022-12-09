import hashlib
from typing import List
from dataclasses import dataclass
users=[]


def hash_password(password: str):
     return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()

class User:
    username: str
    __password: str
    def __init__(self, username: str):
        self.username = username
    def set_password(self, password: str):
        self.__password = hash_password(password)
    def check_password(self, password: str)->bool:
        return self.__password == hash_password(password)
    def __repr__(self):
        return self.username

def create_user(username: str, password: str)-> User:
    user= User(username=username)
    user.set_password(password=password)
    users.append(user)
    return user

def get_user(username:str, password:str)-> User|None:
    user= next((u for u in users if username== u.username and u.check_password(password)), None)
    if not user:
        print('User not found')
        return
    return user

Surname,Name,password=input('Create User:').split(' ')
username=Surname+" "+Name
user=create_user(username=username, password=password)
print(user)

Surname,Name,password=input('Please enter your creds:').split(' ')
username1=Surname+" "+Name
print(get_user(username=username1,password=password))