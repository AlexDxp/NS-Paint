import pygame
from pygame import MOUSEBUTTONDOWN
import sys

offWHITE = (220, 220, 220)
offBLACK = (50, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKBLUE = (0, 0, 139)
BLUE = (0, 0, 255)
LIGHTBLUE = (173, 216, 230)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
MAGENTA = (255, 0, 255)
LIGHTORANGE = (255, 213, 128)
LIGHTGREEN = (144, 238, 144)
LIGHTYELLOW = (255, 255, 125)
PINK = (255, 204, 204)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Paint')
reset = True
while reset:
    screen.fill(offWHITE)

    taskbar = pygame.draw.rect(screen, offBLACK, [0, 0, 800, 100])

    brush1 = pygame.image.load('Brush Sizes/Thinest 1.png')
    brush2 = pygame.image.load('Brush Sizes/Default 2.png')
    brush3 = pygame.image.load('Brush Sizes/Thickish 3.png')
    brush4 = pygame.image.load('Brush Sizes/THICKEST 4.png')
    screen.blit(brush1, (0, 475))
    screen.blit(brush2, (0, 350))
    screen.blit(brush3, (0, 225))
    screen.blit(brush4, (0, 100))

    barrier1 = pygame.draw.rect(screen, BLACK, [0, 100, 800, 2])
    barrier2 = pygame.draw.rect(screen, BLACK, [60, 100, 2, 600])
    barrier3 = pygame.draw.rect(screen, BLACK, [0, 100, 2, 600])
    barrier4 = pygame.draw.rect(screen, BLACK, [798, 100, 2, 600])
    barrier5 = pygame.draw.rect(screen, BLACK, [0, 598, 800, 2])
    barrier6 = pygame.draw.rect(screen, BLACK, [0, 475, 60, 2])
    barrier7 = pygame.draw.rect(screen, BLACK, [0, 350, 60, 2])
    barrier8 = pygame.draw.rect(screen, BLACK, [0, 225, 60, 2])

    black = pygame.draw.circle(screen, BLACK, [775, 25], 10)
    white = pygame.draw.circle(screen, WHITE, [750, 25],10)
    darkblue = pygame.draw.circle(screen, DARKBLUE, [725, 25],10)
    blue = pygame.draw.circle(screen, BLUE, [700, 25],10)
    lightblue = pygame.draw.circle(screen, LIGHTBLUE, [675, 25],10)
    red = pygame.draw.circle(screen, RED, [775, 50],10)
    yellow = pygame.draw.circle(screen, YELLOW, [750, 50],10)
    green = pygame.draw.circle(screen, GREEN, [725, 50],10)
    orange = pygame.draw.circle(screen, ORANGE, [700, 50],10)
    purple = pygame.draw.circle(screen, PURPLE, [675, 50],10)
    pink = pygame.draw.circle(screen, PINK, [775, 75],10)
    lightyellow = pygame.draw.circle(screen, LIGHTYELLOW, [750, 75],10)
    lightgreen = pygame.draw.circle(screen, LIGHTGREEN, [725, 75],10)
    lightorange = pygame.draw.circle(screen, LIGHTORANGE, [700, 75],10)
    magenta = pygame.draw.circle(screen, MAGENTA, [675, 75],10)

    eraser = pygame.image.load('Images/Eraser.png')
    screen.blit(eraser, (575, 11))
    square = pygame.image.load('Shapes/SQUARE.jpg')
    screen.blit(square, (525, 10))
    circle = pygame.image.load('Shapes/CIRCLE.jpg')
    screen.blit(circle, (525, 52))
    draw = pygame.image.load('Shapes/DRAW.jpg')
    screen.blit(draw, (483, 10))
    line = pygame.image.load('Shapes/LINE.png')
    screen.blit(line, (483, 52))

    reset = pygame.image.load('Images/Reset.png')
    screen.blit(reset, (358, 11))

    thin = pygame.image.load('Images/Thin.png')
    thick = pygame.image.load('Images/Thick.png')
    screen.blit(thick, (440, 10))
    screen.blit(thin, (440, 52))
    reset = False

pygame.display.flip()
SHAPE = "DRAW"
size = 3
COLOUR = BLACK
prev_x, prev_y = None, None
line_start = None
line_end = None
count = 0
loops = 0
widthS = 0
widthC = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if MOUSEBUTTONDOWN:
        button = pygame.mouse.get_pressed()
        if button[0]:
            x, y = pygame.mouse.get_pos()
            if 0 <= x <= 60 and 100 < y <= 225:
                size = 5
            elif 0 <= x <= 60 and 225 < y <= 350:
                size = 4
            elif 0 <= x <= 60 and 350 < y <= 475:
                size = 3
            elif 0 <= x <= 60 and 475 < y <= 600:
                size = 2
            if 765 < x <= 785 and 13 < y < 32:
                COLOUR = BLACK
            elif 740 < x <= 760 and 13 < y < 32:
                COLOUR = WHITE
            elif 715 < x <= 735 and 13 < y < 32:
                COLOUR = DARKBLUE
            elif 690 < x <= 710 and 13 < y < 32:
                COLOUR = BLUE
            elif 665 < x <= 685 and 13 < y < 32:
                COLOUR = LIGHTBLUE
            elif 765 < x <= 785 and 39 < y < 59:
                COLOUR = RED
            elif 740 < x <= 760 and 39 < y < 59:
                COLOUR = YELLOW
            elif 715 < x <= 735 and 39 < y < 59:
                COLOUR = GREEN
            elif 690 < x <= 710 and 39 < y < 59:
                COLOUR = ORANGE
            elif 665 < x <= 685 and 39 < y < 59:
                COLOUR = PURPLE
            elif 765 < x <= 785 and 63 < y < 83:
                COLOUR = PINK
            elif 740 < x <= 760 and 63 < y < 83:
                COLOUR = LIGHTYELLOW
            elif 715 < x <= 735 and 63 < y < 83:
                COLOUR = LIGHTGREEN
            elif 690 < x <= 710 and 63 < y < 83:
                COLOUR = LIGHTORANGE
            elif 665 < x <= 685 and 63 < y < 83:
                COLOUR = MAGENTA
            elif 574 <= x <= 654 and 10 <= y <= 90:
                COLOUR = offWHITE
                SHAPE = "ERASER"
            elif 525 <= x <= 565 and 10 <= y <= 50:
                if COLOUR == offWHITE:
                    COLOUR = BLACK
                SHAPE = "SQUARE"
            elif 525 <= x <= 565 and 52 <= y <= 92:
                if COLOUR == offWHITE:
                    COLOUR = BLACK
                SHAPE = "CIRCLE"
            elif 483 <= x <= 523 and 10 <= y <= 50:
                if COLOUR == offWHITE:
                    COLOUR = BLACK
                SHAPE = "DRAW"
            elif 483 <= x <= 523 and 52 <= y <= 92:
                if COLOUR == offWHITE:
                    COLOUR = BLACK
                SHAPE = "LINE"
            elif 440 <= x <= 480 and 10 <= y <= 50:
                if SHAPE == "SQUARE":
                    widthS = 0
                elif SHAPE == "CIRCLE":
                    widthC = 0
            elif 440 <= x <= 480 and 52 <= y <= 92:
                if SHAPE == "SQUARE":
                    widthS = 1
                elif SHAPE == "CIRCLE":
                    widthC = 1
            elif 358 <= x <= 442 and 11 <= y <= 91:
                pygame.draw.rect(screen, offWHITE, (62, 102, 736, 496), 0)
                pygame.display.flip()
            print(x, y)
            if 64 <= x < 800 and 104 <= y < 600:
                if prev_x is not None and prev_y is not None:
                    if COLOUR == offWHITE:
                        pygame.draw.rect(screen, COLOUR, [x - 9, y - 9, 20, 20])
                        pygame.draw.line(screen, COLOUR, (prev_x, prev_y), (x, y), 30)
                    else:
                        if SHAPE == "SQUARE":
                            pygame.draw.rect(screen, COLOUR, [x - 9, y - 9, 20, 20],widthS)
                            count = 0
                        elif SHAPE == "CIRCLE":
                            pygame.draw.circle(screen, COLOUR, [x - 4, y - 4], 15,widthC)
                            count = 0
                        elif SHAPE == "DRAW":
                            pygame.draw.line(screen, COLOUR, (prev_x, prev_y), (x, y), size * 3)
                            pygame.draw.circle(screen, COLOUR, [x, y], size)
                            count = 0
                if SHAPE == "LINE":
                    while True:
                        if count == 0:
                            if MOUSEBUTTONDOWN:
                                if button[0]:
                                    line_start = (x, y)
                                    count = 1
                                    break
                        if count == 1:
                            if MOUSEBUTTONDOWN:
                                if button[0]:
                                    new_x, new_y = pygame.mouse.get_pos()
                                    line_end = (new_x, new_y)
                                    pygame.draw.line(screen, COLOUR, line_start, line_end, size * 2)
                                    pygame.display.flip()
                                    line_start = None
                                    line_end = None
                                    count = 0


                prev_x, prev_y = x, y
                pygame.display.flip()
        else:
            prev_x, prev_y = None, None