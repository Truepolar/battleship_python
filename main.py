from game import Game
from player import Player

print("Hello, please input your player name: ")
name = input()

my_game = Game()
my_game.add_player(name)
my_game.place_ship(name)

print(my_game.player[0].name)
