from ship import Ship
from player import Player

#cuz i laze ships will only be 3 long


class Placement:

    def __init__(self):
        pass

    @staticmethod
    def place_ship(name):
        
##HOW MANY SHIPS

        print("How many ships would you like to play with? (3-5)")
        number_of_ships = int(input())
        
        ship_counter = 1

##START LOOP AND ASKING VERT OR HORI

        while ship_counter <= number_of_ships:
            ship_length = 0
            row_coordinate = []
            column_coordinate = []
            check = True
            while(check == True): 
                print("Would you like horizontal or vertical placement? Enter 0 for horizontal and 1 for vertical\n")
                orientation = int(input())
                if (orientation == 0 or orientation == 1):
                    check = False
                else:
                    print("------------ invalid input, try again ------------")

##ASKING FOR ROW AND COLUMN

            check2 = True
            while(check2 == True): 
                print("Enter the column number of the desired ship placement (1-10)\n")
                ship_placement_column = int(input())
                print("Enter the row number of the desired ship placement (1-10)\n")
                ship_placement_row = int(input())
                if 0<ship_placement_column<11 and 0<ship_placement_row<11:
                    check2 = False

                else:
                    print("------------ invalid input, try again ------------")

##ASKING FOR LENGTH

            while(ship_length <= 2 or ship_length >= 6):
                print("Enter the desired ship length (3-5)\n")
                ship_length = input()
                ship_length = int(ship_length)

                i = 1

 ## THE 2 CHUNKS UNDER IS PROCESSING FOR PLACEMENT

            if (orientation == 0):
                while i <= ship_length:
                    temp_row = i + ship_placement_row -1
                    row_coordinate.append(temp_row)
                    column_coordinate.append(ship_placement_column)
                    check2 = False
                    i += 1
                    
            elif (orientation == 1):
                while i <= ship_length:
                    temp_column = i + ship_placement_column -1
                    row_coordinate.append(temp_column)
                    column_coordinate.append(ship_placement_column)
                    check2 = False
                    i += 1

##APPEND TO OBJECT LIST

            else:
                check2 = True
            print(f"Ship {i}, \n row :{row_coordinate} \n column{column_coordinate}")
            ship = Ship(True , row_coordinate , column_coordinate)
            player = Player(name)
            player.add_ship(ship)
            ship_counter += 1
        


