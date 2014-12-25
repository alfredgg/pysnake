#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pysnake

class Snake(object):
    def __init__(self, game):
        self.body = [[0, 0]]
        self.color = (0, 255, 0)
        self.direction = pysnake.MOVE_STOP
        self.game = game
        self.stop = False

    def initialize(self):
        self.body = [None]
        self.body[0] = [self.game.grid[0]/2, self.game.grid[1]/2]
        self.direction = pysnake.MOVE_STOP
        self._stop = False

    def move(self):
        for position in reversed(xrange(1, len(self.body))):
            self.body[position] = self.body[position-1]
        px = self.body[0][0] + self.direction[0]
        py = self.body[0][1] + self.direction[1]
        px = px % self.game.grid[0]
        py = py % self.game.grid[1]
        self.body[0] = [px, py]

    def is_bitting(self):
        return self.body[0] in self.body[1:]

    def grow(self):
        self.body.extend(self.body[:1])

    def draw(self):
        for position in self.body:
            self.game.draw_rect(position, self.color)

    def eats(self, food):
        return self.body[0] == food.position