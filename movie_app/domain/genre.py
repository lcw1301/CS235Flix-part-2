
class Genre:

    def __init__(self, genre_name: str):
        self.__genre_name = None

        if genre_name != "" and type(genre_name) is str:
            self.__genre_name = genre_name.strip()

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        return self.__genre_name == other.__genre_name

    def __hash__(self):
        return hash(self.__genre_name)

    def __lt__(self, other):
        return self.__genre_name < other.__genre_name

    @property
    def genre_name(self) -> str:
        return self.__genre_name
