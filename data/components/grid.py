import pygame as pg
from data.prepare import *


class GridRect(pg.Rect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = WHITE


class Grid:
    def __init__(self, window_width, window_height, screen):
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen

    def draw(self):
        blockSize = 50
        dots = []
        for x in range(0, self.window_width, blockSize):
            for y in range(0, self.window_height, blockSize):
                dot = GridRect(x, y, blockSize, blockSize)
                pg.draw.circle(self.screen, dot.color, dot.center, 5)
                dots.append(dot)

        return dots
