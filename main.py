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
full_name = input('Enter your name: ')
res = requests.get(f'https://jsonplaceholder.typicode.com/users/')
users = res.json()
counter = 0
for user in users:
    counter += 1
    if user["name"] == full_name:
        counter -= 1
        id = user["id"]
        name = user["name"]
        username = user["username"]
        email = user["email"]
        my_user = MyUser(id, name, username, email)
        print(f'The user was found: {my_user}')
    if counter == 10:
        print(f'User "{full_name}" is not found')



