from movie_app.domain.actor import Actor
from movie_app.domain.director import Director
from movie_app.domain.genre import Genre


class Movie:

    def __init__(self, title: str, release_year: int):
        self.__rank = None
        self.__description = ""
        self.__director = Director("")
        self.__actors = list()
        self.__genres = list()
        self.__runtime_minutes = 0
        self.__rating = None
        self.__votes = None
        self.__revenue = None
        self.__metascore = None
        self.__title = None
        self.__release_year = None

        if title != "" and type(title) is str:
            self.__title = title.strip()

        if release_year >= 1900 and type(release_year) is int:
            self.__release_year = release_year

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return (self.__title, self.__release_year) == (other.__title, other.__release_year)

    def __lt__(self, other):
        return (("None" if self.__title is None else self.__title,
                 "None" if self.__release_year is None else self.__release_year)
                <
                ("None" if other.__title is None else other.__title,
                 "None" if other.__release_year is None else other.__release_year))

    def __hash__(self):
        return hash(self.__title + str(self.__release_year))

    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def description(self) -> str:
        return self.__description

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @property
    def rating(self) -> float:
        return self.__rating

    @property
    def votes(self) -> int:
        return self.__votes

    @property
    def revenue(self) -> float:
        return self.__revenue

    @property
    def metascore(self) -> int:
        return self.__metascore

    @title.setter
    def title(self, title):
        if title != "" and type(title) is  str:
            self.__title = title.strip()

    @rank.setter
    def rank(self, rank):
        if type(rank) is int:
            self.__rank = rank

    @description.setter
    def description(self, description):
        if type(description) is str:
            self.__description = description.strip()

    @director.setter
    def director(self, director):
        if type(director) is Director:
            self.__director = director
        else:
            raise Exception

    @actors.setter
    def actors(self, actors):
        if type(actors) is list:
            self.__actors = actors

    @genres.setter
    def genres(self, genres):
        if type(genres) is list:
            self.__genres = genres

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is int:
            if runtime_minutes <= 0:
                raise ValueError

            self.__runtime_minutes = runtime_minutes

    @rating.setter
    def rating(self, rating):
        if type(rating) is float:
            self.__rating = rating
        else:
            if type(rating) is int:
                self.__rating = float(rating)

    @votes.setter
    def votes(self, votes):
        if type(votes) is int:
            self.__votes = votes

    @revenue.setter
    def revenue(self, revenue):
        if type(revenue) is float:
            self.__revenue = revenue
        else:
            if type(revenue) is int:
                self.__revenue = float(revenue)

    @metascore.setter
    def metascore(self, metascore):
        if type(metascore) is int:
            self.__metascore = metascore

    def add_actor(self, actor):
        if type(actor) is Actor:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if type(actor) is Actor:
            if actor in self.__actors:
                self.__actors.remove(actor)

    def add_genre(self, genre):
        if type(genre) is Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if type(genre) is Genre:
            if genre in self.__genres:
                self.__genres.remove(genre)
