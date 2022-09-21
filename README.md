# Casting Agency API
# Introduction 
The Casting Agency API supports a basic casting agency by allowing users to query the database  for movies and actors.
There are three different users roles (and related permissions), Which are:

- Casting Assistant
    - Can view actors and movies
- Casting Director
    - All permissions a Casting Assistant has and...
    - Add or delete an Actor from the database
    - Modify actors or movies
- Executive Producer
    - All permissions a Casting Director has and
    - Add or delete a movie from the database


## Capstone Project for Udacity's Full Stack Developer Nanodegree
Heroku Link: https://capstone-agency7.herokuapp.com

While running locally: http://localhost:5000
## Getting Started

### Installing Dependencies

```
install dependencies by running:

```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in api.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

# Deploy to heroku
- Create app in heroku
- Set your environment variables
- Define your Procfile file
- Push your code to github
- Connect your repository to heroku
- Click on deploy option
## Running the server

First you have to start the postgresql service by running the following command
```bash
sudo service postgresql start
```
After that you have to create the database by running

```bash
DROP DATABASE agency;
CREATE DATABASE agency;
```

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:



To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

This will install all of the required packages we selected within the `requirements.txt` file.
# Error Handling
Errors are returned as JSON objects in the following format:

```json
{
    "error": 404,
    "message": "resource not found",
    "success": false
}
```
The API will return the following errors based on how the request fails:
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 404: Not Found
    - 405: Method Not Allowed
    - 422: Unprocessable Entity
    - 500: Internal Server Error



# API Documentation

Errors
`401`
`403`
`404`
`422`

Note: all error handlers return a JSON object with the request status and error message.

401
- 401 error handler is returned when there is an issue with the authentication necessary for the action being requested. 
```
{
	"error": 401,
	"message": "Authentication error.",
	"success": false
}
```
403
- 403 error handler occurs when the requested action is not allowed, i.e. incorrect permissions.
```
{
	"error": 403,
	"message": "Forbidden.",
	"success": false
}
```
404
- 404 error handler occurs when a request resource cannot be found in the database, i.e. an actor with a nonexistent ID is requested.
```
{
	"error": 404,
	"message": "Item not found.",
	"success": false
}
```
422
- 422 error handler is returned when the request contains invalid arguments, i.e. a difficulty level that does not exist.
```
{
	"error": 422,
	"message": "Request could not be processed.",
	"success": false
}
```

Endpoints
`GET '/actors'`
`GET '/movies'`
`POST '/actors'`
`POST '/movies'`
`PATCH '/actors/<int:actor_id>'`
`PATCH '/movies/<int:movie_id>'`
`DELETE '/actors/<int:actor_id>'`
`DELETE '/movies/<int:movie_id>'`

