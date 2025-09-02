from player import Player
from battlefield import Battlefield
from placement import place_ship


class Game:

    def __init__(self, player):
        self.player = player

    def place_ship(self, name, player):
        player = place_ship(name, player)

    def player_status(self, player):
        print("Player status :\n")
        print(f"Name : {player.name}")
        print(f"Health : {player.health}")
        print(f"Ships : {player.ship_list}")
