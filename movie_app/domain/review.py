from datetime import datetime

from movie_app.domain.movie import Movie


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie = None
        self.__review_text = None
        self.__rating = None
        self.__timestamp = datetime.now()

        if type(movie) is Movie:
            self.__movie = movie

        if type(review_text) is str:
            self.__review_text = review_text.strip()

        if 1 <= rating <= 10 and type(rating) is int:
            self.__rating = rating

    def __repr__(self):
        return f"<Review {self.__movie.title}, {self.__movie.release_year}, {self.__timestamp}>"

    def __eq__(self, other):
        return (self.__movie, self.__review_text, self.__rating, self.__timestamp) \
               == (other.__movie, other.__review_text, other.__rating, other.__timestamp)

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
