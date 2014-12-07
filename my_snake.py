#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.locals import K_UP, K_LEFT, K_RIGHT, K_DOWN, K_SPACE
import pysnake

class SnakeGame(pysnake.Game):
    def __init__(self):
        self.snake = pysnake.Snake(self)
        self.food = pysnake.Food(self)
        self.points = 0
        self.stop = False

    def setup(self):
        self.background(0,0,0)
        self.size(600, 300)
        self.grid(20, 10)
        self.update_ratio = 100
        self.snake.initialize()
        self.food.generate(self.snake.body)
        self.set_title("SNAKE")

    def update(self):
        if self.stop:
            return
        self.snake.move()
        if self.snake.eats(self.food):
            self.snake.grow()
            self.food.generate(self.snake.body)
            self.points += 1
            self.set_title("SNAKE " + str(self.points))
        elif self.snake.is_bitting():
            self.set_title("GAMEOVER " + str(self.points))
            self.points = 0
            self.stop = True

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def keypressed(self, key):
        if key == K_UP:
            self.snake.direction = pysnake.MOVE_UP
        elif key == K_DOWN:
            self.snake.direction = pysnake.MOVE_DOWN
        elif key == K_LEFT:
            self.snake.direction = pysnake.MOVE_LEFT
        elif key == K_RIGHT:
            self.snake.direction = pysnake.MOVE_RIGHT
        elif key == K_SPACE:
            self.snake.initialize()
            self.food.generate(self.snake.body)
            self.stop = False
            self.set_title("SNAKE")

if __name__ == '__main__':
    snake_game = SnakeGame()
    snake_game.run()