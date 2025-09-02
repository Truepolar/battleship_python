from player import Player
from battlefield import Battlefield
from placement import Placement


class Game:

    def __init__(self):
        self.player = Player()

    def place_ship(self, name):
        Placement.place_ship(name)

    def player_status(self):
        print("Player status :\n")
        print(f"Name : {self.player.name}")
        print(f"Health : {self.player.health}")
        print(f"Ships : {self.player.ship_list}")
