from typing import Iterable
from movie_app.adapters.repository import AbstractRepository
from movie_app.domain.actor import Actor
from movie_app.domain.director import Director
from movie_app.domain.genre import Genre
from movie_app.domain.movie import Movie


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_movie(movie_rank: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_rank)
    if movie is None:
        raise NonExistentMovieException
    return movie_to_dict(movie)


def get_first_movie(repo: AbstractRepository):
    movie = repo.get_first_movie()
    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):
    movie = repo.get_last_movie()
    return movie_to_dict(movie)


def get_movies_by_rank(rank_list, repo: AbstractRepository):
    movies = repo.get_movies_by_rank(rank_list)
    movies_as_dict = movies_to_dict(movies)
    return movies_as_dict


def movie_to_dict(movie: Movie):
    movie_dict = {
        'rank': movie.rank,
        'title': movie.title,
        'release_year': movie.release_year,
        'description': movie.description,
        'director': director_to_dict(movie.director),
        'actors': actors_to_dict(movie.actors),
        'genres': genres_to_dict(movie.genres),
        'runtime_minutes': movie.runtime_minutes,
        'rating': movie.rating,
        'votes': movie.votes,
        'revenue': movie.revenue,
        'metascore': movie.metascore
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def director_to_dict(director: Director):
    director_dict = {
        'director_name': director.director_full_name
    }
    return director_dict


def directors_to_dict(directors: Iterable[Director]):
    return [director_to_dict(director) for director in directors]


def actor_to_dict(actor: Actor):
    actor_dict = {
        'actor_name': actor.actor_full_name
    }
    return actor_dict


def actors_to_dict(actors: Iterable[Actor]):
    return [actor_to_dict(actor) for actor in actors]


def genre_to_dict(genre: Genre):
    genre_dict = {
        'genre_name': genre.genre_name,
    }
    return genre_dict


def genres_to_dict(genres: Iterable[Genre]):
    return [genre_to_dict(genre) for genre in genres]


def dict_to_movie(dict):
    movie = Movie(dict.title, dict.release_year)
    movie.rank = dict.rank
    movie.description = dict.description
    movie.director = dict_to_director(dict.director)
    movie.actors = dict_to_actors(dict.actors)
    movie.genres = dict_to_genres(dict.genres)
    movie.runtime_minutes = dict.runtime_minutes
    movie.rating = dict.rating
    movie.votes = dict.votes
    movie.revenue = dict.revenue
    movie.metascore = dict.metascore
    return movie


def dict_to_director(dict):
    director = Director(dict.director_name)
    return director


def dict_to_actors(dict_list):
    actor_list = []
    for dict in dict_list:
        actor_list.append(Actor(dict.actor_name))
    return actor_list


def dict_to_genres(dict_list):
    genre_list = []
    for dict in dict_list:
        genre_list.append(Genre(dict.genre_name))
    return genre_list
