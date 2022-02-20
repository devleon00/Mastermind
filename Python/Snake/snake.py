# Snake
import readchar
import os
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 40
MAP_HEIGHT = 15

obstacles = """"\
###############################################
#####       ##                         ######## 
####    ###  ##   ######      ###         #####
######  ###   ###         ###          ########
######                 #########          #####
####   ####       ######     #  ###         ###
#####       ##                       ##   #####
####    ###  ##   ######      ###         #####
######  ###   ###         ###          ########
######     ##   ###            ###         ####
#    ####            #######      ###         #
####    ####  #   ######      ###         #####
######  ###   ###         ###          ########
    ##                 #########          #####
###     #####     ########      ####         ##
#    ####          ####   ####   ###       ####
##         #######     ####             ##  ###
##   ##    ###########      ####          #####
###############################################\
"""

my_position = [6, 3]
tail_length = 0
map_objects = []
tail = []

end_game = False

# Create obstacles map
obstacles = [list(row) for row in obstacles.split("\n")]

# Main loop
while not end_game:
    os.system("cls")

    while len(map_objects) < 8:
        coor_to_add = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
        if coor_to_add not in map_objects and coor_to_add != my_position and obstacles[coor_to_add[POS_Y]][coor_to_add[POS_X]] != "#":
            map_objects.append(coor_to_add)

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    object_in_cell = map_object
                    char_to_draw = " *"

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True

            if obstacles[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    if end_game:
        print("GAME OVER!")

    direction = readchar.readchar().decode()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, (my_position[POS_Y])]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, (my_position[POS_Y])]

    if new_position:
        if obstacles[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

    elif direction == "q":
        end_game = True
