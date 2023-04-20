# Welcome to PhoneBook REST API

This is a REST API application that allows you to maintain a phonebook of names and phone numbers. You can store, retrieve, update, and delete information using this API.

#  API Endpoints

| API Endpoint | Description |  
| ----------- | ----------- |  
| GET /PhoneBook/list | This endpoint returns a list of all the contacts in the phonebook. |  
| POST /PhoneBook/add| This endpoint allows you to add a new person to the phonebook. You need to provide an object with the person's name and phone number as string elements in JSON format. |
| PUT /PhoneBook/deleteByName | This endpoint allows you to remove a person from the phonebook by name. You need to provide the person's name as a string element in JSON format. |  
| PUT /PhoneBook/deleteByNumber| This endpoint allows you to remove a person from the phonebook by phone number. You need to provide the person's phone number as a string element in JSON format. |
| GET /PhoneBook/logs|This endpoint allows you to view the audit log of the entire PhoneBook. |
|POST /PhoneBook/login|This endpoint allows you to login using credentials and generates token which is to be copied and pasted in the authorization tabs inside the token bearer option of it.

#  Getting Started

Clone the repository

`git clone https://github.com/Dishant8218/PhoneBook-REST-API` 

Change directory

`cd PhoneBook-REST-API` 

Build the docker-file

`docker build -t my-rest-api . ` 

Run the docker-file

`docker run -p 2000:5000 my-rest-api` 

Test if the setup has been completed by going to the browser and typing "localhost:2000"

`localhost:2000`
