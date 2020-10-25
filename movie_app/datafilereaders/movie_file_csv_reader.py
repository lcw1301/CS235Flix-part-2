import csv

from movie_app.domain.actor import Actor
from movie_app.domain.director import Director
from movie_app.domain.genre import Genre
from movie_app.domain.movie import Movie


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    @property
    def dataset_of_movies(self) -> list:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> set:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> set:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            i = 0

            for row in movie_file_reader:
                rank = int(row['Rank'].strip())
                title = row['Title']
                release_year = int(row['Year'].strip())
                actors = row['Actors'].split(',')
                genres = row['Genre'].split(',')
                description = row['Description'].strip()
                director = Director(row['Director'].strip())
                runtime_minutes = int(row['Runtime (Minutes)'].strip())
                rating = float(row['Rating'].strip()) if row['Rating'].strip() != 'N/A' else row['Rating'].strip()
                votes = int(row['Votes'].strip()) if row['Votes'].strip() != 'N/A' else row['Votes'].strip()
                revenue = float(row['Revenue (Millions)'].strip()) \
                    if row['Revenue (Millions)'].strip() != 'N/A' else row['Revenue (Millions)'].strip()
                metascore = int(row['Metascore'].strip()) \
                    if row['Metascore'].strip() != 'N/A' else row['Metascore'].strip()

                movie_genres = list()
                for g in genres:
                    genre = g.strip()
                    movie_genres.append(Genre(genre))

                movie_actors = list()
                for a in actors:
                    actor = a.strip()
                    movie_actors.append(Actor(actor))

                self.__dataset_of_movies.append(Movie(title, release_year))
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].rank = rank
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].genres = movie_genres
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].description = description
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].director = director
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].actors = movie_actors
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].runtime_minutes = runtime_minutes
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].rating = rating
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].votes = votes
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].revenue = revenue
                self.__dataset_of_movies[len(self.__dataset_of_movies) - 1].metascore = metascore
                self.__dataset_of_directors.add(director)

                for actor in movie_actors:
                    self.__dataset_of_actors.add(actor)

                for genre in movie_genres:
                    self.__dataset_of_genres.add(genre)

                i += 1