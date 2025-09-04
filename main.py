from game import Game
from player import Player
from jason_dumps import json_dumps

print("Hello, please input your player name: ")
name = input()

player = Player(name)
print(player.name)
my_game = Game(player)

my_game.place_ship(name, player) #object
my_game.player_status()


