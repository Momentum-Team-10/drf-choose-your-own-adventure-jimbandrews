# DRF Library API

This project uses Django Rest Framework to run an API that keeps track of books that you and other users want to read, are reading, and have finished.

<br>
<br>

# Local Installation

## Prerequisites
* Python 3.10.0
* PostgreSQL
* Pipenv

## Instructions
NOTE: This is specific to macOS.
* In PostgreSQL, create a new database (to make this easy to track, create a new user first and use the same name for the user and database)
* Clone remote repo locally
* Locate the directory in terminal
* Run `pipenv install`
* Run `pipenv shell`
* cd to the library directory and create a .env file
* Open the .env file in a text editor and add in the following lines:
```
DEBUG=on
SECRET_KEY=<your generated secret key>
DATABASE_URL=postgres://<postgresql username>:@127.0.0.1:5432/<database name>
```
* Run `python manage.py createsuperuser` to create an admin account
* Run `python manage.py runserver` to start the server locally
* You're all set to use the API!

<br>
<br>

# Endpoint Documentation

If you are running the server locally, the base URL will be displayed in the terminal after starting the server.
Unless indicated otherwise, the request body should be empty.

## User Login
Username and password required.

### Request
```json
POST /auth/token/login/
{
    "username": "pip",
    "password": "Estella"
}
```

### Response
```json
200 OK
{
    "auth_token": "<your token hash here>"
}
```

## User Logout
Token authentication required.

### Request
```json
POST /auth/token/logout/
```

### Response
```json
204 No Content
```

## Register New User
Username, password, and retyped password required.

### Request
```json
POST /auth/users/
{
    "username": "murderbot",
    "password": "sanctuarymoon",
    "re_password": "sanctuarymoon"
}
```

### Response
```json
201 Created
{
    "email": "",
    "username": "murderbot",
    "id": 160
}
```

## List All Books

### Request
```json
GET /books/
```

### Response
```json
200 OK
[
    {
		"pk": 49,
		"title": "A Tale of Two Cities",
		"author": {
			"pk": 1,
			"name": "Charles Dickens"
		},
		"genres": [],
		"tags": [],
		"reviews": []
	},
    (...)
]
```

## Book Detail
Number at the end of the URL should correspond to the book's pk.
### Request
```json
GET /books/53/
```

### Response
```json
200 OK
{
	"pk": 53,
	"title": "The Haunting of Hill House",
	"author": {
		"pk": 3,
		"name": "Shirley Jackson"
	},
	"pub_year": 1959,
	"genres": [],
	"tags": [],
	"reviews": []
}
```

## Add a New Book
Token authentication required. Title and author fields required.

### Request
```json
POST /books/
{
    "title": "American Gods",
    "author": "Neil Gaiman"
}
```

### Response
```json
201 Created
{
	"pk": 51,
	"title": "American Gods",
	"author": {
		"pk": 2,
		"name": "Neil Gaiman"
	},
	"pub_year": 2001,
	"genres": [],
	"tags": [],
	"reviews": []
}
```

## List a Book's Reviews

### Request
```json
GET /books/53/reviews/
```

### Response
```json
200 OK
[
    {
        "pk": 12,
        "user": {
            "pk": 144,
            "username": "simplereader"
        },
        "book": {
            "pk": 53,
            "title": "The Haunting of Hill House",
            "author": "Shirley Jackson"
        },
        "created": "2021-12-15T00:19:51.903050Z",
        "text": "Truly terrifying!"
    },
    (...)
]
```

## Add a Review
Authentication required.

### Request
```json
POST /books/51/reviews/
{
	"text": "Reads like a long roadtrip, but the atmosphere is excellent."
}
```

### Response
```json
201 Created
{
	"pk": 68,
	"user": {
		"pk": 144,
		"username": "simplereader"
	},
	"book": {
		"pk": 51,
		"title": "American Gods",
		"author": "Neil Gaiman"
	},
	"created": "2022-01-06T19:35:14.639079Z",
	"text": "Reads like a long roadtrip, but the atmosphere is excellent."
}
```

## Delete a Review

### Request
```json
DELETE /books/43/reviews/92/
```

### Response
```json
204 No Content
```

## List Featured Books

### Request
```json
GET /featured/
```

### Response
```json
200 OK
[
    {
		"pk": 52,
		"title": "Anansi Boys",
		"author": {
			"pk": 2,
			"name": "Neil Gaiman"
		},
		"genres": [],
		"tags": [],
		"reviews": []
	},
    (...)
]
```

## List Authors

### Request
```json
GET /authors/
```

### Response
```json
200 OK
[
	{
		"pk": 1,
		"name": "Charles Dickens",
		"books": [
			{
				"pk": 50,
				"title": "Great Expectations",
				"pub_year": 1861
			},
			{
				"pk": 49,
				"title": "A Tale of Two Cities",
				"pub_year": 1859
			}
		]
	},
    (...)
]
```

## Author Detail

### Request
```json
GET /authors/3/
```

### Response
```json
200 OK
{
	"pk": 3,
	"name": "Shirley Jackson",
	"books": [
		{
			"pk": 53,
			"title": "The Haunting of Hill House",
			"pub_year": 1959
		}
	]
}
```