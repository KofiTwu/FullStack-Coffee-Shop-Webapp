# Full Stack Trivia API

## Full Stack Trivia

Full stack trivia is a way for Udacity's employees and students to connect with each other. Allowing them to create bonding experiences by placing trivia once a week.

## API Description

1. Displays questions — both by all questions and by category. Questions has the ability to show the question, category and difficulty rating. Answers are hidden and can be shown with the press of a button.
2. Questions can be deleted with the press of a button.
3. Questions can be added, text for question and answer are required.
4. All questions can be searched, based on text query string.
5. The game is played by category or all questions, in a random order.

## Local Requirements

Requires Python 3.7 or later

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend micro-services framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first en sure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

# Full Stack Trivia API Frontend

## Getting Setup

> _tip_: the frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman or curl, update the endpoints in the frontend, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _tip_: **npm i** is shorthand for **npm install**

## Required Tasks

## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use `npm start`. You can change the script in the `package.json` file.

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

# Endpoints

### GET '/categories'

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.

Example: `CURL -X GET http://127.0.0.1:5000/categories`

```
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
  "success": true
}
```

### GET '/questions'

- Fetches a dictionary of questions, paginated in groups of 10.
- Returns JSON object of categories, questions dictionary with answer, category, difficulty, id and question.

Example: `curl http://localhost:5000/questions`

```
{
    "categories": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
    ],
    "current_category": [],
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }
        ... # omitted for brevity
    ],
    "success": true,
    "total_questions": 33
}
```

### DELETE '/questions/<int:question_id>'

- Deletes selected question by id
- Returns 200 if question is successfully deleted.
- Returns 404 if question did not exist
- Returns JSON object of deleted id, remaining questions, and length of total questions

Example: `curl -X DELETE http://localhost:5000/question/2`

```
{
    "deleted": 2,
    "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }
        ... # omitted for brevity
    ],
    "success": true,
    "total_questions": 32
}
```

### POST '/questions'

- Creates a new question posted from the react front end.
- Fields are: answer, difficulty and category.
- Returns a success value and ID of the question.
- If search field is present will return matching expressions

Example (Create):
`curl -X POST -H "Content-Type: application/json" -d '{"question":"Through which country does the greater part of the Nile flow", "answer":"Sudan", "difficulty":"5", "category":"3"}' http://127.0.0.1:5000/questions`


```
{
  "created": 25, 
  "question": {
    "answer": "Sudan", 
    "category": 3, 
    "difficulty": 5, 
    "id": 25, 
    "question": "Through which country does the greater part of the Nile flow"
  }, 
  "success": true
}

```

### POST  search for a question '/search'
Example (Search):

`curl http://127.0.0.1:5000/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"who"}'`

```
{
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}

```

### GET '/categories/<cat_id>/questions'

- Returns JSON response of current_category, and the questions pertaining to that category

Example: `curl http://localhost:5000/categories/3/questions`

```
{
  "current_category": 3, 
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Lake Nyos", 
      "category": 3, 
      "difficulty": 5, 
      "id": 24, 
      "question": "What is the smallest lake in Africa"
    }
  ], 
  "success": true, 
  "total_questions": 4
}

```

### POST '/quizzes'

- Generates a quiz based on category or a random selection depending on what the user chooses.
- Returns a random question

Example: `curl http://localhost:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[], "quiz_category":{"type":"Art","id":2}}'`

```
{
  "question": {
    "answer": "One",
    "category": 2,
    "difficulty": 4,
    "id": 18,
    "question": "How many paintings did Van Gogh sell in his lifetime?"
  },
  "success": true
}
```

## Error Handlers

When an error occurs a JSON response is returned

- Returns these error types when the request fails - 400: Bad Request - 404: Resource Not Found - 422: Not Processable - 500: Internal Server Error
  Example "Resource Not Found":

```
{
	"success": False,
	"error": 404,
	"message": "Resource Not Found"
}
```

## Testing

To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
