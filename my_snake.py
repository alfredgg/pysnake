#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.locals import K_UP, K_LEFT, K_RIGHT, K_DOWN, K_SPACE
import pysnake

class SnakeGame(pysnake.Game):
    def __init__(self):
        self.snake = pysnake.Snake(self)
        self.food = pysnake.Food(self)

    def setup(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def keypressed(self, key):
        pass

if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()