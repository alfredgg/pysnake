#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Food(object):
    def __init__(self, game):
        self.position = None
        self.color = (255, 0, 0)
        self.game = game

    def draw(self):
        if self.position:
            self.game.draw_rect(self.position, self.color)

    def generate(self, forbidden_positions = None):
        forbidden = [] if not forbidden_positions else forbidden_positions
        new_position = None
        while not new_position or new_position in forbidden:
            new_position = [randint(0, self.game.grid[0]-1), randint(0, self.game.grid[1]-1)]
        self.position = new_position 