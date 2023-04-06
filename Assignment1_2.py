# -------Assignment 1, 2--------

import requests


# -----1-----
class MyUser:
    def __init__(self, id1, name1, username1, email1):
        self.id = id1
        self.name = name1
        self.username = username1
        self.email = email1

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, username: {self.username}, email: {self.email}'


# -----2-----
def get_user(users, full_name):
    for user in users:
        id = user["id"]
        name = user["name"]
        username = user["username"]
        email = user["email"]
        my_user = MyUser(id, name, username, email)
        if my_user.name == full_name:
            return my_user
    return None


full_name = input('Enter your name: ')
res = requests.get(f'https://jsonplaceholder.typicode.com/users/')
users = res.json()
my_user = get_user(users, full_name)

if my_user:
    print(f'The user was found: {my_user}')
else:
    print(f'User "{full_name}" is not found')

