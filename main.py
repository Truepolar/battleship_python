from game import Game
from player import Player

print("Hello, please input your player name: ")
name = input()

player = Player()
my_game = Game(player)

my_game.place_ship(name, player) #object
my_game.player_status(player)

