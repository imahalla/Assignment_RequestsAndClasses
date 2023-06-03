# Assignment_RequestsAndClasses

**1,2**

Class: MyUser
Create a class called MyUser with an __init__ function that accepts the following parameters: id, email, username, and name.
Write a __str__ function that prints the fields of the class.

Retrieving Users
To retrieve user data, use the following API endpoint:

URL: https://jsonplaceholder.typicode.com/users
Code for User Search
Write code that prompts the user to enter a username.
Then, iterate through all the users obtained from the above API endpoint until a user with a matching username is found.
If such a user is not found, return the message: "User not found." Each time you access a user from the API, create an object for that user.

**2,3**

Class: SpeedUser
Create a class called SpeedUser with a constructor and __str__ function that utilize the
JSON response values from the following API endpoint:

URL: https://jsonplaceholder.typicode.com/users
Code for Latitude Search
Write code that prompts the user to enter their latitude (displayed as "lat"). 
Then, iterate through all the users obtained from the above API endpoint until a user with a matching latitude is found. 
If an exact latitude match is not found, return the user with the closest latitude (hint: create a list of differences). 
Each time you access a user from the API, create an object of type SpeedUser.

**5**

Accessing Random Users
Using the REST address of the randomuser server: https://randomuser.me/api/, prompt the user for a positive number less than 100.
Send a GET request to the randomuser server for the number of times requested by the user, 
and for each request, print the name of the user received from the site. For example, 
if the user enters 50, print the names of 50 different users received. Note that with each REST GET request to the site, 
you will receive details of a random user.
