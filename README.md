# Music Library

REST API written in Django

## Technologies

- Python
- Django REST Framework
- Postman

## Models

Song model
Property names

- title (CharField)
- artist (CharField)
- album (CharField)
- release_date (DateField)
- genre (CharField)

## Paths

- 127.0.0.1:8000/music/
- 127.0.0.1:8000/music/<int:pk>/

## Design

REST web API in Django REST Frameworkcan

Uses HTTP requests interact with the data set

GET endpoint responds with a 200 success status code and all of the songs within the Music table

GET by id endpoint that does the following:

- Accepts a value from the request’s URL (The id of the song to retrieve)
- Returns a 200 status code
- Responds with the song in the database that has the id that was sent through the URL

POST endpoint that does the following:

- Accepts a body object from the request in the form of a Song model.
- Adds the new song to the database
- Returns a 201 status code
-Responds with the newly created song object

PUT endpoint that does the following things:

- Accepts a value from the request’s URL (The id of the song to be updated)
- Accepts a body object from the request in the form of a Song model
- Finds the song in the Music table and updates that song with the properties that were sent in the request’s body
- Returns a 200 status code
- Responds with the newly updated song object

DELETE endpoint that does the following things:

- Accepts a value from the request’s URL
- Returns a 200 status code
- Responds with the song in the database that has just been deleted

## Tests with Postman

- POST, PUT, DELETE, and both GET requests (get by id and get all) saved to a collection, and exported as JSON

## Extra Feature

- Ability to “like” a song through the web API and have the number of likes saved in the database with the song
