import sys
from board import *
from gameConfig import *
import gameConfig
from bomberman import *
from getch import *
from bomb import bomb_plant
import brick
import os
import time
import random
from enemy import Enemy
from termcolor import colored

# This is the main game file where game is running &print game score & lives of bomberman
# Update bomb, enemies etc.
# print board and bricks in board


class Game:
    def __init__(self, level):
        self.level = level


Game_obj = Game(gameConfig.level)

count = 1
flag = 0
tr = 0
brick_obj = brick.Brick(Game_obj)


def print_board():
    global flag1
    if(obj.lives <= 0):
        loose()
    # os.system('tput reset')
    # if(len(enemybin)==0):
    # 	youwin()
    print(colored("\t\t\t\t    BOMBERMAN \t\t\t\t\t", "green", attrs=["bold"]))
    bp.make_board()
    brick_obj.entity_build()
    obj.curr()
    for i in bomb_bin:
        i.set_bomb()

    for i in enemybin:
        i.curr_Enemy()
    # bricks.Bricks()
    check_Game_Score()
    for x in range(Length):
        for y in range(Width):
            if global_arr[x][y] == 'E':
                print(colored(global_arr[x][y], "red", attrs=["bold"]), end="")
            elif global_arr[x][y].isdigit():
                print(
                    colored(
                        global_arr[x][y],
                        "yellow",
                        attrs=["bold"]),
                    end="")
            elif global_arr[x][y] == '%' or global_arr[x][y] == 'B':
                print(
                    colored(
                        global_arr[x][y],
                        "yellow",
                        attrs=[
                            "bold",
                            "dark"]),
                    end="")
            elif (global_arr[x][y] == 'e'):
                print(
                    colored(
                        global_arr[x][y],
                        "green",
                        attrs=[
                            "bold",
                            "dark"]),
                    end="")
            elif (global_arr[x][y] == 'P'):
                print(
                    colored(
                        global_arr[x][y],
                        "blue",
                        attrs=[
                            "bold",
                            "dark"]),
                    end="")
            else:
                print(global_arr[x][y], end="")
        print()
        # print("".join(str(global_arr[x][y]) for y in range(Width)))
    print(
        colored(
            "Lives", "blue"), colored(
            obj.lives, "blue"), "   ", colored(
                "Score", "green"), colored(
                    obj.score, "green"))
    p = brick_obj.get_level()
    print(colored("Level", "green"), colored(p - 1, "yellow"))


def enemy_update():
    # print(gameConfig.level)
    if not len(enemybin):
        # brick_obj.set_level()
        os.system('tput reset')
        q = brick_obj.get_level()
        # print(q)
        getch.Set_Frame_rate(q)  # Speed of enemy increase in every level
        if(q <= 5 and q > 0):
            print(
                colored(
                    "Level", 'green'), ' ', colored(
                    q, 'yellow'))
            time.sleep(1)
            levelup()
        if q > 5:
            you_win()

    for entity in enemybin:
        [r, t] = entity.get_pos()
        [p, q] = obj.get_pos()
        # print(r,t)
        if(entity.check_murder(p, q, r, t, obj)):
            obj.set_Pos(2, 2)
            obj.curr()
        entity.remove_Enemy()
        locomotion = random.randint(0, 3)
        if locomotion == 1:
            entity.left_Move()
        elif locomotion == 2:
            entity.right_Move()
        elif locomotion == 3:
            entity.up_Move()
        else:
            entity.down_Move()

        entity.curr_Enemy()


def levelup():
    brick_obj.Enemymade = True
    brick_obj.Wallmade = True
    getchar = getch
    bp.make_board()
    brick_obj.entity_build()
    for k in range(len(enemybin2)):
        enemybin.append(Enemy())
        enemybin[k].set_Pos(enemybin2[k][0], enemybin2[k][1])
    # print(len(enemybin2))


for k in range(len(enemybin2)):
    enemybin.append(Enemy())
    enemybin[k].set_Pos(enemybin2[k][0], enemybin2[k][1])


def check_Game_Score():
    for entity in bomb_bin:
        explode_time = 3 + tr - int(time.time())
        if(explode_time >= 0):
            bomb_plant.start_counter(explode_time - 1)
            if(explode_time < 1):
                bomb_plant.start_counter('B')
                bomb_plant.explosion()
        elif(explode_time < 0):
            bomb_plant.explode()
            if(obj.hanged_bomber(entity.present_Coordiate_Bomb())):
                obj.set_Pos(2, 2)
                obj.curr()
            for j in enemybin:
                if(j.hanged_enemy(entity.present_Coordiate_Bomb())):
                    enemybin.remove(j)
                    obj.score += 100
            del bomb_bin[:]


def loose():
    count = 0
    print(colored("!!!!!! GAME OVER !!!!!!", 'red'))
    sys.exit()


def you_win():
    count = 0
    print(colored("!! -_- ^_^ You Win -_- ^_^ !!", 'green'))
    sys.exit()


while(count != 0):
    enemy_update()
    print_board()
    ch = getch()
    if(ch == 'q'):
        count = 0
    elif(ch == 'w'):
        obj.remove()
        obj.up_Move()
        obj.curr()

    elif(ch == 's'):
        obj.remove()
        obj.down_Move()
        obj.curr()

    elif(ch == 'a'):
        obj.remove()
        obj.left_Move()
        obj.curr()

    elif(ch == 'd'):
        obj.remove()
        obj.right_Move()
        obj.curr()

    elif(ch == 'b'):
        if(len(bomb_bin) == 0):
            bomb_bin.append(bomb_plant)
            bomb_bin[0].set_coordinate()
            tr = int(time.time())

    os.system('clear')
