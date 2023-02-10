import pygame as pg
from random import randrange

# create window/screen for game to show up on
WINDOW = 1000
screen = pg.display.set_mode([WINDOW] * 2)
# instance of clock class to set frame rate
clock = pg.time.Clock()

# main loop of program
while True:
    # check for closing of program
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill('black')
    pg.display.flip()
    clock.tick(60)
