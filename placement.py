from jason_dumps import json_dumps
from ship import Ship
from player import Player
from collision_check import collision_check
from ship_temp_adder import temp_row,temp_column

def place_ship(name, player):
        
##HOW MANY SHIPS

        print("How many ships would you like to play with? (3-5)")
        number_of_ships = int(input())
        coordinate_list = []
        
        ship_counter = 1
        health = 0

##START LOOP AND ASKING VERT OR HORI

        while ship_counter <= number_of_ships:
            ship = Ship(True)
            ship_length = 0
            coordinate = []
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
                ship_length = int(input())

            health = health + ship_length
            print("pass check 1")

 ## THE 2 LINES UNDER IS PROCESSING FOR PLACEMENT AND COLLISION DETECTION
 ## COLUMNS ARE X, ROWS ARE Y 

            if ship_counter == 1:
                i = 1
                if (orientation == 0):
                    while i <= ship_length:
                        temp_column(coordinate,ship_placement_column,ship_placement_row,coordinate_list,i)
                        i += 1

                elif (orientation == 1): 
                    while i <= ship_length:
                        temp_row(coordinate,ship_placement_column,ship_placement_row,coordinate_list,i)
                        i += 1

            else:
                collision_detection = False
                collision_check(player,orientation,ship_length,coordinate,ship_placement_column,ship_placement_row,coordinate_list,collision_detection)

            print("pass check")
##APPEND TO OBJECT LIST OR DROP OBJ
        
            if collision_detection == True: ##collision detection broke for 1st iteration
                check = True

            else:
                print(f"Ship , \n coordinates: {player.ship_list} \n")
                ship = Ship(True , coordinate_list)
                player.add_ship(ship)
                player.health = health

                print(json_dumps(player))
                print(json_dumps(ship))
                
                ship_counter += 1
        return player

