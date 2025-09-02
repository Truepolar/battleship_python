from ship import Ship
from player import Player

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
                ship_length = input()
                ship_length = int(ship_length)
                

                i = 1
            health = health + ship_length

 ## THE 2 CHUNKS UNDER IS PROCESSING FOR PLACEMENT AND COLLISION DETECTION
 ## COLUMNS ARE X, ROWS ARE Y 

            if (orientation == 0):
                collion_detection = False
                while collion_detection == False:
                    while i <= ship_length:
                        for other_coordinates in player.ship_list.coordinates:
                            if coordinate == other_coordinates:
                                collion_detection = True
        
                        temp_column = i + ship_placement_column -1
                        coordinate.append(temp_column)
                        coordinate.append(ship_placement_row)
                        coordinate_list.append(coordinate)
                        i += 1
                    

                
                    
            elif (orientation == 1):
                while i <= ship_length:
                    for other_coordinates in player.ship_list.coordinate_list:
                            if coordinate == other_coordinates:
                                collion_detection = True

                    temp_row = i + ship_placement_row -1
                    coordinate.append(ship_placement_column)
                    coordinate.append(temp_row)
                    coordinate_list.append(coordinate)
                    i += 1

##APPEND TO OBJECT LIST

            else:
                check2 = True

        
            print(f"Ship {i}, \n coordinates: {player.ship_list.coordinate_list} \n")
            ship = Ship(True , coordinate_list)
            player.add_ship(ship)
            player.health = health
            print("OBJECT STATUS : \n")
            print(player.health)
            print(player)
            
            ship_counter += 1
        return player

