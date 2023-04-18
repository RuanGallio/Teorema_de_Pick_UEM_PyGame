import pygame as pg
import sys

from data.components.grid import Grid
from data.components.polygon import Polygon
from data.prepare import *
pg.init()


def main():
    running = True
    can_select = True

    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pg.time.Clock()
    screen.fill(BLACK)

    grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, screen)
    grid_dots = grid.draw()

    selected = dict()
    num_selected = 0

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and can_select:
                mouse_position = pg.mouse.get_pos()
                for dot in grid_dots:
                    if dot.collidepoint(mouse_position):
                        if dot not in selected.values():
                            dot.color = RED
                            selected[num_selected] = dot
                            num_selected += 1
                            pg.draw.circle(screen, dot.color, dot.center, 5)
                        else:
                            if Polygon.check_if_dots_form_polygon(selected):
                                polygon = Polygon(list(selected.values()),
                                                  "blue", screen)
                                polygon.draw()
                                not_selected = [
                                    i for i in grid_dots if i not in selected.values()]
                                polygon.colorInsideDots(not_selected)

        pg.display.update()


if __name__ == '__main__':
    main()
