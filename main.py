import pygame as pg
from random import randrange

# create window/screen for game to show up on
WINDOW = 1000
# since game is in form of grid break into tiles
TILE_SIZE = 50
# tuple that defines range for rand coordinates
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
def get_random_position(): return [randrange(*RANGE), randrange(*RANGE)]


snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
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
    # draw snake
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    pg.display.flip()
    clock.tick(60)
