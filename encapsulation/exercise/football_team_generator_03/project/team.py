class Team:
    name: str
    rating: int
    players: list

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        if isinstance(value, list):
            self.__players = value

    def add_player(self, player) -> str:
        if player in self.players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name) -> str:
        if player_name not in map(lambda p: p.name, self.players):
            return f"Player {player_name} not found"
        player = [p for p in self.__players if p.name == player_name][0]

        self.__players.remove(player)
        return player