from movie_app.domain.movie import Movie


class WatchList:

    def __init__(self):
        self.__watchlist = list()

    @property
    def watchlist(self):
        return self.__watchlist

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__watchlist):
            result = self.__watchlist[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration

    def add_movie(self, movie: Movie):
        if type(movie) is Movie:
            if movie not in self.__watchlist:
                self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if type(movie) is Movie:
            if movie in self.watchlist:
                self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index: int):
        if type(index) is int and 0 <= index < len(self.__watchlist):
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) != 0:
            return self.__watchlist[0]

    def clear_watchlist(self):
        self.__watchlist.clear()
