from ship_temp_adder import temp_column,temp_row

def collision_check(player, orientation,ship_length,coordinate,ship_placement_column,ship_placement_row,coordinate_list,collision_detection):
    
    
    i = 1
    if (orientation == 0):
        while i <= ship_length and collision_detection == False:
                for a_ship in player.ship_list:
                    for a_coord in a_ship.coordinate_list:
                        if coordinate == a_coord:
                            collision_detection = True
                            return collision_detection
                            break
        
                        temp_column(coordinate,ship_placement_column,ship_placement_row,coordinate_list,i)
                        i += 1

    elif (orientation == 1):
        while i <= ship_length and collision_detection == False:
                for a_ship in player.ship_list: 
                    for a_coord in a_ship.coordinate_list:
                        if coordinate == a_coord:
                            collision_detection = True
                            return collision_detection
                            break

                        temp_row(coordinate,ship_placement_column,ship_placement_row,coordinate_list,i)
                        i += 1
