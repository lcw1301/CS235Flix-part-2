from typing import List
from movie_app.domain.actor import Actor
from movie_app.domain.director import Director
from movie_app.domain.genre import Genre
from movie_app.domain.movie import Movie


def test_repo_can_add_director(in_memory_repo):
    director = Director('Peter Jackson')
    in_memory_repo.add_director(director)
    assert in_memory_repo.get_director('Peter Jackson') == director


def test_repo_can_retrieve_director(in_memory_repo):
    director = in_memory_repo.get_director('James Gunn')
    assert director == Director('James Gunn')


def test_repo_does_not_retrieve_non_existent_director(in_memory_repo):
    director = in_memory_repo.get_director('Bob')
    assert director is None


def test_repo_can_add_genre(in_memory_repo):
    genre = Genre('Anime')
    in_memory_repo.add_genre(genre)
    assert genre in in_memory_repo.get_genres()


def test_repo_can_retrieve_genres(in_memory_repo):
    genres: List[Genre] = in_memory_repo.get_genres()
    assert len(genres) == 20


def test_repo_can_add_actor(in_memory_repo):
    actor = Actor('Vin Diesel')
    in_memory_repo.add_actor(actor)
    assert in_memory_repo.get_actor('Vin Diesel') == actor


def test_repo_can_retrieve_actor(in_memory_repo):
    actor = in_memory_repo.get_actor('Vin Diesel')
    assert actor == Actor('Vin Diesel')


def test_repo_does_not_retrieve_non_existent_actor(in_memory_repo):
    actor = in_memory_repo.get_actor('Ace')
    assert actor is None


def test_repo_can_add_movie(in_memory_repo):
    movie = Movie('New Movie', 2020)
    movie.rank = 1001
    in_memory_repo.add_movie(movie)
    assert in_memory_repo.get_movie(1001) == movie


def test_repo_does_not_retrieve_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(0)
    assert movie is None


def test_repo_can_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.title == 'Guardians of the Galaxy'


def test_repo_can_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.title == 'Nine Lives'


def test_repo_can_retrieve_movie_count(in_memory_repo):
    no_of_movies = in_memory_repo.get_number_of_movies()
    assert no_of_movies == 1000


def test_repo_can_get_movies_by_ranks(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank([1, 2, 3])
    assert len(movies) == 3
    assert movies[0].title == 'Guardians of the Galaxy'
    assert movies[1].title == 'Prometheus'
    assert movies[2].title == 'Split'


def test_repo_does_not_retrieve_movie_for_non_existent_rank(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank([1000, 1001])
    assert len(movies) == 1
    assert movies[0].title == 'Nine Lives'


def test_repo_returns_an_empty_list_for_non_existent_ranks(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank([1111, 2222])
    assert len(movies) == 0
