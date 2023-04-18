import pygame
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


""" 
    TODO: Only let polygon be drawn if it is closed and more than 3 dots are selected
    TODO: Fix bug where bottom and left dots on the front of the polygon are not as inside as they should be
    TODO: Class for vertices
    TODO: Rest of the game
"""


def main():
    selected = []

    global screen, clock
    can_select = True
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(BLACK)

    drawGrid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check if left mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and can_select:
                pos = pygame.mouse.get_pos()
                # Check if mouse is inside a rectangle
                for dot in dots:

                    if dot.collidepoint(pos):

                        if dot not in selected:
                            selected.append(dot)
                            dot.color = RED
                            pygame.draw.circle(
                                screen, dot.color, dot.center, 5)

                        else:
                            poly = Polygon(
                                list(i.center for i in selected), "blue")
                            poly.draw()
                            not_selected = [
                                i.center for i in dots if i not in selected]
                            poly.addInsideDots(not_selected)

                            # print(not_selected)

                            selected = []
                            can_select = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


class GridRect(pygame.Rect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = WHITE


class Polygon:
    def __init__(self, vertices, color=WHITE):
        self.vertices = vertices
        self.color = color

    def draw(self):
        pygame.draw.polygon(screen, self.color, self.vertices, 3)

    def isInside(self, dot):
        min_x = min(v[0] for v in self.vertices)
        max_x = max(v[0] for v in self.vertices)
        min_y = min(v[1] for v in self.vertices)
        max_y = max(v[1] for v in self.vertices)

        if not (min_x < dot[0] < max_x and min_y < dot[1] < max_y):
            return False

        inside = False
        for i in range(len(self.vertices)):
            j = (i + 1) % len(self.vertices)

            try:
                if (self.vertices[i][1] > dot[1]) != (self.vertices[j][1] > dot[1]) and \
                        dot[0] <= (self.vertices[j][0] - self.vertices[i][0]) * (dot[1] - self.vertices[i][1]) / (self.vertices[j][1] - self.vertices[i][1]) + self.vertices[i][0]:
                    inside = True
                print(self.vertices[i][1] > dot[1]) != (
                    self.vertices[j][1] > dot[1])
                print(dot[0] <= (self.vertices[j][0] - self.vertices[i][0]) * (dot[1] - self.vertices[i]
                      [1]) / (self.vertices[j][1] - self.vertices[i][1]) + self.vertices[i][0])
            except ZeroDivisionError:
                inside = True

        print("inside", inside)

        return inside

    def addInsideDots(self, dots):
        for dot in dots:
            if self.isInside(dot):
                pygame.draw.circle(screen, "green", dot, 5)


def drawGrid():
    blockSize = 50
    global dots
    dots = []
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            dot = GridRect(x, y, blockSize, blockSize)
            pygame.draw.circle(screen, dot.color, dot.center, 5)
            dots.append(dot)


if __name__ == '__main__':
    main()
