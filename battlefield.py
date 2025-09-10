import numpy as np

class Battlefield:

    def __init__(self, grid_square):
        self.grid_square = grid_square

    def create_field(self,dimension):
        for r in range(dimension):
            for c in range(dimension):
                np.append(self.grid_square,0,axis=0)






Battlefield.create_field(10)

