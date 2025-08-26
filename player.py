class Player:

    def __init__(self, name, health=None, ship_list=None):
        self.name = name
        self.health = health
        self.ship_list = ship_list
        self.ship_list = []
    
    def add_ship (self, ship_object):
        self.ship_list.append(ship_object)