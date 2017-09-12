#!/usr/bin/python
# -*- coding: utf-8 -*-
from bomberman import obj
import gameConfig
import time
import brick


class Bomb:
    # This class is making bomb & give time remaining in exploding bomb.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ''' set cordinates of bomb'''

    def set_coordinate(self):
        [x, y] = obj.get_pos()
        self.x = x
        self.y = y

    ''' return current coordinate of bomb in binary set '''

    def present_Coordiate_Bomb(self):
        return [self.x, self.y]

    '''return bomberman present coordinates '''

    def get_bomberman_Coordinate(self):
        return [obj.x, obj.y]

    ''' set bomb in bommberman current position '''

    def set_bomb(self):
        for x in range(self.x, self.x + 2):
            for y in range(self.y, self.y + 4):
                gameConfig.global_arr[x][y] = gameConfig.bomb_arr[x -
                                                                  self.x][y - self.y]

    ''' defines the timing in bomb from real time '''

    def start_counter(self, t):
        gameConfig.bomb_arr = [[str(t), str(t), str(t), str(t)], [
            str(t), str(t), str(t), str(t)]]

    '''defines the method during explosion in bomb'''

    def explosion(self):

        if (gameConfig.global_arr[self.x + 2][self.y] != 'X'):
            for i in range(4):
                gameConfig.global_arr[self.x + 2][i + self.y] = 'e'
                gameConfig.global_arr[self.x + 3][i + self.y] = 'e'

            # print("l")

        if (gameConfig.global_arr[self.x - 2][self.y] != 'X'):
            for i in range(4):
                gameConfig.global_arr[self.x - 2][i + self.y] = 'e'
                gameConfig.global_arr[self.x - 1][i + self.y] = 'e'

            # print("s")

        if (gameConfig.global_arr[self.x][self.y - 4] != 'X' and self.y > 2):
            for i in range(4):
                gameConfig.global_arr[self.x + 1][i + self.y - 4] = 'e'
                gameConfig.global_arr[self.x][i + self.y - 4] = 'e'

        if (gameConfig.global_arr[self.x][self.y + 4] != 'X'):
            for i in range(4):
                gameConfig.global_arr[self.x + 1][i + self.y + 4] = 'e'
                gameConfig.global_arr[self.x][i + self.y + 4] = 'e'

    '''defines the method after the  bomb explodes '''

    def explode(self):
        [x, y] = self.present_Coordiate_Bomb()
        for i in range(4):
            gameConfig.global_arr[x][i + y] = ' '
            gameConfig.global_arr[x + 1][i + y] = ' '

        for i in range(4):
            if (y < 3 or gameConfig.global_arr[x][y - 4] == 'X'):
                break
            if (gameConfig.global_arr[x][y - 4] == '%'):
                gameConfig.setbrick.remove([x, y - 4])
                obj.score += 20
            gameConfig.global_arr[x][i + y - 4] = ' '
            gameConfig.global_arr[x + 1][i + y - 4] = ' '

        for i in range(4):
            if (gameConfig.global_arr[x][y + 4] == 'X'):
                break
            if (gameConfig.global_arr[x][y + 4] == '%'):
                gameConfig.setbrick.remove([x, y + 4])
                obj.score += 20
            gameConfig.global_arr[x][i + y + 4] = ' '
            gameConfig.global_arr[x + 1][i + y + 4] = ' '

        for i in range(4):
            if (gameConfig.global_arr[x + 2][y] == 'X'):
                break
            if (gameConfig.global_arr[x + 2][y] == '%'):
                gameConfig.setbrick.remove([x + 2, y])
                obj.score += 20
            gameConfig.global_arr[x + 2][i + y] = ' '
            gameConfig.global_arr[x + 3][i + y] = ' '

        for i in range(4):
            if (gameConfig.global_arr[x - 2][y] == 'X'):
                break
            if (gameConfig.global_arr[x - 2][y] == '%'):
                gameConfig.setbrick.remove([x - 2, y])
                obj.score += 20
            gameConfig.global_arr[x - 2][i + y] = ' '
            gameConfig.global_arr[x - 1][i + y] = ' '

    def diffuse_bomb(self):
        for x in range(self.x, self.x + 2):
            for y in range(self.y, self.y + 4):
                gameConfig.global_arr[x][y] = ' '


bomb_plant = Bomb(obj.x, obj.y)
