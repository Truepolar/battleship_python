

def collision_check(player, orientation,ship_length,coordinate,ship_placement_column,ship_placement_row,coordinate_list,collision_detection):
    i = 1
    if (orientation == 0):
        while collision_detection == False:
            while i <= ship_length:
                for a_ship in player.ship_list:  ##problems
                    for a_coord in a_ship.coordinate_list:
                        if coordinate == a_coord:
                            collision_detection = True
                            return collision_detection
                            break
        
                        temp_column = i + ship_placement_column -1
                        coordinate.append(temp_column)
                        coordinate.append(ship_placement_row)
                        coordinate_list.append(coordinate)
                        i += 1

    elif (orientation == 1):
        while collision_detection == False:
            while i <= ship_length:
                for a_ship in player.ship_list:  ##problems
                    for a_coord in a_ship.coordinate_list:
                        if coordinate == a_coord:
                            collision_detection = True
                            return collision_detection
                            break

                    temp_row = i + ship_placement_row -1
                    coordinate.append(ship_placement_column)
                    coordinate.append(temp_row)
                    coordinate_list.append(coordinate)
                    i += 1
