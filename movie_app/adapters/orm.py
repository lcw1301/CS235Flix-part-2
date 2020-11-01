from sqlalchemy import (
    MetaData, Table, Column, String, Integer, Text, Float, ForeignKey
)
from sqlalchemy.orm import mapper

from movie_app.domain.movie import Movie
from movie_app.domain.director import Director
from movie_app.domain.actor import Actor
from movie_app.domain.genre import Genre

metadata = MetaData()

movies = Table(
    'movies', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('rank', Integer),
    Column('title', String(255)),
    Column('description', Text),
    Column('release_year', Integer),
    Column('runtime_minutes', Float),
    Column('rating', Float),
    Column('votes', Integer),
    Column('revenue', Float),
    Column('metascore', Float)
)

directors = Table(
    'directors', metadata,
    Column('id', Integer),
    Column('director_full_name', String(255), unique=True, nullable=False)
)

genres = Table(
    'genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('genre_name', String(255), unique=True, nullable=False)
)

movie_genres = Table(
    'movie_genres', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

actors = Table(
    'actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('actor_full_name', String(255), unique=True, nullable=False)
)

movie_actors = Table(
    'movie_actors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)


def map_model_to_tables():
    mapper(Movie, movies, properties={
        '__id': movies.c.id,
        '__rank': movies.c.rank,
        '__title': movies.c.title,
        '__description': movies.c.description,
        '__release_year': movies.c.release_year,
        '__runtime_minutes': movies.c.runtime_minutes,
        '__rating': movies.c.rating,
        '__votes': movies.c.votes,
        '__revenue:': movies.c.revenue,
        '__metascore': movies.c.metascore
    })

    mapper(Director, directors, properties={
        '__id': directors.c.id,
        '__director_full_name': directors.c.director_full_name
    })

    mapper(Actor, actors, properties={
        '__id': actors.c.id,
        '__actor_full_name': actors.c.actor_full_name
    })

    mapper(Genre, genres, properties={
        '__id': genres.c.id,
        '__genre_name': genres.c.genre_name
    })
