import pygame as pg
import sys
from data.prepare import *
from data.components.grid import Grid, GridRect


class Polygon():
    def __init__(self, vertices, color, screen) -> None:
        self.screen = screen
        self.vertices = vertices
        self.color = color

    def draw(self) -> None:
        polygon = pg.draw.polygon(self.screen, self.color, [
            dot.center for dot in self.vertices], 3)
        self.polygon = polygon

    def check_if_dots_form_polygon(dots: GridRect) -> bool:
        """
        Checks if the dots form a polygon by checking if all the dots are on the same line (or there are less than 3 dots)

        Args:
            dots (GridRect): The dots to check

        Returns:
            bool: True if the are more then three non consecutive dots, False otherwise

        """
        if len(dots) < 3:
            return False

        dots_center = [dot.center for dot in dots.values()]

        return not all(dot[0] == dots_center[0][0] or dot[1] ==
                       dots_center[0][1] for dot in dots_center)

    def isInside(self, dot):
        return self.polygon.collidepoint(dot)

    def colorInsideDots(self, dots):
        for dot in dots:
            if self.isInside(dot.center):
                dot.color = "green"
                pg.draw.circle(self.screen, dot.color, dot.center, 5)
