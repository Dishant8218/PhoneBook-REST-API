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

```
git clone https://github.com/Dishant8218/PhoneBook-REST-API
```

Change directory

```
cd PhoneBook-REST-API
``` 

Build the docker-file

```
docker build -t my-rest-api . 
```

Run the docker-file

```
docker run -p 2000:5000 my-rest-api
``` 

Test if the setup has been completed by going to the browser and typing "localhost:2000"

```
localhost:2000
```

#  Instructions to run all the methods on Postman


1.  Open Postman and click on the "Import" button in the top-left corner of the screen.
    
2.  In the "Import" dialog box, select "Paste Raw Text" and paste the JSON code provided.
    
3.  Click on the "Import" button to import the collection into Postman.
    
4.  Once the collection is imported, select it from the left-hand menu to view its contents.
    
5.  To test the "Login" method, expand the "Login" request and enter the username and password in the request body using JSON format:
```
{  
"username":  "myuser",  
"password":  "mypassword"  
}
```
6.  Click on the "Send" button to send the request to the server. After a successful login, a token will be generated.
    
7.  Copy the generated token and paste it in the "Authorization" tab for all the subsequent requests. Select the "Bearer Token" type from the dropdown and paste the copied token in the "Token" field.
    
8.  To test the "View List" method, expand the "View List" request and click on the "Send" button to send the request to the server.
    
9.  To test the "Add Contact" method, expand the "Add Contact" request, enter the contact details in the request body using JSON format:
  ```  
{  
"name":  "enter name here",
"phone_number":"enter phone number here"  
}
```
10.  Click on the "Send" button to send the request to the server.
    
11.  To test the "Delete by name" method, expand the "Delete by name" request, enter the name of the contact to delete in the request body using JSON format:
 ```   
{  
"name":  "enter name here"  
}
```
12.  Click on the "Send" button to send the request to the server.
    
13.  To test the "Delete by Phone Number" method, expand the "Delete by Phone Number" request, enter the phone number of the contact to delete in the request body using JSON format:
 ```   
{  
"phone_number":"enter phone number here"  
}
```
14.  Click on the "Send" button to send the request to the server.
    
15.  To test the "Audit Logs" method, expand the "Audit Logs" request and click on the "Send" button to send the request to the server.
    
That's it! You have successfully checked all the methods on Postman using this JSON code. Remember to use the generated token in the "Authorization" tab for all the subsequent requests, and to enter the request body details in JSON format as specified for each method.
