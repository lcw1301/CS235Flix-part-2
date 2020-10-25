import abc
from typing import List

from movie_app.domain.actor import Actor
from movie_app.domain.director import Director
from movie_app.domain.genre import Genre
from movie_app.domain.movie import Movie
from movie_app.domain.review import Review
from movie_app.domain.user import User
from movie_app.domain.watchlist import WatchList

repo_instance = None


class RepositoryException(Exception):

    def __init__(self):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_director(self, director: Director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_director(self, director_name) -> Director:
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actor(self, actor_name) -> Actor:
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, rank: int) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_rank(self, rank_list):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_ranks_for_genre(self, genre_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        if review.movie is None:
            raise RepositoryException

    @abc.abstractmethod
    def get_reviews(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username: str) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def add_watchlist(self, watchlist: WatchList):
        raise NotImplementedError

    @abc.abstractmethod
    def get_watchlist(self, user: User) -> List[WatchList]:
        raise NotImplementedError
