class BattleField:

    
   def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        
class Player :

    def __init__(self, name):
        self.name   

class Game:

    def __init__(self):
        self.battle_field = None
        self.players = [] # list of Player object

    def start(self):
        self.init_battle_field()
        

    def _init_battle_field(self):
        self.battle_field = BattleField(10, 10)

    def add_player(self, name:str):
        player = Player(name)
        
        self.players.append(Player(name))

   


if __name__ == "__main__":
    # This code will only run when my_module.py is executed directly
   game = Game()

   game.start()
   game.add_player("Amy")
   game.add_player("Bob")




 