from player import Player
from battlefield import Battlefield
from placement import place_ship


class Game:

    def __init__(self, player):
        self.player = player

    def place_ship(self, name, player):
        player = place_ship(name, player)

   
    def player_status(self):
        print("Player status :\n")
        print(f"Name : {self.player.name}")
        print(f"Health : {self.player.health}")
        print(f"Ships : {self.player.ship_list}")
