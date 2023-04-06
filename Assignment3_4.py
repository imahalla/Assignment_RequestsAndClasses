# ---Assignment 3, 4
import requests

URL = 'https://jsonplaceholder.typicode.com/users'


class SpeedUser:
    def __init__(self, user):
        self.id = user['id']
        self.name = user['name']
        self.username = user['username']
        self.email = user['email']
        self.address = user['address']
        self.lat = self.get_lat()

    def __str__(self):
        return f'id: {self.id},\n name: {self.name},\n username: {self.username}' \
               f',\n email: {self.email},\n lat: {self.lat},\n'

    def get_lat(self):
        lat = self.address['geo']['lat']
        return lat


def lat_dict_by_user(users_list):
    user_latitude_dict = {}
    for i in range(len(users_list)):
        user1 = SpeedUser(users_list[i])
        user_latitude_dict.update({user1: float(user1.get_lat())})
    return user_latitude_dict


def who_is_closets(latitude_dict1, user_lat):
    difference_dict = {}
    for user, lat in latitude_dict1.items():
        difference_dict.update({abs(user_lat - lat): user})
        if user_lat == lat:
            return user
    closest = min(difference_dict.items(), key=lambda x: x[0])
    return closest[1]


def get_input():
    while True:
        user_lat = (input('Enter your latitude : '))
        if not user_lat.isalpha():
            return float(user_lat)


users_list = requests.get(URL).json()
user_lat = get_input()
latitude_dict = lat_dict_by_user(users_list)
closest_user = who_is_closets(latitude_dict, user_lat)
if float(closest_user.lat) == user_lat:
    print(f'The user:\n {closest_user} in your position:)')
else:
    print(f'The user:\n {closest_user} is closest to you:)')
