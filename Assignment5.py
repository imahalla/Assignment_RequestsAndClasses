# ---Assignment 5 ---
import requests

URL = 'https://randomuser.me/api/'


def extract_first_name():
    response = requests.get(URL).json()
    first_name = response['results'][0]['name']['first']
    return first_name


number = 1


def check_input_and_print_results(number):
    if number > 0:
        for i in range(number):
            name = extract_first_name()
            print(name)
    elif number == -1:
        print('Bye Bye')
    else:
        print("invalid entry, enter number greater then 0!!!")


while number != -1:
    number = int(input('Enter number between 1 - 100, to quit enter -1 :'))
    check_input_and_print_results(number)

