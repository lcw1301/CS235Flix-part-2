import pytest

from movie_app.domain.actor import Actor
from movie_app.domain.director import Director
from movie_app.domain.genre import Genre
from movie_app.domain.movie import Movie
from movie_app.domain.review import Review
from movie_app.domain.user import User
from movie_app.domain.watchlist import WatchList


def test_director_full_name():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None
    director4 = Director("")
    assert repr(director4) == "<Director None>"


def test_director_equal():
    director1 = Director("b")
    director2 = Director("B")
    assert (director1 != director2)


def test_director_lt():
    director1 = Director("Cameron Diaz")
    director2 = Director("Brad Pitt")
    assert (director1 > director2)


def test_director_hash():
    director1 = Director("Taika Waititi")
    assert hash(director1)


def test_genre_name():
    genre1 = Genre("Comedy")
    assert repr(genre1) == "<Genre Comedy>"
    genre2 = Genre("")
    assert repr(genre2) == "<Genre None>"
    genre3 = Genre(0)
    assert genre3.genre_name is None


def test_actor_full_name():
    a1 = Actor("Taika Waititi")
    assert repr(a1) == "<Actor Taika Waititi>"
    a2 = Actor("")
    assert a2.actor_full_name is None
    a3 = Actor(42)
    assert a3.actor_full_name is None
    a4 = Actor("")
    assert repr(a4) == "<Actor None>"


def test_actor_add_colleague():
    a1 = Actor("Taika Waititi")
    a2 = Actor("Bob bob")
    a1.add_actor_colleague(a2)
    assert a1.actor_colleague == [a2]
    a3 = Actor("")
    a1.add_actor_colleague(a3)
    assert a1.actor_colleague == [a2, a3]


def test_actor_check_colleague():
    a1 = Actor("Taika Waititi")
    a2 = Actor("Bob bob")
    a1.add_actor_colleague(a2)
    assert (a1.check_if_this_actor_worked_with(a2))


# Movie Unit Tests
def test_movie_lt():
    m1 = Movie("", 0)
    m2 = Movie("x", 0)
    assert (m1 < m2)


def test_movie_eq():
    m1 = Movie("wow", 0)
    m2 = Movie("wow", 1899)
    assert (m1 == m2)


def test_set_title():
    m1 = Movie("wow", 0)
    m1.title = "WOW"
    assert (m1.title == "WOW")


def test_add_actors():
    m1 = Movie("wow", 0)
    m1.actors = [Actor("a"), Actor("b"), Actor("c")]
    assert (m1.actors == [Actor("a"), Actor("b"), Actor("c")])


def test_one_director():
    m1 = Movie("wow", 0)
    with pytest.raises(Exception):
        m1.director = [Director("a"), Director("b")]


def test_description():
    m1 = Movie("wow", 0)
    m1.description = ""
    assert (m1.description == "")


def test_hash():
    m1 = Movie("wow", 2000)
    hash1 = hash("wow" + str(2000))
    assert(hash(m1) == hash1)


def test_repr():
    m1 = Movie("wow", 0)
    assert(repr(m1) == "<Movie wow, None>")


# Review Unit Tests
def test_review_eq():
    r1 = Review("", "", 0)
    r2 = Review("", "", 0)
    assert (r1 == r2)


# User Unit Tests
def test_username():
    user1 = User('Martin', 'pw12345')
    user2 = User('IAN', 'pw67890')
    user3 = User('daniel', 'pw87465')
    user4 = User('', '')
    assert (repr(user1) == "<User martin>")
    assert (repr(user2) == "<User ian>")
    assert (repr(user3) == "<User daniel>")
    assert (repr(user4) == "<User None>")


def test_user_eq():
    user1 = User('a', 'pw12345')
    user2 = User('b', 'pw67890')
    assert (user1 != user2)


def test_user_lt():
    user1 = User('a', 'pw12345')
    user2 = User('b', 'pw67890')
    assert (user2 > user1)


def test_user_hash():
    user1 = User('a', 'pw12345')
    user2 = User('a', 'pw67890')
    assert (hash(user1) == hash(user2))


def test_watch_movie():
    user1 = User('Martin', 'pw12345')
    m1 = Movie("a", 2000)
    m2 = Movie("b", 2000)
    m1.runtime_minutes = 10
    m2.runtime_minutes = 20
    user1.watch_movie(m1)
    user1.watch_movie(m2)
    assert (user1.time_spent_watching_movies_minutes == 30)
    assert (user1.watched_movies == [m1, m2])


def test_add_review():
    user1 = User('Martin', 'pw12345')
    m1 = Movie('a', 2000)
    r1 = Review(m1, 'wow', 10)
    user1.add_review(r1)
    assert (user1.reviews == [r1])


# WatchList Unit Tests
@pytest.fixture()
def w():
    return WatchList()


def test_iter_and_next(w):
    w.add_movie(Movie("Moana", 2016))
    w.add_movie(Movie("Ice Age", 2002))
    w.add_movie(Movie("Guardians of the Galaxy", 2012))
    iterable = iter(w)
    assert next(iterable) == Movie("Moana", 2016)


def test_add_and_remove_movie(w):
    w.add_movie(Movie("Moana", 2016))
    w.remove_movie(Movie("Moana", 2016))
    assert w.watchlist == []


def test_select_movie(w):
    w.add_movie(Movie("Moana", 2016))
    assert w.select_movie_to_watch(0) == Movie("Moana", 2016)


def test_size(w):
    w.add_movie(Movie("Moana", 2016))
    assert w.size() == 1


def test_first_movie_in_watchlist(w):
    w.add_movie(Movie("Moana", 2016))
    w.add_movie(Movie("Ice Age", 2002))
    w.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert w.first_movie_in_watchlist() == Movie("Moana", 2016)


def test_clear_watchlist(w):
    w.add_movie(Movie("Moana", 2016))
    w.add_movie(Movie("Ice Age", 2002))
    w.add_movie(Movie("Guardians of the Galaxy", 2012))
    w.clear_watchlist()
    assert w.watchlist == []
