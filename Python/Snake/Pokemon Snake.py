
import os
import random
import readchar

POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 3
VIDA_INICIAL_CHARIZARD = 80
VIDA_INICIAL_LUCARIO = 90
VIDA_INICIAL_BULBASUR = 75
VIDA_INICIAL_PIKACHU = 100

obstacle_definition = """\
############################
#                      #####
####     ########      #####
#####                #######
########      ####      ####
###      ######       ######
#             #####     ####
#########          #########
#####            #####    ##
####        ###   #       ##
####          ##   ##    ###
######    ####  ####      ##
#######              #######
####        ####       #####
#######        ######   ####
####     #####      ########
############################\
"""

my_position = [6, 2]
end_game = False
map_objects = [[5, 15], [15, 1], [23, 8]]
vida_charizard = 80
vida_lucario = 90
vida_bulbasur = 75
vida_pikachu = 100
obstacle_definition = [list(raw) for raw in obstacle_definition.split("\n")]
has_ganado = 0

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

print("Bienvenido Ash Ketchum")
input("PULSA PARA CONTINUAR...")
while not end_game and not has_ganado == 3:

    os.system("cls")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            object_in_cell = None
            trainer_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    trainer_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

                if trainer_in_cell:

                    if trainer_in_cell[POS_X] == 5 and trainer_in_cell[POS_Y] == 15:
                        pokemon = 1

                    elif trainer_in_cell[POS_X] == 15 and trainer_in_cell[POS_Y] == 1:
                        pokemon = 2

                    else:
                        pokemon = 3

                    os.system("cls")

                    if pokemon == 1:
                        print("Te haz encontrado con Charizard")
                        print("La batalla comienza")
                        input("Pulsa enter para continuar... ")
                        vida_pikachu = 100

                        while vida_pikachu != 0 and vida_charizard != 0:
                            ataque_charizard = random.randint(1, 3)
                            ataque_critico = random.randint(1, 5)

                            print("Turno de charizard")
                            ataquechari = "Charizard ataca con {}"

                            if ataque_charizard == 1:
                                if ataque_critico == 2:
                                    print(ataquechari.format("critico Mar Llamas (-22)"))
                                    vida_pikachu -= 22

                                elif ataque_critico != 2:
                                    print(ataquechari.format("Mar Llamas (-11)"))
                                    vida_pikachu -= 11

                            elif ataque_charizard == 2:
                                if ataque_critico == 2:
                                    print(ataquechari.format("critico Sequía (-24)"))
                                    vida_pikachu -= 24
                                elif ataque_critico != 2:
                                    print(ataquechari.format("Sequía (-12)"))
                                    vida_pikachu -= 12

                            elif ataque_charizard == 3:
                                if ataque_critico == 2:
                                    print(ataquechari.format("critico Poder Solar (-20)"))
                                    vida_pikachu -= 20

                                elif ataque_critico != 2:
                                    print(ataquechari.format("Poder Solar (-10)"))
                                    vida_pikachu -= 10

                            if vida_pikachu < 0:
                                vida_pikachu = 0
                            elif vida_charizard < 0:
                                vida_charizard = 0

                            barra_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
                            barra_de_vida_charizard = int(vida_charizard * 10 / VIDA_INICIAL_CHARIZARD)

                            print("La vida de pikachu es [{}] ({}/{})".format(barra_de_vida_pikachu * "*",
                                                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

                            print("La vida de charizard es [{}] ({}/{})".format(barra_de_vida_charizard * "*",
                                                                                vida_charizard, VIDA_INICIAL_CHARIZARD))

                            input("Pulsa para continuar... \n")
                            os.system("cls")

                            print("Turno de pikachu")
                            ataque_pikachu = None

                            while ataque_pikachu != "I" and ataque_pikachu != "G" and ataque_pikachu != "L" and \
                                    ataque_pikachu != "N":
                                ataque_pikachu = input("¿Qué ataca ataque deseas realizar? (I)mpactrueno, (G)ruñido, "
                                                       "(L)atigo, (N)ada: ")

                                ataque_critico = random.randint(1, 5)
                                ataque_pika = "Pikachu ataca con {}"

                                if ataque_pikachu == "I":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Impactrueno (-28)"))
                                        vida_charizard -= 28
                                    elif ataque_critico != 2:
                                        print(ataque_pika.format("Impactrueno (-14)"))
                                        vida_charizard -= 14

                                elif ataque_pikachu == "G":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Impactrueno (-24)"))
                                        vida_charizard -= 24
                                    elif ataque_critico != 2:
                                        print(ataque_pika.format("Gruñido (-12)"))
                                        vida_charizard -= 12

                                elif ataque_pikachu == "L":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Latigo (-20)"))
                                        vida_charizard -= 20

                                    elif ataque_critico != 2:
                                        print(ataque_pika.format(" Latigo (-10)"))
                                        vida_charizard -= 10

                                elif ataque_pikachu == "N":
                                    print("Pikachu no hace nada")

                                if vida_pikachu < 0:
                                    vida_pikachu = 0
                                elif vida_charizard < 0:
                                    vida_charizard = 0

                                barra_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
                                barra_de_vida_charizard = int(vida_charizard * 10 / VIDA_INICIAL_CHARIZARD)

                                print("La vida de pikachu es [{}] ({}/{})".format(barra_de_vida_pikachu * "*",
                                                                                  vida_pikachu,
                                                                                  VIDA_INICIAL_PIKACHU))

                                print("La vida de charizard es [{}] ({}/{})".format(barra_de_vida_charizard * "*",
                                                                                    vida_charizard,
                                                                                    VIDA_INICIAL_CHARIZARD))

                                input("Pulsa enter para continuar....")

                                os.system("cls")

                        if vida_pikachu > vida_charizard:
                            os.system("cls")
                            print("Pikachu gana")
                            has_ganado += 1
                            map_objects.remove(trainer_in_cell)

                        else:
                            os.system("cls")
                            print("Charizard gana")
                            if input("Deseas revivir a pikachu (S/N)") == "N":
                                end_game = True
                            else:
                                print("Pikachu ha sido revivido")

                    elif pokemon == 2:
                        print("Te haz encontrado con Lucario")
                        print("La batalla comienza")
                        input("Pulsa enter para continuar... ")
                        vida_pikachu = 100

                        print("Turno de Lucario")
                        ataqueluca = "Lucario ataca con {}"

                        while vida_pikachu != 0 and vida_lucario != 0:
                            ataque_lucario = random.randint(1, 3)
                            ataque_critico = random.randint(1, 5)

                            if ataque_lucario == 1:
                                if ataque_critico == 2:
                                    print(ataqueluca.format(" critico Mar Aguante Endure (-18)"))
                                    vida_pikachu -= 18
                                elif ataque_critico != 2:
                                    print(ataqueluca.format("Mar Aguante Endure (-9)"))
                                    vida_pikachu -= 9
                            elif ataque_lucario == 2:
                                if ataque_critico == 2:
                                    print(ataqueluca.format("critico Mar Bofetón Lodo Mud-Slap (-24)"))
                                    vida_pikachu -= 24
                                elif ataque_critico != 2:
                                    print(ataqueluca.format("Mar Bofetón Lodo Mud-Slap (-12)"))
                                    vida_pikachu -= 12

                            elif ataque_lucario == 3:
                                if ataque_critico == 2:
                                    print(ataqueluca.format("critico Golpe Bis Dual Chop (-22)"))
                                    vida_pikachu -= 22

                                elif ataque_critico != 2:
                                    print(ataqueluca.format("Golpe Bis Dual Chop (-11)"))
                                    vida_pikachu -= 11

                            barra_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
                            barra_de_vida_lucario = int(vida_lucario * 10 / VIDA_INICIAL_LUCARIO)

                            if vida_pikachu < 0:
                                vida_pikachu = 0
                            elif vida_lucario < 0:
                                vida_lucario = 0

                            print("La vida de pikachu es [{}] ({}/{})".format(barra_de_vida_pikachu * "*", vida_pikachu,
                                                                              VIDA_INICIAL_PIKACHU))

                            print("La vida de lucario es [{}] ({}/{})".format(barra_de_vida_lucario * "*", vida_lucario,
                                                                              VIDA_INICIAL_LUCARIO))

                            input("Pulsa para continuar... \n")
                            os.system("cls")

                            print("Turno de pikachu")
                            ataque_pikachu = None

                            while ataque_pikachu != "I" and ataque_pikachu != "G" and ataque_pikachu != "L" and \
                                    ataque_pikachu != "N":
                                ataque_pikachu = input("¿Qué ataca ataque deseas realizar? (I)mpactrueno, (G)ruñido, "
                                                       "(L)atigo, (N)ada: ")

                                ataque_critico = random.randint(1, 5)
                                ataque_pika = "Pikachu ataca con {}"

                                if ataque_pikachu == "I":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Impactrueno (-28)"))
                                        vida_lucario -= 28
                                    elif ataque_critico != 2:
                                        print(ataque_pika.format("Impactrueno (-14)"))
                                        vida_lucario -= 14

                                elif ataque_pikachu == "G":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Impactrueno (-24)"))
                                        vida_lucario -= 24
                                    elif ataque_critico != 2:
                                        print(ataque_pika.format("Gruñido (-12)"))
                                        vida_lucario -= 12

                                elif ataque_pikachu == "L":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Latigo (-20)"))
                                        vida_lucario -= 20

                                    elif ataque_critico != 2:
                                        print(ataque_pika.format(" Latigo (-10)"))
                                        vida_lucario -= 10

                                elif ataque_pikachu == "N":
                                    print("Pikachu no hace nada")

                            if vida_pikachu < 0:
                                vida_pikachu = 0
                            elif vida_lucario < 0:
                                vida_lucario = 0

                            barra_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
                            barra_de_vida_lucario = int(vida_lucario * 10 / VIDA_INICIAL_LUCARIO)

                            print("La vida de pikachu es [{}] ({}/{})".format(barra_de_vida_pikachu * "*",
                                                                              vida_pikachu,
                                                                              VIDA_INICIAL_PIKACHU))

                            print("La vida de lucario es [{}] ({}/{})".format(barra_de_vida_lucario * "*",
                                                                              vida_lucario,
                                                                              VIDA_INICIAL_LUCARIO))

                            input("Pulsa para continuar... \n")
                            os.system("cls")

                        if vida_pikachu > vida_lucario:
                            os.system("cls")
                            print("Pikachu gana")
                            has_ganado += 1
                            map_objects.remove(trainer_in_cell)

                        else:
                            os.system("cls")
                            print("Lucario gana")
                            if input("Deseas revivir a pikachu (S/N): ") == "N":
                                end_game = True
                            else:
                                print("Pikachu ha sido revivido")

                    elif pokemon == 3:
                        print("Te haz encontrado con Bulbasur")
                        print("La batalla comienza")
                        input("Pulsa enter para continuar... ")
                        vida_pikachu = 100

                        print("Turno de Bulbasur")

                        while vida_pikachu != 0 and vida_bulbasur != 0:
                            ataque_bulbasur = random.randint(1, 3)
                            ataque_critico = random.randint(1, 5)
                            ataquebulb = "Bulbasur ataca con {}"

                            if ataque_bulbasur == 1:
                                if ataque_critico == 2:
                                    print(ataquebulb.format("critico Placaje (-22)"))
                                    vida_pikachu -= 16
                                elif ataque_critico != 2:
                                    print(ataquebulb.format("Placaje (-11)"))
                                    vida_pikachu -= 11
                            elif ataque_bulbasur == 2:
                                if ataque_critico == 2:
                                    print(ataquebulb.format("critico Gruñido (-24)"))
                                    vida_pikachu -= 24
                                elif ataque_critico != 2:
                                    print("Bulbasur ataca con Gruñido (-12)")
                                    vida_pikachu -= 12
                            elif ataque_bulbasur == 3:
                                if ataque_critico == 2:
                                    print(ataquebulb.format("critico Placaje (-20)"))
                                    vida_pikachu -= 20
                                elif ataque_critico != 2:
                                    print("Bulbasur ataca con Somnifero (-10)")
                                    vida_pikachu -= 10

                            barra_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
                            barra_de_vida_bulbasur = int(vida_bulbasur * 10 / VIDA_INICIAL_BULBASUR)

                            if vida_pikachu < 0:
                                vida_pikachu = 0
                            elif vida_bulbasur < 0:
                                vida_bulbasur = 0

                            print("La vida de pikachu es [{}] ({}/{})".format(barra_de_vida_pikachu * "*", vida_pikachu,
                                                                              VIDA_INICIAL_PIKACHU))

                            print("La vida de bulbasur es [{}] ({}/{})".format(barra_de_vida_bulbasur * "*",
                                                                               vida_bulbasur,  VIDA_INICIAL_BULBASUR))

                            input("Pulsa para continuar... \n")
                            os.system("cls")

                            print("Turno de pikachu")
                            ataque_pikachu = None

                            while ataque_pikachu != "I" and ataque_pikachu != "G" and ataque_pikachu != "L" and \
                                    ataque_pikachu != "N":
                                ataque_pikachu = input("¿Qué ataca ataque deseas realizar? (I)mpactrueno, (G)ruñido, "
                                                       "(L)atigo, (N)ada: ")

                                ataque_critico = random.randint(1, 5)
                                ataque_pika = "Pikachu ataca con {}"

                                if ataque_pikachu == "I":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Impactrueno (-28)"))
                                        vida_bulbasur -= 28
                                    elif ataque_critico != 2:
                                        print(ataque_pika.format("Impactrueno (-14)"))
                                        vida_bulbasur -= 14

                                elif ataque_pikachu == "G":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Impactrueno (-24)"))
                                        vida_bulbasur -= 24
                                    elif ataque_critico != 2:
                                        print(ataque_pika.format("Gruñido (-12)"))
                                        vida_bulbasur -= 12

                                elif ataque_pikachu == "L":
                                    if ataque_critico == 2:
                                        print(ataque_pika.format("critico Latigo (-20)"))
                                        vida_bulbasur -= 20

                                    elif ataque_critico != 2:
                                        print(ataque_pika.format(" Latigo (-10)"))
                                        vida_bulbasur -= 10

                                elif ataque_pikachu == "N":
                                    print("Pikachu no hace nada")

                                if vida_pikachu < 0:
                                    vida_pikachu = 0
                                elif vida_bulbasur < 0:
                                    vida_bulbasur = 0

                                barra_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
                                barra_de_vida_charizard = int(vida_bulbasur * 10 / VIDA_INICIAL_BULBASUR)

                                print("La vida de pikachu es [{}] ({}/{})".format(barra_de_vida_pikachu * "*",
                                                                                  vida_pikachu,
                                                                                  VIDA_INICIAL_PIKACHU))

                                print("La vida de bulbasur es [{}] ({}/{})".format(barra_de_vida_bulbasur * "*",
                                                                                   vida_bulbasur,
                                                                                   VIDA_INICIAL_BULBASUR))

                                input("Pulsa para continuar... \n")
                                os.system("cls")

                        if vida_pikachu > vida_bulbasur:
                            os.system("cls")
                            print("Pikachu gana")
                            has_ganado += 1
                            map_objects.remove(trainer_in_cell)

                        else:
                            os.system("cls")
                            print("Lucario gana")
                            if input("Deseas revivir a pikachu (S/N): ") == "N":
                                end_game = True
                            else:
                                print("Pikachu ha sido revivido")

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    direction = readchar.readchar().decode()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        new_position = [my_position[POS_X] - 1 % MAP_WIDTH, (my_position[POS_Y])]

    elif direction == "d":
        new_position = [my_position[POS_X] + 1 % MAP_WIDTH, (my_position[POS_Y])]

    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

if end_game:
    os.system("cls")
    print("¡Pikachu a muerto!")

if has_ganado == 3:
    os.system("cls")
    print("Felicidades Entrenador, el juego ha sido completado. Una pasada el curso y las horitas que le he metido ☺")
