class Actor:

    def __init__(self, actor_full_name: str):
        self.__actor_full_name = None
        self.__colleagues = list()

        if actor_full_name != "" and type(actor_full_name) is str:
            self.__actor_full_name = actor_full_name.strip()

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def actor_colleague(self) -> list:
        return self.__colleagues

    def add_actor_colleague(self, colleague):
        if type(colleague) is Actor:
            if colleague not in self.__colleagues:
                self.__colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if type(colleague) is Actor:
            return colleague in self.__colleagues
