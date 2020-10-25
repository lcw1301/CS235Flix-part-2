from movie_app.domain.movie import Movie
from movie_app.domain.review import Review


class User:

    def __init__(self, user_name, password):
        self.__user_name = None
        self.__password = None
        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0

        if user_name != "" and type(user_name) is str:
            self.__user_name = user_name.strip().lower()

        if password != "" and type(password) is str:
            self.__password = password.strip()

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    @property
    def user_name(self) -> str:
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        if user_name != "" and type(user_name) is str:
            self.__user_name = user_name.strip().lower()

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password):
        if password != "" and type(password) is str:
            self.__password = password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, minutes):
        if minutes > 0 and type(minutes) is int:
            self.__time_spent_watching_movies_minutes = minutes

    def watch_movie(self, movie):
        if type(movie) is Movie:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) is Review:
            self.__reviews.append(review)
