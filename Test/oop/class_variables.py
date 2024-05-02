class Player:
    __number_of_players: int = 0

    def __init__(self):
        self.__add_player()

    @classmethod
    def __add_player(cls):
        cls.__number_of_players += 1


player_1 = Player()
player_2 = Player()
