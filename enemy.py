#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from person import Person
from gameConfig import global_arr


class Enemy(Person):  # inherit class of Person

    # This Class is making Enemy randomly

    def __init__(self):
        self.lives = 1
        self.shape = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]
        self.position = [7, 2]
        self.ocuupied = ['3', '2', '1', '0','E', '%', '@', 'B','X']

    ''' remove enemy from previous random position'''

    def remove_Enemy(self):
        [x, y] = self.get_pos()
        for k in range(4):
            global_arr[x + 1][k + y] = ' '
            global_arr[x][k + y] = ' '

    ''' make the enemy in current random position '''

    def curr_Enemy(self):
        [x, y] = self.get_pos()
        for i in range(4):
            global_arr[x][i + y] = self.shape[0][i]
            global_arr[x + 1][i + y] = self.shape[1][i]

    def check_murder(self, p, q, x, y, planter):
        if (p == x and q == y):
            planter.hanged()

            # print("gothanged")

            return True
        else:
            return False

    def destroy(self):
        self.lives = self.lives - 1

    ''' check enemy killed by bomb'''

    def hanged_enemy(self, presentCoordiateBomb):
        [p, q] = self.get_pos()
        [g, h] = presentCoordiateBomb
        if(p == q and q == h):
            return True
        if p == g and q != h:
            if abs(q - h) <= 4:
                self.destroy()
                return True
        if q == h and g != p:
            if abs(p - g) <= 2:
                self.destroy()
                return True
        return False