GET '/actors'
- Fetches a JSON object with a list of actors in the database.
- Request Arguments: None
- Returns: An object with a single key, actors, that contains multiple objects with a series of string key pairs.
```
{
  "actors": [
    {
      "age": 30,
      "gender": "male",
      "id": 1,
      "name": "Tobey"
    },
    {
      "age": 32,
      "gender": "female",
      "id": 2,
      "name": "Megan Fox"
    },
    {
      "age": 55,
      "gender": "female",
      "id": 3,
      "name": "Rosemary"
    },
    {
      "age": 40,
      "gender": "male",
      "id": 4,
      "name": "Willen"
    },
    {
      "age": 50,
      "gender": "male",
      "id": 5,
      "name": "Robert"
    },
    {
      "age": 40,
      "gender": "male",
      "id": 6,
      "name": "Chris Evans"
    },
    {
      "age": 55,
      "gender": "male",
      "id": 7,
      "name": "Robert Downey"
    },
    {
      "age": 30,
      "gender": "female",
      "id": 8,
      "name": "Jennifer Lawrence"
    },
    {
      "age": 30,
      "gender": "female",
      "id": 9,
      "name": "Margot Robbie"
    },
    {
      "age": 37,
      "gender": "female",
      "id": 10,
      "name": "Scarlett Johansson"
    },
    {
      "age": 24,
      "gender": "male",
      "id": 11,
      "name": "Tom Holland"
    },
    {
      "age": 50,
      "gender": "male",
      "id": 13,
      "name": "Jackie Chan"
    },
    {
      "age": 50,
      "gender": "male",
      "id": 14,
      "name": "Jackie Chan"
    },
    {
      "age": 29,
      "gender": "female",
      "id": 15,
      "name": "Keke Palmer"
    },
    {
      "age": 29,
      "gender": "female",
      "id": 16,
      "name": "Keke Palmer"
    },
    {
      "age": 29,
      "gender": " female",
      "id": 17,
      "name": "Keke Palmer"
    },
    {
      "age": 44,
      "gender": "male",
      "id": 18,
      "name": "Kevin Hart"
    }
  ],
  "success": true
}


```
GET '/movies'
- Fetches a JSON object with a list of movies in the database.
- Request Arguments: None
- Returns: An object with a single key, movies, that contains multiple objects with a series of string key pairs.
```
{
  "movies": [
    {
      "duration": 2,
      "id": 1,
      "release_year": 1976,
      "title": "kong I"
    },
    {
      "duration": 5,
      "id": 2,
      "release_year": 1998,
      "title": "Titanic"
    },
    {
      "duration": 2,
      "id": 3,
      "release_year": 1998,
      "title": "Titanic"
    },
    {
      "duration": 3,
      "id": 4,
      "release_year": 2012,
      "title": "Avengers 1"
    },
    {
      "duration": 2,
      "id": 5,
      "release_year": 2015,
      "title": "Avengers 2"
    },
    {
      "duration": 2,
      "id": 6,
      "release_year": 1976,
      "title": "Rocky I"
    },
    {
      "duration": 2,
      "id": 8,
      "release_year": 2018,
      "title": "La hera del hielo"
    },
    {
      "duration": 3,
      "id": 9,
      "release_year": 2022,
      "title": "Nope"
    }
  ],
  "success": true
}
```
POST '/actors'
- Posts a new actor to the database, including the name, age, gender, and actor ID, which is automatically assigned upon insertion.
- Request Arguments: Requires three string arguments: name, age, gender.
- Returns: An actor object with the name, actor ID.
-curl -X POST -H "Content-Type: application/json" -d '{"name":"Kevin Hart","age":44,"gender":"male"}' http://127.0.0.1:5000/actors


```
{"actor":"Kevin Hart","created":19,"success":true}
```
POST '/movies'
- Posts a new movie to the database, including the title, release, and movie ID, which is automatically assigned upon insertion.
- Request Arguments: Requires two string arguments: title, release.
- Returns: A movie object with the movie ID, release, and title.
-curl -X POST -H "Content-Type: application/json" -d '{"title":"Nope","release_year":2022,"duration":2}' http://127.0.0.1:5000/movies

```
{"created":9,"movie":"Nope","success":true,"total_movies":7}
```
PATCH '/actors/<int:actor_id>'
- Patches an existing actor in the database.
- Request arguments: Actor ID, included as a parameter following a forward slash (/), and the key to be updated passed into the body as a JSON object. For example, to update the age for '/actors/6'
```
{
	"age": "36"
}
```
- Returns: An actor object with the full body of the specified actor ID.
```
{
    "actor": {
        "age": "36",
        "gender": "male",
        "id": 6,
        "name": "Henry Cavill"
    },
    "success": true
}
```
PATCH '/movies/<int:movie_id>'
- Patches an existing movie in the database.
- Request arguments: Movie ID, included as a parameter following a forward slash (/), and the key to be updated, passed into the body as a JSON object. For example, to update the age for '/movies/5'
-curl -d '{"title":"Nope","release_year":2022,"duration":3}' -H 'Content-Type: application/json' -X PATCH http://127.0.0.1:5000/movies/9
```
{"success":true,"total_movies":9,"updated_movie":9}
```

```


```
DELETE '/actors/<int:actor_id>'
- Deletes an actor in the database via the DELETE method and using the actor id.
- Request argument: Actor id, included as a parameter following a forward slash (/).
- Returns: ID for the deleted question.
 curl -X DELETE http://127.0.0.1:5000/actors/19
```
{"deleted_actor":19,"success":true}
```
DELETE '/movies/<int:movie_id>'
- Deletes a movie in the database via the DELETE method and using the movie id.
- Request argument: Movie id, included as a parameter following a forward slash (/).
- Returns: ID for the deleted question .
curl -X DELETE http://127.0.0.1:5000/movies/10
```
{"deleted_movie":10,"success":true}
```


## Testing
For testing the backend, run the following commands (in the exact order):
```
dropdb agency
createdb agency
psql agency < agency.sql
python3 test_agency.py
```
