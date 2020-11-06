# MoviesAPI

Recruitment task for Decathlon

## Local installation
- clone repository
- move to project direction
- run ``docker-compose up --build``(it will apply migrations and run app)
- go to ``http://localhost:8003/<endpoint>`` to use application

## Endpoints
- ``/movies`` - [POST] with {"title": movie_title} - retrieves data from ``http://www.omdbapi.com`` , creates movie object and returns movie data
- ``/movies`` - [GET] - list of all movies
    <b>Optional parameters</b>:
    - filtering: ``/movies?<filter>=<data>`` where ``<filter>`` can be ``rated`` or ``type``
    - sorting: ``/movies?ordering=year`` from oldest or  ``/movies?ordering=-year`` from newest
- ``/movies/<id>`` [PATCH] - with body with fields you want to change
- ``/movies/<id>`` [DELETE] - if movie exists delete it
- ``/comments`` [POST] with { "text": text, "movie": movie_id} - if movie exists create comment for it
- ``/comments`` [GET] - list of comments
    <b>Optional parameters</b>:
     - filtering: ``/comments?movie=id``
- ``/top?start=date&end=date`` - [GET] - returns movies ordered by number of comments in specified time range  

## Testing
- run ``docker-compose run api python manage.py test`` to start tests
