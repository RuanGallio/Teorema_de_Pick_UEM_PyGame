import sys
import pygame as pg

from data.main import main


global WINDOW_WIDTH, WINDOW_HEIGHT
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()
