# FitKick-API

This is the repo for the back-end of the FitKick app. The purpose of this app is to make it easier for people to get/stay fit by helping users find exercises and create workouts based on their needs.

### FitKick Back-End

The front-end for this app can be found at:

> https://github.com/tkg808/fitkick-ui

## Technologies Used

* VScode
* Heroku
* Python
* Django
* Postgres
* djangorestframework
* psycopg2-binary
* dj-database-url
* gunicorn
* djoser
* django-cors-headers
* whitenoise
* Pages

## Installation Instructions

* Fork and clone this repo

> git clone https://github.com/tkg808/fitkick-api.git

* Change into this directory

> cd fitkick-api

* Open in your preferred IDE

* Change into virtual environment and install dependencies

```
pipenv shell

pipenv install django psycopg2-binary dj-database-url gunicorn djoser django-cors-headers whitenoise
```
* You will need to set up a database to test out this code, try checking out this documentation to get started:

> https://www.postgresql.org/


* Open http://localhost:8000 to interact with the Django REST framework admin interface

## Contribution Guidelines

### How to Contribute

Feel free to contribute to this app with code or suggestions. If you would like to contribute code - install the app, checkout to a dev branch, play with the code, then submit a pull request.

### How to Identify Bugs

You can submit an issue on the git repo, or work on a dev branch and submit a pull request with suggested code to fix the bug. Please detail the bug and recommendations for solutions if possible.

### How to Propose Improvements

You can submit an issue on the git repository detailing your suggestion.

# Planning

## Wireframes

![req-res](https://tinyimg.io/i/YvGOsz4.png)

## Models

### User

* Enables authentication.
* One to many relationship with Workout.
* One to many relationship with Exercise.
* One to many relationship with ExerciseInfo.

### Workout

* Stores a collection of exercises.
* Many to one relationship with User.
* Many to many relationship with Exercise.

### Exercise

* Stores the exercise type and muscles used.
* Many to one relationship with User.
* Many to many relationship with Exercise.
* Many to one relationship with ExerciseInfo.

### ExerciseInfo

* Stores user specific information for an exercise.
* Many to one relationship with User.
* Many to one relationship with Exercise.

## User Stories

### MVP Goals

* As a user, I want to be able to create/retrieve/update/delete a workout so I can accurately maintain a list of workouts I like for future reference.
* As a user, I want to be able to create/retrieve/update/delete an exercise so I can accurately maintain a list of exercises I like for future reference.
* As a user, I want to be able to see other users' workouts and exercises so I can get ideas for workouts and exercises I can do.
* As a user, I want to be able to search for exercises based on different criteria so I can get ideas for exercises I can do.
* As a user, I want to be able to login so that the workouts and exercises I create can only be changed or deleted by me.

### Stretch Goals

* As a user, I want to be able to save certain information for exercises (ie notes, sets, reps, weights, etc.) that are exclusive to me even if I didn't create that exercise so that I can effectively track my experiences with those exercises.
* As a user, I want to be able to look back at past workouts so that I can see my progress and possibly make adjustments to my workouts.
* As a user, I want to be able to connect with other users so that I can feel a sense of community that can help keep me accountable.