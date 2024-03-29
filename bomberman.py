#!/usr/bin/python
# -*- coding: utf-8 -*-
from board import *
from gameConfig import *
from person import Person


class Bomberman(Person):  # inherit class of Person
    # This class is making Bomberman & checking if he dies with the bomb, enemy
    # Also remove enemy at previous pos and build at new position

    def __init__(self, x, y, score, lives):
        Person.__init__(self, x, y)
        self.score = score
        self.lives = lives
        self.position = [2, 2]
        self.ocuupied = ['3', '2', '1', '0','%', '@', 'B','X']

    ''' return bomb planting position '''

    def get_Pos_planter(self):
        return [self.x, self.y]

    ''' remove bomberman from previous position '''

    def remove(self):
        [x, y] = self.get_pos()
        for k in range(4):
            global_arr[x][k + y] = ' '
            global_arr[x + 1][k + y] = ' '

    ''' set the bomberman in cuurrent position '''

    def curr(self):
        [x, y] = self.get_pos()
        for k in range(4):
            global_arr[x][k + y] = ar[0][k]
            global_arr[x + 1][k + y] = ar[1][k]

    ''' decresse in life of bommberman'''

    def hanged(self):
        self.lives = self.lives - 1

    ''' check if bomberman is killed by bomb'''

    def hanged_bomber(self, present_Coordiate_Bomb):
        [p, q] = self.get_pos()
        [g, h] = present_Coordiate_Bomb
        if p == g and q == h:
            self.hanged()
            return True
        if p == g and q != h:
            if abs(q - h) <= 4:
                self.hanged()
                return True
        if q == h and g != p:
            if abs(p - g) <= 2:
                self.hanged()
                return True
        return False


obj = Bomberman(2, 2, 0, 3)
