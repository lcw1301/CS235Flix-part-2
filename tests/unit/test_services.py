from movie_app.movies import services as movies_services
import pytest


def test_can_get_movie(in_memory_repo):
    movie_rank = 1
    movie_as_dict = movies_services.get_movie(movie_rank, in_memory_repo)
    assert movie_as_dict['rank'] == movie_rank
    assert movie_as_dict['title'] == 'Guardians of the Galaxy'
    assert movie_as_dict['release_year'] == 2014
    assert movie_as_dict['description'] == 'A group of intergalactic criminals are forced to work together to stop ' \
                                           'a fanatical warrior from taking control of the universe.'
    assert movie_as_dict['runtime_minutes'] == 121
    assert movie_as_dict['rating'] == 8.1
    assert movie_as_dict['votes'] == 757074
    assert movie_as_dict['revenue'] == 333.13
    assert movie_as_dict['metascore'] == 76
    director_as_dict = movie_as_dict['director']
    assert 'James Gunn' == director_as_dict['director_name']
    assert len(movie_as_dict['actors']) == 4
    actor_names = [dictionary['actor_name'] for dictionary in movie_as_dict['actors']]
    assert 'Chris Pratt' in actor_names
    assert 'Vin Diesel' in actor_names
    assert 'Bradley Cooper' in actor_names
    assert 'Zoe Saldana' in actor_names
    assert len(movie_as_dict['genres']) == 3
    genre_names = [dictionary['genre_name'] for dictionary in movie_as_dict['genres']]
    assert 'Action' in genre_names
    assert 'Adventure' in genre_names
    assert 'Sci-Fi' in genre_names


def test_cannot_get_movie_with_non_existent_rank(in_memory_repo):
    movie_rank = 1001

    with pytest.raises(movies_services.NonExistentMovieException):
        movies_services.get_movie(movie_rank, in_memory_repo)


def test_get_first_movie(in_memory_repo):
    movie_as_dict = movies_services.get_first_movie(in_memory_repo)
    assert movie_as_dict['rank'] == 1


def test_get_last_movie(in_memory_repo):
    movie_as_dict = movies_services.get_last_movie(in_memory_repo)
    assert movie_as_dict['rank'] == 1000


def test_get_movies_by_rank(in_memory_repo):
    target = [1, 2, 3]
    movies_as_dict = movies_services.get_movies_by_rank(target, in_memory_repo)
    assert len(movies_as_dict) == 3
    movie_ranks = [movie['rank'] for movie in movies_as_dict]
    assert movie_ranks == target
