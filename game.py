from player import Player
from battlefield import Battlefield
from placement import Placement


class Game:

    def __init__(self):
        self.player = []
        

    def add_player(self,name):
        player = Player(name)
        self.player.append(player)

    def place_ship(self, name):
        Placement.place_ship(name)

