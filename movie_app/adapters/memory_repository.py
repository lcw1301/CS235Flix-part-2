import os
from typing import List
from movie_app.adapters.repository import AbstractRepository
from movie_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from movie_app.domain.actor import Actor
from movie_app.domain.director import Director
from movie_app.domain.genre import Genre
from movie_app.domain.movie import Movie


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._directors = list()
        self._genres = list()
        self._actors = list()
        self._movies = list()
        self._movies_index = dict()

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_director(self, director_name) -> Director:
        return next(
            (director for director in self._directors if director.director_full_name == director_name), None)

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genres(self) -> List[Genre]:
        return self._genres

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actor(self, actor_name) -> Actor:
        return next((actor for actor in self._actors if actor.actor_full_name == actor_name), None)

    def add_movie(self, movie: Movie):
        self._movies.append(movie)
        self._movies_index[movie.rank] = movie

    def get_movie(self, rank: int) -> Movie:
        movie = None
        try:
            movie = self._movies_index[rank]
        except KeyError:
            pass
        return movie

    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self) -> Movie:
        movie = None
        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self) -> Movie:
        movie = None
        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_movies_by_rank(self, rank_list):
        existing_ranks = [rank for rank in rank_list if rank in self._movies_index]

        movies = [self._movies_index[rank] for rank in existing_ranks]
        return movies


def load_data(data_path: str, repo: MemoryRepository):
    all_data = MovieFileCSVReader(os.path.join(data_path, 'Data1000Movies.csv'))
    all_data.read_csv_file()

    for director in all_data.dataset_of_directors:
        repo.add_director(director)

    for genre in all_data.dataset_of_genres:
        repo.add_genre(genre)

    for actor in all_data.dataset_of_actors:
        repo.add_actor(actor)

    for movie in all_data.dataset_of_movies:
        repo.add_movie(movie)


def populate(data_path: str, repo: MemoryRepository):
    load_data(data_path, repo)
