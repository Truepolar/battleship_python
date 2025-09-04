

def temp_column(coordinate,ship_placement_column,ship_placement_row,coordinate_list,i):
        coordinate = []
        temp_column = i + ship_placement_column -1
        coordinate.append(temp_column)
        coordinate.append(ship_placement_row)
        coordinate_list.append(coordinate)
        
        return coordinate_list

def temp_row(coordinate,ship_placement_column,ship_placement_row,coordinate_list,i):
        coordinate = []
        temp_row = i + ship_placement_row -1
        coordinate.append(ship_placement_column)
        coordinate.append(temp_row)
        coordinate_list.append(coordinate)
    
        return coordinate_list